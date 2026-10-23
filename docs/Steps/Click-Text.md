# Click Text

Click Text finds visible text, moves to the accepted target, and verifies the same text again before pressing the mouse button.

## Fields

| Field | Meaning |
| --- | --- |
| Text | The phrase to find; may use `{variables}` |
| Match characters | All text by default, or a character filter |
| Keep characters | Required allowed characters for Custom chars |
| Screen zone | Where to search |
| Mouse button | M1 left, M2 right, M3 middle, M4 back, or M5 forward |
| Delay after found (seconds) | Configured delay before clicking |
| Hold seconds | How long to hold; `0` moves without clicking |
| Click offset | Offset from the recognized center, constrained to the verified text |

Keep the offset at `0,0` for ordinary labels and buttons. This action does not authorize clicking an unrelated control outside the verified text. Use a separate explicit mouse action if that is your intended workflow.

## Example

```text
Click Text
Text: Submit
Match characters: All text
Screen zone: selected dialog area
Mouse button: M1
Click offset: 0,0
```

To find `12` inside `Score:12`, choose Numbers only and enter `12`. The query must already fit its filter. Entering `Score12` under Numbers only is an error, not a search for a silently modified number.

## Before The Click

The final check uses the same phrase and character filter, real OCR boxes, and a fresh pixel-persistence check. It does not guess a substring position from its length.

If the target is absent or keeps moving, the action can retry up to three guarded attempts, then skip and continue. Capture/recognition errors and actual input-delivery failures stop playback. A high confidence result alone does not bypass the final check.

Use a specific phrase and a narrow area if several copies are visible. Test the area with [Read Text](Read-Text.md) when the returned characters are unclear.

## Related Pages

- [Text Recognition And Character Filters](../Recognition/Text.md)
- [Text Clicks Wrong Place](../Troubleshooting/Text-Clicks-Wrong-Place.md)
- [Click Image](Click-Image.md)
