# Click If Text

Click If Text finds visible text, verifies the accepted target, attempts the click, and runs Then only after the mouse click was delivered. Confirmed absence or target loss selects Else.

## Fields

| Field | Meaning |
| --- | --- |
| Text | The phrase to find; may use `{variables}` |
| Match characters | All text by default, or a character filter |
| Keep characters | Required allowed characters for Custom chars |
| Screen zone | Where to search |
| Cursor mode | Move or Teleport |
| Mouse button | M1 left, M2 right, M3 middle, M4 back, or M5 forward |
| Delay before click (seconds) | Configured delay before clicking |
| Hold seconds | Positive duration of the button press |
| Click offset | Offset from the recognized center, kept inside the verified text |

**Hold seconds must resolve to a finite value greater than zero.** Moving the cursor without pressing a button cannot count as a delivered click. Delay and hold may use `{variables}`; the resolved values are checked at runtime.

Keep Click offset at `0,0` for ordinary labels and buttons. An offset does not authorize a click outside the verified text.

## Outcomes

| Outcome | Behavior |
| --- | --- |
| Click delivered to the verified text target | Then |
| Valid search found no matching text | Else |
| Target kept disappearing or moving through three guarded attempts | Else |
| Capture, OCR, filter/query, or configuration error | Stop; neither branch |
| Real input-delivery failure | Stop; neither branch |
| Playback stopped | Neither branch |

Each attempt uses the same phrase, character filter, and search area. The final guard checks the text again and verifies fresh target pixels before mouse-down. It uses real OCR bounds rather than guessing a substring position from its length. If the required filtered characters cannot be located safely, recognition is unavailable; this does not authorize Else.

## Example

```text
Click If Text
Text: Submit
Match characters: All text
Screen zone: selected dialog area
Cursor mode: Teleport
Mouse button: M1
Delay before click (seconds): 0
Hold seconds: 0.05
Click offset: 0,0
Then: Status Message: Click delivered
Else: Status Message: No stable text target to click
```

For a numeric label such as `Score:12`, choose Numbers only and search for `12`. The query must already contain only characters allowed by its filter. Entering `Score12` with Numbers only is an error, not a search for a silently rewritten number.

Then confirms input delivery. It does not prove the target application completed the requested operation. Add [Wait For](Wait-For.md) afterward when the next action depends on a visible result.

A separate If Text followed by Click Text performs two independent actions. Use Click If Text when the branch must depend on the verified click itself.

## Related Pages

- [Click Text](Click-Text.md)
- [If Text](If-Text.md)
- [Text Recognition And Character Filters](../Recognition/Text.md)
- [Text Clicks Wrong Place](../Troubleshooting/Text-Clicks-Wrong-Place.md)
- [Click If Image](Click-If-Image.md)
