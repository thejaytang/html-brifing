# Repository guidance

Read README.md, PROJECT_STATE.md and the task-relevant plugin references. The distributable entrypoint is plugins/html-brifing/skills/html-brifing/SKILL.md. Keep the requested identifier html-brifing.

Always preserve evidence boundaries, optional helper reuse, user scope, accessible interaction and offline-delivery verification. Keep third-party skills external; do not hardcode personal paths or bundle business materials. Keep English and Chinese README claims equivalent. The Chinese validation reference is intentional; README language does not assert host/runtime language support.

Validate with python3 scripts/check_package.py. For behavior changes, use the scenarios in project-support/evaluation.md and a clean destination. Structural validation does not prove model behavior or platform portability. Update PROJECT_STATE.md and relevant evidence after material changes. No project-specific dependencies are required for the stdlib checker.

Publishing requires user authorization. Never force-push, rewrite unrelated history, collect credentials or install helper skills automatically. Do not weaken acceptance to satisfy a cosmetic review budget.
