# If Text

If Text checks visible text and chooses Then or Else after a valid recognition result.

## Fields

| Field | Meaning |
| --- | --- |
| Text | The phrase to search for; may use `{variables}` |
| Match characters | All text or a character filter |
| Keep characters | Allowed characters for Custom chars |
| Mode | is seen or is not seen |
| Screen zone | Where to check |
| Then / Else | Steps chosen by the condition |

With **is seen**, Then runs for a match and Else for valid absence. With **is not seen**, those results are inverted. An invalid filter/query, capture failure, unavailable OCR worker, or unavailable exact filtered-text position stops playback before either branch.

## Example

```text
If Text
Text: Complete
Match characters: All text
Mode: is seen
Screen zone: selected status area
Then: Status Message: Finished
Else: Status Message: Not complete
```

For a numeric label such as `Score:12`, choose Numbers only and search for `12`. Enter only characters permitted by the selected filter. The query is not automatically stripped or corrected.

Use [Wait For](Wait-For.md) when playback should wait until a state appears. If Text decides from the current check; it does not keep waiting for a future match.

Use [Click If Text](Click-If-Text.md) when the target should be clicked and Then must depend on successful delivery. An If Text check alone does not guarantee that a later click still has the same accepted target.

Keep the full word and margin inside the area. Under All text, `Start` does not match `Restart`, and `10` does not match `1.0`. These rules reduce accidental activations but cannot eliminate OCR mistakes.

## Related Pages

- [Text Recognition And Character Filters](../Recognition/Text.md)
- [If Image](If-Image.md)
- [Selected Area Problems](../Troubleshooting/Selected-Area-Problems.md)
