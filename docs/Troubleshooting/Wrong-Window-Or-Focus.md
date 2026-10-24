# Wrong Window Or Focus

Keyboard input normally goes to the foreground application. Recorded mouse coordinates depend on the current screen layout. A window being open does not mean it is focused or ready.

## Check Before Sending Input

- Open the intended application and keep it visible.
- Use Focus Window when the sequence needs a particular window.
- Use a Window condition or Wait For Window to verify the state that matters.
- Check the loaded item and recording's display layout.
- Move WhirlyTask away if Always on Top covers the target.

Text/image clicks locate visible pixels, but they do not make every later keyboard action target that application automatically. Confirm focus before typing.

If recorded coordinates drift after a resize, zoom, or monitor change, restore the expected layout or use a recognition-based sequence instead of a fixed-coordinate recording.

If Windows blocks input into a more privileged application, check the reported delivery error and application privilege levels. Do not treat a failed click as successful simply because recognition found the target.

Use Stop or F12 Emergency if input is reaching the wrong application.

See [Focus Window](../Steps/Focus-Window.md), [Wait For](../Steps/Wait-For.md), [Hotkeys](../App-Features/Hotkeys.md), and [Selected Area Problems](Selected-Area-Problems.md).
