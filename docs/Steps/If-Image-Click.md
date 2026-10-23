# If Image Click

If Image Click searches for a reference image, safely attempts the click, and runs Then only after the mouse click was delivered. It combines recognition and delivery into one branch action.

## Fields

It has the same image, Recognition, Pixel tolerance, Screen zone, Cursor mode, Mouse button, delay, and offset fields as [Click Image](Click-Image.md).

**Hold seconds must resolve to a finite value greater than zero.** A move-only action cannot count as a successful click. Delay and hold can use `{variables}`; runtime validation still applies after resolution.

## Outcomes

| Outcome | Behavior |
| --- | --- |
| Click delivered to the verified target | Then |
| Valid search found no target | Else |
| Target kept disappearing/moving through three guarded attempts | Else |
| Recognition/capture unavailable or invalid configuration | Stop; neither branch |
| Real input-delivery failure or playback stopped | Neither branch |

Each retry reacquires the same reference and preserves the configured delay. The final guard verifies the target before mouse-down. It does not use a second independent Click Image step inside Then.

## Example

```text
If Image Click
Image: confirm-button.png
Recognition: Smart
Screen zone: selected dialog area
Hold seconds: 0.05
Then: Status Message: Click delivered
Else: Status Message: No stable target to click
```

Then means input delivery succeeded. It does not prove the other application completed the requested operation. Add [Wait For](Wait-For.md) afterward if you need to confirm a visible result.

## Related Pages

- [Smart And Pixel Image Recognition](../Recognition/Images.md)
- [If Image](If-Image.md)
- [Click Image](Click-Image.md)
