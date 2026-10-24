# Image Not Found

Check which recognition mode the action uses before changing the reference or tolerance.

| Mode | Check first |
| --- | --- |
| Smart | Is the reference distinctive, visible, and still the same target? |
| Pixel | Is the target the same pixel size, with every included RGB channel within tolerance? |

## Reference And Area

- Confirm the Image preview shows the intended reference.
- Keep the complete target inside the selected area.
- Exclude changing counters, animation, hover effects, and the pointer from the reference.
- Avoid blank areas and generic fragments shared by other controls.
- Narrow the area if several copies are visible.

Smart tolerates some scale and appearance changes, but cannot guarantee recognition of a heavily changed or obscured target. Pixel has no scale adaptation or Smart fallback. Display scaling, zoom, rendering changes, or a single out-of-tolerance pixel can break a literal match.

Use an opaque crop for Pixel. Semitransparent, entirely transparent, or sparse unsupported references are unavailable, not a valid absence. Keep the target inside a physical monitor rather than spanning a monitor gap.

## Found, Then Gone

A moving target can disappear between recognition and the final click check. Click Image reacquires the same reference for up to three guarded attempts, preserving the configured delay. Exhausted target loss skips ordinary Click Image; Click If Image chooses Else.

For image condition/click steps, an unavailable worker, failed capture, invalid reference/configuration, or real input failure stops playback. Image watchers do not activate from an unavailable check. These errors must not trigger is not seen or choose Else as if absence had been verified.

## Related Pages

- [Smart And Pixel Image Recognition](../Recognition/Images.md)
- [Click Image](../Steps/Click-Image.md)
- [Click If Image](../Steps/Click-If-Image.md)
- [Pixel Recognition](../Recognition/Pixel.md)
