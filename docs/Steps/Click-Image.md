# Click Image

Click Image locates a reference image and verifies the accepted target again before mouse-down.

## Fields

| Field | Meaning |
| --- | --- |
| Image | Reference file or pasted image data; check the preview |
| Recognition | Smart by default, or Pixel for an original-size literal match |
| Pixel tolerance (0–255) | Maximum RGB-channel difference per included pixel; Pixel only |
| Screen zone | Where to search |
| Cursor mode | Move or Teleport |
| Mouse button | M1 left, M2 right, M3 middle, M4 back, or M5 forward |
| Delay before click (seconds) | Delay applied for each newly accepted target |
| Hold seconds | Button hold duration; `0` moves without pressing |
| Click offset | Offset from the recognized center, kept inside the verified image |

## Example

```text
Click Image
Image: ready-icon.png
Recognition: Smart
Screen zone: selected toolbar area
Cursor mode: Teleport
Mouse button: M1
Click offset: 0,0
```

Smart is designed for the same target with some visual variation. Pixel requires its original size and compares every included pixel. At tolerance `0`, Pixel is exact; it does not fall back to Smart if the reference differs.

## Moving Or Missing Targets

After movement and the configured delay, the action checks target identity again. If the target moved or disappeared, it can reacquire the same reference, up to three guarded delivery attempts. Each new target keeps your configured delay.

If no stable target remains, ordinary Click Image skips and playback continues. Invalid input, an unavailable recognizer, capture failure, or actual mouse-delivery failure stops playback.

Use [If Image Click](If-Image-Click.md) when the following branch must depend on successful delivery. A separate If Image check does not guarantee a later Click Image will still find that target.

Offsets do not authorize clicks outside the verified image. Keep `0,0` for the recognized center; use a separate explicit cursor/mouse action for an unrelated location.

## Related Pages

- [Smart And Pixel Image Recognition](../Recognition/Images.md)
- [Pixel Recognition](../Recognition/Pixel.md)
- [Image Not Found](../Troubleshooting/Image-Not-Found.md)
