# If Pixel

If Pixel checks whether **at least one real screen pixel** in an area matches a chosen RGB color. It then chooses Then or Else.

## Fields

| Field | Meaning |
| --- | --- |
| Color / Hex color | Target `#RRGGBB`; choose, type, or use the color picker |
| Mode | is seen or is not seen |
| Screen area | Area in which a matching pixel can satisfy the condition |
| Color tolerance (0–255) | Maximum difference allowed independently in red, green, and blue |
| Then / Else | Steps chosen after a valid check |

Tolerance `0` is exact. At tolerance `3`, target RGB `(100,120,140)` accepts `(103,117,142)`, but rejects `(104,120,140)` because one channel differs by `4`.

## Example

```text
If Pixel
Hex color: #00CC66
Mode: is seen
Screen area: selected status-indicator area
Color tolerance: 0
Then: Status Message: Indicator color is present
Else: Status Message: Indicator color is absent
```

Select a small, useful area. A broad area containing an unrelated pixel of the same color also satisfies is seen. This step does not require the entire area to be one color or identify the shape of an object.

With is not seen, Then requires a completed check finding no matching pixel. Invalid color/tolerance/area or failed capture stops playback before either branch. Monitor gaps are not treated as black screen pixels.

For a whole image rather than any pixel of a color, use [If Image](If-Image.md) with Recognition: Pixel. For visual changes in size or appearance, consider Smart recognition.

## Related Pages

- [Pixel Recognition](../Recognition/Pixel.md)
- [Selected Area Problems](../Troubleshooting/Selected-Area-Problems.md)
