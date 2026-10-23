# Hotkeys

Hotkeys control recording and playback without bringing WhirlyTask to the foreground.

| Action | Default |
| --- | --- |
| Record | F8 |
| Play | F9 |
| Stop | F10 |
| Emergency stop | F12 |

The main window shows the configured recording/playback bindings. **Menu > Bindings** changes Record, Stop, and Play. F12 is reserved for emergency stopping; it is not a fourth configurable binding submenu.

Record starts/stops recording. Play runs the active loaded item or valid playback draft. Stop ends recording/playback. Emergency stopping also handles held inputs when automation must be interrupted.

## If A Binding Does Not Work

- Check the current binding shown by WhirlyTask.
- Load the intended item before pressing Play.
- Stop playback before starting a recording.
- If the status says **Hotkey busy**, another application may have registered that key; select another supported binding.
- Avoid assigning a key that the target application needs for an unrelated action.

Know the emergency key before testing input-heavy automation. Editor shortcuts such as Undo, Copy, and Paste are editing commands; they are separate from these global playback controls.

See [Testing A Sequence](../Tips/Testing-A-Sequence.md) for a small test workflow.
