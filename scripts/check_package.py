#!/usr/bin/env python3
"""Check local package structure/resources; not a browser or security audit."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree


def check(root):
    root = Path(root).resolve()
    errors = []

    def fail(message):
        errors.append(message)

    def local(base, target):
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith(('#', '//')):
            return None
        path = (base / unquote(parsed.path)).resolve()
        if not path.is_relative_to(root):
            fail(f'Path outside package: {target}')
            return None
        elif not path.exists():
            fail(f'Missing local resource: {path.relative_to(root)}')
            return None
        return path

    try:
        market = json.loads((root / '.agents/plugins/marketplace.json').read_text())
        assert market['name'] == 'html-brifing'
        entry, = market['plugins']
        assert entry['name'] == 'html-brifing'
        assert entry['source'] == {'source': 'local', 'path': './plugins/html-brifing'}
        plugin = local(root, entry['source']['path'])
        assert plugin is not None
        manifest = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
        assert manifest['name'] == 'html-brifing' and manifest['license'] == 'MIT'
        assert re.fullmatch(r'\d+\.\d+\.\d+(?:\+[0-9A-Za-z.-]+)?', manifest['version'])
        assert manifest['skills'].startswith('./') and '..' not in Path(manifest['skills']).parts
        skills = local(plugin, manifest['skills'])
        assert skills and skills.is_relative_to(root)
        skill = skills / 'html-brifing/SKILL.md'
        assert skill.is_file() and skill.read_text().startswith('---\nname: html-brifing\n')
        assert (skills / 'html-brifing/agents/openai.yaml').is_file()
    except (AssertionError, KeyError, ValueError, TypeError, OSError) as exc:
        fail(f'Invalid package/skill manifest: {exc}')

    for required in ['README.md', 'README.zh-CN.md', 'LICENSE', 'AGENTS.md', 'PROJECT_STATE.md']:
        if not (root / required).is_file():
            fail(f'Missing required file: {required}')
    for path in root.rglob('*'):
        if any(part in {'.git', '.venv', '__pycache__'} for part in path.relative_to(root).parts):
            continue
        if path.is_symlink():
            fail(f'Symlink is not a portable package resource: {path.relative_to(root)}')
            continue
        if path.suffix == '.md':
            text = path.read_text()
            targets = re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', text)
            targets += re.findall(r'(?:href|src)=[\'"]([^\'"]+)[\'"]', text)
            for target in targets:
                local(path.parent, target)
        if path.suffix == '.svg':
            try:
                ElementTree.parse(path)
            except ElementTree.ParseError as exc:
                fail(f'Invalid SVG {path.relative_to(root)}: {exc}')
    return errors


if __name__ == '__main__':
    issues = check(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1])
    for issue in issues:
        print('FAIL:', issue)
    print('Package structure/resources:', 'FAIL' if issues else 'PASS')
    sys.exit(bool(issues))
