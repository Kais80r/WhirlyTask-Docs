# If Image

If Image checks for a reference image and chooses Then or Else after a valid result. It does not click the image.

## Fields

| Field | Meaning |
| --- | --- |
| Image | Reference file or pasted image; check the preview |
| Recognition | Smart or Pixel |
| Pixel tolerance (0–255) | Maximum per-channel RGB difference; Pixel only |
| Mode | is seen or is not seen |
| Screen zone | Where to search |
| Then / Else | Steps chosen by the condition |

Smart is the default and checks the reference using learned visual features and geometric agreement. Pixel checks at the reference's original dimensions, with every included pixel within tolerance. It has no Smart fallback.

## Branch Behavior

With is seen, a match selects Then and valid absence selects Else. With is not seen, those results are inverted.

Invalid image/configuration, unsupported Pixel transparency, failed capture, or unavailable recognition stops playback before either branch. A failed check is not proof that the image is absent.

```text
If Image
Image: ready-icon.png
Recognition: Smart
Mode: is seen
Screen zone: selected panel area
Then: Status Message: Ready
Else: Status Message: Not ready
```

Use [If Image Click](If-Image-Click.md) to click the same accepted target and branch only after delivery. Use [Wait For](Wait-For.md) to wait for a future state instead of choosing a branch now.

## Related Pages

- [Smart And Pixel Image Recognition](../Recognition/Images.md)
- [Image Not Found](../Troubleshooting/Image-Not-Found.md)
- [If Pixel](If-Pixel.md)
