# Editorial glass page transitions

Use this treatment for presenter-led reports when page-by-page progression supports the story. Keep ordinary reading natural and preserve accessible controls.

## Visual model

- Build vertically stacked, translucent light sheets over a quiet pale background.
- On forward progression, the next sheet rises over the current one. Reverse progression reveals the previous sheet.
- Use a restrained static backdrop blur, a readable translucent surface, a subtle border and shadow, and a slight outgoing-sheet scale, around 1 to 0.97 as a starting point.
- Animate translation and opacity. Do not animate full-page blur or distort text. Keep the outgoing evidence visible until the incoming page covers it.
- Keep an opaque readable fallback when backdrop filtering is unavailable.

## Native scrolling first

Start with one native vertical scroller and CSS scroll snapping. Use full-height snap areas, start alignment and stop-at-page-boundary behavior where supported. Do not use a horizontal carousel.

Long content must have a free reading interval before another page transition. Allocate scroll distance for the viewport plus the page's real overflow. A gesture inside a long page belongs to reading that page; absorb remaining wheel, trackpad or touch inertia at the boundary. Reaching an edge must not turn the page in the same gesture. Only a fresh outward gesture that starts at the edge may enter one adjacent page.

Recalculate after resize, font/image load, disclosure and language changes. Preserve the selected page and valid reading offset. Add sticky stages and scroll-linked transforms only when the requested layering requires them.

## Damping and gesture feel

Let native scrolling provide most of the resistance and settling. For discrete edge gestures, use a short transition that responds to gesture direction and intensity but always settles at a complete page boundary. Avoid a rigid one-wheel-event/one-page mapping. Ignore tiny trackpad noise, coalesce repeated events while a transition is active, and prevent a single continuous gesture from skipping multiple sheets. Pointer/touch handling must not trap normal reading or browser zoom.

## Accessibility and reduced motion

Keep page headings, content order and keyboard focus in document order. Provide visible previous/next controls and keyboard navigation where appropriate. Do not make scroll snap the only way to reach content. Under `prefers-reduced-motion`, use instant or restrained transitions while preserving page state and all controls. Avoid parallax that impairs reading.

## Acceptance

Inspect a real artifact with long and short pages. Exercise slow and fast wheel/trackpad gestures, touch, reverse direction, reading overflow, boundary gestures, resize, keyboard, fullscreen and reduced motion. Confirm that the transition visibly overlaps two sheets and settles cleanly. Static checks cannot establish damping, frame rate or native gesture feel.
