# Track

A Track is a recording of keyboard and mouse input. Use one for a short action that can be replayed from the same starting state.

A Track repeats recorded input; it does not decide whether a button or message is currently visible. A Sequence can run a Track and check the result afterward.

## A Practical First Recording

1. Put the target app in the expected starting state.
2. Start a short recording using the main window's recording controls.
3. Perform only the action you need, then stop recording.
4. Save a named Track in the Library.
5. Replay it once from the same starting state.

Use the [Track Editor](../App-Features/Editors-And-Saving.md#track-editor-is-different) for the recording's playback settings. Recording options such as mouse and keyboard capture are described in [Recording Options](../App-Features/Recording-Options.md).

## Use A Track In A Sequence

Add [Play Track](../Steps/Play-Track.md), select the saved Track, and configure its repeat setting. Add a readiness check before it if the app can take time to load, and verify the result afterward when later actions depend on success.

A recorded click is sensitive to window position, focus, and layout changes. Use [Click Text](../Steps/Click-Text.md), [Click Image](../Steps/Click-Image.md), or [Click If Image](../Steps/Click-If-Image.md) when the target should be found from the current screen.

See [Choosing What To Use](Choosing-What-To-Use.md) and [Sequence](Sequence.md).
