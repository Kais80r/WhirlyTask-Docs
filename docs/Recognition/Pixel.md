# Pixel Recognition

WhirlyTask has two different pixel features. **Pixel image recognition** checks a whole reference image. **If Pixel** checks whether any pixel in an area has a chosen color.

## Pixel Image Recognition

Choose **Recognition: Pixel** on If Image, Click Image, If Image Click, or Image Watcher.

- The reference keeps its original width and height.
- Tolerance `0` requires exact RGB equality.
- Tolerance `0–255` is the maximum permitted difference in each RGB channel of every included pixel.
- No Smart-recognition fallback runs if the literal match fails.

For example, at tolerance `3`, a reference channel value of `100` accepts `97` through `103`; `104` fails. Every other included channel and pixel must also pass. Larger tolerances admit more different images, so keep `0` when exact equality is required.

Use an opaque screen crop for the clearest result. Supported fully transparent pixels are ignored, but the image must contain enough opaque evidence. Semitransparent images, entirely transparent images, and sparse masks are rejected as unavailable rather than matched against a guessed background.

Only real observed screen areas are eligible. Synthetic gaps between monitors or obscured WhirlyTask overlays must not supply a false black-image match. Keep the complete reference target inside a physical monitor and inside the selected search area.

## If Pixel Color Checks

[If Pixel](../Steps/If-Pixel.md) searches the selected area for at least one pixel matching `#RRGGBB`, using the same maximum-per-channel meaning of tolerance.

It does not compare the whole area to a solid color, count matching pixels, identify an object, or locate an image. A broad area containing a common color can satisfy it in an unrelated location. Select the smallest useful area around the expected state.

An invalid color, tolerance, area, or failed capture stops the check. It must not become a successful **is not seen** result or an Else action.

## Related Pages

- [Smart And Pixel Image Recognition](Images.md)
- [If Pixel](../Steps/If-Pixel.md)
- [Image Not Found](../Troubleshooting/Image-Not-Found.md)
