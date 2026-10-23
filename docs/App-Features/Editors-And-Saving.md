# Editors And Saving

Use **Save** or **Ctrl+S** to update the open workflow. It writes back to the file or Library entry you opened. A new document asks for a file name and location on its first save.

## Sequence Graph Editor

| Action | What it does |
| --- | --- |
| Save / Ctrl+S | Update the open file or Library entry; choose a file location for a new document |
| Save As / Ctrl+Shift+S | Save to another file and continue editing that file |
| Open / Ctrl+O | Choose a workflow file to edit |
| Add to Library | Create a named Library copy of the open workflow |
| New | Start an empty document |
| Close / window X | Close the editor and retain its recovery session |

Sequence files use **.kseq**. Premade Block files use **.prm**. The document label identifies the open workflow; its save status shows whether changes still need saving.

## Save Your Work

You can save an unfinished workflow. Errors remain visible in Editor Issues and must be fixed before playback. Saving a file does not mean every step is ready to run.

Wait for the save confirmation. Cancelling the file dialog or encountering a write error leaves your edits and the current document association intact. If you edit during a save, those additional edits still need saving.

Before **New** or opening another document, unsaved changes offer **Save**, **Don't Save**, and **Cancel**. Save continues only after the changes have been saved. **Don't Save** replaces the open document; **Cancel** keeps it open.

## Playback

Play checks the open Sequence before running it. You do not need to save a file just to test an edit. Invalid settings or an unavailable editor response prevent that run; inspect Editor Issues and the status message.

## Automatic Session Recovery

The editor checkpoints its graph and editing state so work can be recovered after a normal restart. Recovery retains the file association and unsaved state. It does not replace **Save** or create a separate file for sharing.

Use Undo for an editing mistake. Use **Open** to load a saved file. **Save As** creates a separate working file when you want to keep another version.

## Track Editor Is Different

The native Track Editor edits playback settings for a recording. Its **Save** applies those settings; **Cancel** or closing it leaves pending settings unapplied. Use the Library's Track file actions for **.mcro** files.

## Related Pages

- [Library And Files](Library-And-Files.md)
- [Graph Editor](Graph-Editor.md)
- [Editor Changes Disappear](../Troubleshooting/Editor-Changes-Disappear.md)
