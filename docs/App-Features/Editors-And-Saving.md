# Editors And Saving

The graph editor's draft, a named Library item, and a file export are separate things. Automatic session recovery is a fourth layer; it helps restore editing work but is not a named backup.

## Sequence Graph Editor

| Action | What it does |
| --- | --- |
| Save Draft | Validates and applies the graph as the current playback draft |
| Save New | Applies the draft and opens a dialog to create a named Library copy |
| Save As | Applies the draft and opens the Library save/overwrite workflow |
| Close / window X | Closes the editor while preserving its session; it does not mean discard |
| New or loading another document | Replaces the active editing document; save a named copy first if you need both |

Wait for the native save result. If validation fails, the editor can retain your work while playback still uses the last valid draft. A stored editor session is not proof the changed graph is ready to run.

Save Draft does not create or overwrite a named Library entry. Save New does not create a portable file. Use the explicit Library/file actions for those purposes.

## Automatic Session Recovery

The editor checkpoints its graph and editing state. Reopening can recover work, including edits that have not been applied for playback. Closing the window is not a reliable way to undo changes, and recovered work is not necessarily the version stored under a Library name.

Use Undo for an editing mistake. To deliberately return to a named version, load that version explicitly. Keep file backups of important workflows.

## Track Editor Is Different

The native Track Editor edits playback settings for a recording. Its Save applies the settings; Cancel or closing that Track Editor leaves its pending settings unapplied. Do not transfer that Save/Cancel rule to the sequence graph editor.

## Related Pages

- [Graph Editor](Graph-Editor.md)
- [Library And Files](Library-And-Files.md)
- [Editor Changes Disappear](../Troubleshooting/Editor-Changes-Disappear.md)
