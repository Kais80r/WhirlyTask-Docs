# Playback, Speed, And Loop

Playback speed changes the timing of recorded input. A higher setting shortens recorded delays; a lower setting stretches them. It does not make a target application load faster or make OCR finish sooner.

Slow a recording down while diagnosing missed input. For readiness that varies between runs, prefer an explicit [Wait For](../Steps/Wait-For.md) condition in a sequence over assuming one fixed speed is always safe.

## Track Looping

The main Loop control and **Menu > Continuous Playback** apply to recorded tracks. Looping is not the sequence graph's control-flow system.

The configured loop count limits track repetitions. Enabling continuous playback can set a large repeat count; use Stop or Emergency to interrupt it. Check the loaded item and visible settings instead of assuming Loop means an unlimited sequence loop.

For sequence repetition, connect the graph deliberately or use [Repeat X Times](../Steps/Repeat-X-Times.md) and the documented jump steps. Give a loop a clear exit condition and allow the target application time to respond.

## Common Problems

| Problem | Check |
| --- | --- |
| Loop control is unavailable | A recorded track must be the active item |
| Clicks arrive before the application is ready | Slow the track or use a sequence with readiness checks |
| A sequence runs once | Its graph needs an explicit repeat path |
| Repeated input targets another window | Check [window focus](../Troubleshooting/Wrong-Window-Or-Focus.md) |

See [Hotkeys](Hotkeys.md) for playback controls.
