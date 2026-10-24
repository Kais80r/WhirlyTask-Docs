# Recording Options

Recording options control which input is captured into new tracks. Changing an option does not rewrite events already recorded in an existing track.

Open **Menu > Recording**.

| Option | Effect |
| --- | --- |
| Record Mouse Movement | Capture pointer movement between actions |
| Record Mouse Buttons/Wheel | Capture mouse buttons and wheel input |
| Record Mouse Positions | Store positions with mouse actions |
| Record Keyboard | Capture keyboard input |

Turn off movement before recording if only the clicks matter. Turning off mouse positions changes how later mouse actions use coordinates; it does not automatically recognize the intended control.

## Test A Short Track First

1. Set the recording options.
2. Record a small, repeatable action.
3. Stop recording.
4. Replay once while watching the target window.
5. Save a named track when the result is correct.

Recorded coordinates depend on the screen layout. If controls move or the application is not always ready at the same time, build a sequence using [Wait For](../Steps/Wait-For.md), [Click Text](../Steps/Click-Text.md), or [Click Image](../Steps/Click-Image.md).

Missing keys or clicks usually warrant checking the corresponding recording option before recording again. Use [Stop or Emergency](Hotkeys.md) if playback sends unexpected input.
