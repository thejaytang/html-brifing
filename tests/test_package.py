"""Mutation checks prove the checker detects broken packages, not just this tree."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('checker', ROOT / 'scripts/check_package.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PackageChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'package'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', '.venv'))

    def test_valid_package(self):
        self.assertEqual(checker.check(self.root), [])

    def test_reintroduced_setup_entry(self):
        skills = self.root / 'plugins/html-brifing/skills'
        shutil.copytree(skills / 'html-brifing', skills / 'html-brifing-setup')
        self.assertTrue(checker.check(self.root))

    def test_missing_skill(self):
        (self.root / 'plugins/html-brifing/skills/html-brifing/SKILL.md').unlink()
        self.assertTrue(checker.check(self.root))

    def test_missing_bundled_entry(self):
        (self.root / 'plugins/html-brifing/skills/research-results-tables/SKILL.md').unlink()
        self.assertTrue(checker.check(self.root))

    def test_missing_plot_preset(self):
        (self.root / 'plugins/html-brifing/skills/academic-research-plotting/assets/journal_presets.json').unlink()
        self.assertTrue(checker.check(self.root))

    def test_missing_upstream_notice(self):
        (self.root / 'plugins/html-brifing/skills/academic-humanizer/LICENSE').unlink()
        self.assertTrue(checker.check(self.root))

    def test_missing_gsap_module(self):
        (self.root / 'plugins/html-brifing/skills/gsap-timeline/SKILL.md').unlink()
        self.assertTrue(checker.check(self.root))

    def test_modified_bundled_script(self):
        target = self.root / 'plugins/html-brifing/skills/ui-ux-pro-max/scripts/search.py'
        target.write_text('print("changed")')
        self.assertTrue(checker.check(self.root))

    def test_example_code_is_not_a_resource(self):
        with (self.root / 'README.md').open('a') as stream:
            stream.write('\n```html\n<img src="sample-only.png">\n```\n')
        self.assertEqual(checker.check(self.root), [])

    def test_divergent_portable_manifest(self):
        target = self.root / 'plugins/html-brifing/plugin.json'
        data = json.loads(target.read_text())
        data['version'] = '0.0.1'
        target.write_text(json.dumps(data))
        self.assertTrue(checker.check(self.root))

    def test_manifest_escape(self):
        file = self.root / 'plugins/html-brifing/.codex-plugin/plugin.json'
        data = json.loads(file.read_text())
        data['skills'] = '../../outside'
        file.write_text(json.dumps(data))
        self.assertTrue(checker.check(self.root))

    def test_broken_document_link(self):
        with (self.root / 'README.md').open('a') as stream:
            stream.write('\n[Missing](docs/absent.md)\n')
        self.assertTrue(checker.check(self.root))

    def test_invalid_svg(self):
        (self.root / 'assets/cover.svg').write_text('<svg>')
        self.assertTrue(checker.check(self.root))


if __name__ == '__main__':
    unittest.main()
