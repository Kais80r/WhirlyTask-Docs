# Window Watcher

Window Watcher checks the state of a window identified by **Window title**.

## Fields

| Field | Choices or meaning |
| --- | --- |
| Window title | The target window title |
| Mode | is focused, is not focused, is open, is not open, is fullscreen, is not fullscreen |
| Check every seconds | Requested interval between checks |

Set the shared [Enabled, cooldown, and conflict settings](../Watcher-Settings.md) afterward.

Choose the mode that represents the event you care about. An open window may be behind another app, so is open is different from is focused. Changing focus as recovery can also affect the main flow while it is still running.

Start with a Status Message action to verify the title and state. If recovery sends keys or clicks, use explicit block control when parallel main actions would be unsafe.

See [Focus Window](../../Steps/Focus-Window.md) and [Controlling Main Blocks](../Steps/Pause-Sequence.md).
