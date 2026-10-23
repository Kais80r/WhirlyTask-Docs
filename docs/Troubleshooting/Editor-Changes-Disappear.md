# Editor Changes Disappear

First identify which version you are looking at: the open editor session, the applied playback draft, a named Library item, or a separately saved file.

| Situation | What to check |
| --- | --- |
| Editor shows changes but playback does not | Save Draft and check for a validation error |
| A named Library item does not include your edits | Save Draft alone does not overwrite it; use the Library save/overwrite workflow |
| Reopening restores unsaved edits | Automatic session recovery preserved editing work |
| Loading an item replaces current work | You explicitly loaded another document; save a named copy first if both are needed |
| Save New creates another item | Load/select the intended named copy before testing it |

Closing the graph editor with X does **not** mean discard. It preserves the session. Do not use close/reopen as Undo, and do not assume a recovered graph was validated for playback.

If a save reports invalid fields or graph structure, fix that error. The editor can retain the draft while runtime keeps the last valid graph.

The native Track Editor has separate Save/Cancel behavior for recorded-track settings. Its Cancel rule does not describe the graph editor.

See [Editors And Saving](../App-Features/Editors-And-Saving.md), [Library And Files](../App-Features/Library-And-Files.md), and [Graph Editor](../App-Features/Graph-Editor.md).
