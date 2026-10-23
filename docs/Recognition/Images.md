# Smart And Pixel Image Recognition

Image actions search for the reference image you provide. They do not take an object name such as “any green button” and detect every example of that category.

The **Recognition** selector is available on [If Image](../Steps/If-Image.md), [Click Image](../Steps/Click-Image.md), [If Image Click](../Steps/If-Image-Click.md), and [Image Watcher](../Watchers/Triggers/When-Image.md).

| Recognition | Use it when | Important limit |
| --- | --- | --- |
| Smart | The same target can change size, lighting, or appearance | Similar-looking or heavily changed targets can still be rejected or confused |
| Pixel | The reference should appear at its original pixel size | There is no scaling or learned fallback |

## Smart

Smart is the default. It combines local learned visual features, geometric agreement, and image-identity checks. It is designed to tolerate more variation than literal pixel matching, including some scale, lighting, and partial-visibility changes. It does not guarantee a match under every change.

Use a distinctive reference with enough visible structure. Avoid blank areas, generic borders, or a tiny fragment shared by many controls. Narrow the search area when the same target appears in several places.

## Pixel

Pixel checks the image at its original dimensions. At tolerance `0`, every included red, green, and blue value must match exactly. A tolerance of `3` permits a difference of at most `3` in each channel of every included pixel; it is not an average similarity score.

Changing display scale, zoom, font rendering, hover state, or animation can break a Pixel match. Increasing tolerance does not allow resizing. See [Pixel Recognition](Pixel.md) for transparency and color-check details.

## References And Clicks

Use the Image field to browse for a file. The editor also supports pasted image data and previews. Check the preview after replacing a reference so that the intended image is selected.

Image clicks are verified again after the configured cursor movement and delay. If the target moved or disappeared, WhirlyTask can search again for the same reference, up to three guarded attempts. It preserves the configured delay for each new target.

After target-loss exhaustion, ordinary Click Image skips and continues. If Image Click chooses Else. A missing image, invalid configuration, unavailable recognition, failed capture, or real input-delivery failure stops playback; those errors do not authorize Else.

Use [If Image Click](../Steps/If-Image-Click.md) when Then must depend on a delivered click. A separate If Image followed by Click Image performs two independent actions and is not equivalent.

## Related Pages

- [Image Not Found](../Troubleshooting/Image-Not-Found.md)
- [Selected Area Problems](../Troubleshooting/Selected-Area-Problems.md)
