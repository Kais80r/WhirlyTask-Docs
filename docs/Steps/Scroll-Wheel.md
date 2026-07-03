# Scroll Wheel

Scroll Wheel rotates the mouse wheel at the cursor's current position.

## Fields

| Field | Meaning |
| --- | --- |
| Direction | `Down` scrolls down. `Up` scrolls up. |
| speed | How fast the wheel rotates, in wheel notches per second |
| duration | How many seconds to keep scrolling |

## Setup From Scratch

1. Add Scroll Wheel.
2. Choose `Down` or `Up`.
3. Set speed. A value like `8` means about 8 wheel notches per second.
4. Set duration. A value like `2` means keep scrolling for about 2 seconds.
5. Add Set Cursor Position before it if the scroll should happen over a specific panel or list.

## Example: Scroll Down A List

```text
1. Set Cursor Position 900,520
2. Scroll Down speed 8 /sec for 2 sec
```

This sends about 16 wheel notches over 2 seconds.

## Useful For

- Scrolling long pages, lists, or inventory panels.
- Repeating a controlled amount of wheel movement.
- Replacing a recorded wheel action with editable speed and duration.

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The wrong thing scrolls | Move the cursor over the target area first |
| It scrolls too far | Lower speed, lower duration, or both |
| It scrolls too slowly | Raise speed |
| Nothing happens | Make sure the target window is focused and the cursor is over a scrollable area |

## More About

- Moving the cursor first: [Set Cursor Position](Set-Cursor-Position.md)
- Clicking before scrolling: [Press Mouse Button](Press-Mouse-Button.md)
- Waiting between scrolls: [Wait](Wait.md)
