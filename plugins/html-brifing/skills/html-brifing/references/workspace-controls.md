# Workspace, language and viewing controls

Use this guidance for linked panes, multilingual briefings or fullscreen viewing. A single-column explanation does not need artificial panes.

## Chapter navigation

For workplace communication, project updates and narrative reports, use persistent top chapter navigation by default. Derive its order from the title outline. A learning atlas, searchable reference or tool workspace keeps navigation suited to that task.

- Use one chapter/scene model for the outline, sections, targets, active state and previous/next controls.
- Give each chapter a stable ID, full heading and short localized label. Several scenes may belong to one chapter.
- Keep language and fullscreen/exit at the right side of the top toolbar, outside transformed scene layers.
- Use semantic links or labeled buttons, stable targets, visible focus and `aria-current`.
- Keep direct navigation, reading changes, URLs, browser history and language switches aligned to the displayed chapter.

Check every chapter, backward navigation, direct links, refresh/back, long labels, narrow screens and fullscreen.

## Resizable panes

For a left-to-right workspace, allow boundary dragging and supporting-pane collapse/restore. Define usable minimum and maximum widths, clamp after resize or fullscreen changes, provide a generous grip and pointer capture, and avoid text selection during drag.

Expose keyboard resizing through a focusable separator with `role="separator"`, orientation, accessible name, `aria-controls`, and current/min/max values. Arrow keys resize; Home/End reach bounds. Keep a visible restore control. Move focus before hiding pane content. On narrow screens, use a drawer or vertical reading order instead of tiny columns.

Check drag, bounds, keyboard controls, collapse/restore, narrow windows and fullscreen.

## Languages and fullscreen

For new localized design or a language-set change, confirm one to three languages and the default. Preserve an existing set for ordinary edits. Use a compact, accessible top-right language switch; preserve valid selection, search, reading position and pane state. Avoid flags as language names.

Place one fullscreen button beside language. Keep its name and state synchronized with the browser Fullscreen API, including Escape exit; handle rejected requests clearly. Verify the actual host rather than assuming support.
