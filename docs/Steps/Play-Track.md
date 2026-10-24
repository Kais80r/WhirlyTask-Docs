# Play Track

Replays a saved mouse/keyboard recording.

| Field | Meaning |
| --- | --- |
| Track | Name of a saved recording in the Library |
| Repeat | Number of repetitions; use the editor's supported repeat choices |

Record a short track, save it to the Library, and select that exact saved name here. A missing recording cannot be replayed.

Recorded coordinates and timing depend on the desktop and application state. Before playback, focus the intended window and use a condition to check readiness where practical. Test with the same window arrangement used during recording.

```text
Start -> Focus Window: Report -> Wait: 0.5 -> Play Track: Export report / 1
      -> Status Message: Recording finished
```

Track settings control recording-specific speed, delays, and mouse offsets. A premade block is a graph template, not a recorded track: see [reusable premade blocks](../Guides/Reusable-Premade-Blocks.md).
