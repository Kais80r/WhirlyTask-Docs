# Library And Files

**Save** or **Ctrl+S** updates the workflow you opened. Open a file to save back to that file, or open a Library entry to save back to that entry. The Library holds named Tracks, Sequences and Premade Blocks that you can load or reuse.

## Workflow Files

| Workflow | File extension |
| --- | --- |
| Track | .mcro |
| Sequence | .kseq |
| Premade Block | .prm |

In the graph editor, **Save** asks for a file name and location when a new document has no saved source yet. Subsequent saves update that file. A document opened from the Library saves back to its Library entry. **Save As** writes another file and makes it the open document. **Open** or **Ctrl+O** opens a workflow file.

You can save unfinished graph documents. Check Editor Issues before playback. If a file dialog is cancelled or a write fails, the editor retains your work and does not claim it was saved.

## Add A Workflow To The Library

Use **More > Add to Library** in the editor and enter a name. The Library receives a separate copy. Editing or saving the open file does not update that copy automatically.

Open **Library** and choose **Tracks**, **Sequences**, or **Blocks** to manage its named items. Select the intended item before loading, renaming, deleting, or replacing it.

Loading a Library item makes it the open document. **Save** writes your edits back to that entry. Use **Save As** to keep a separate file on your PC.

## Premade Blocks

Create a Premade Block in the Sequence editor:

1. Hold **Shift** and drag a rectangle over the nodes to reuse.
2. Click **Save Premade Block**, or right-click and choose **Save as Premade Block**.
3. Enter a unique name in the dialog.

This saves a Library copy of the selected nodes and connections between them. Invalid or ambiguous fragments are rejected. It leaves the open Sequence intact.

Clear the selection and click **Import Premade Block** to insert a saved template. In the Library's **Blocks** pane, select it and choose **Import**. Imported nodes are a copy you can edit in the Sequence.

See [Reusable Premade Blocks](../Guides/Reusable-Premade-Blocks.md) for a complete walkthrough.

## Library File Actions

The Library's file buttons use the extension of the selected item type. In **Blocks**, **Save .prm** writes a selected template to a file and **Load .prm** adds a file to the Library. Import the template afterward to place its nodes in the open Sequence.

Library copies and workflow files are independent. Keep the copy you intend to reuse up to date explicitly.

## Check Dependencies After Transfer

Verify referenced Tracks, app paths, variable names, screen zones, and block targets on the destination PC. Embedded image data travels with the graph; an unresolved external image path needs attention before recognition can use it.

See [Editors And Saving](Editors-And-Saving.md), [Track](../Basics/Track.md), and [Premade Blocks](../Basics/Premade-Blocks.md).
