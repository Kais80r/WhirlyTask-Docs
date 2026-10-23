# Editor Changes Disappear

Check the open document name, its source and save status. Save updates the file or Library entry you opened; an independent copy and the recovery session can contain different editing states.

| Symptom | What to check |
| --- | --- |
| Changes still show as unsaved | Use Save and wait for confirmation; cancelling or a write error does not save them |
| A Library item does not include your edits | Open that entry and use Save; saving a separate file does not update its Library copy |
| Save opens a file dialog | This document does not have a working file yet; choose its name and location |
| Save As changes the document name | You are now editing the newly selected file |
| New or Open stops at a question | Choose Save, Don't Save or Cancel for the unsaved document |
| Playback refuses the current graph | Fix Editor Issues; unfinished documents can be saved before they are playable |

The open graph is checked before playback. A failed editor response or invalid graph must not silently start a different editing state.

Automatic recovery restores editing work across a restart, including unsaved changes. Use Save to update its file or Library entry, or Save As for a file you want to share. Edits made while a save is pending still need saving afterward.

The native Track Editor has its own Save/Cancel controls for recording settings.

See [Editors And Saving](../App-Features/Editors-And-Saving.md), [Library And Files](../App-Features/Library-And-Files.md), and [Graph Editor](../App-Features/Graph-Editor.md).
