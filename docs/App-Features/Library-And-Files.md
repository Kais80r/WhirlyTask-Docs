# Library And Files

The Library holds named Tracks, Sequences, and Premade Blocks. A portable file is a separate copy for backup, transfer, or sharing.

## Named Library Items

Open **Library** and select the appropriate pane. Check the item type and selected name before loading, renaming, deleting, or overwriting anything.

For a Sequence, the graph editor provides:

| Action | Result |
| --- | --- |
| Save Draft | Validate and apply the current playable graph; no named Library item is created |
| Save New | Open the naming workflow for a new Library copy |
| Save As | Open the Library save/overwrite workflow |

Errors in the graph block those actions. Warnings do not. Automatic session recovery retains editing work separately; a recovered session is not proof that the Library version was updated.

Explicitly loading a Sequence or file takes priority over the recovered editing session. Save a named copy first when you want to keep both versions.

## Premade Blocks

Create a Premade Block in the Sequence editor:

1. Hold **Shift** and drag a rectangle over the nodes to reuse.
2. Click **Save Premade Block**, or right-click and choose **Save as Premade Block**.
3. Enter a unique name in the dialog.

This saves a selection copy without replacing the open workflow. Only selected nodes and connections between them belong to the template. Invalid or ambiguous fragments are rejected.

To insert one, clear the selection and click **Import Premade Block**. In the Library's **Blocks** pane, select the saved template and choose **Import**. The result is a copy in the graph, not a live link to the Library item.

See [Reusable Premade Blocks](../Guides/Reusable-Premade-Blocks.md) for a complete walkthrough.

## Portable Files

The Library file buttons reflect the selected item type:

| Item | File buttons / extension |
| --- | --- |
| Track | Save .mcro / Load .mcro |
| Sequence | Save .kseq / Load .kseq |
| Premade Block | Save .prm / Load .prm |

A graph document label such as `Untitled.seq` is not the Sequence Library file-dialog extension.

In **Library / Blocks**, select a template and use **Save .prm** to write it to a file. **Load .prm** adds a template to that Library; import it afterward when you want nodes in the open graph. These Premade file operations preserve the currently open Sequence.

Loading other item types can change the active draft. Confirm the selected pane and item before using a file or Library action. Keep a separate file backup of important workflows rather than relying only on the current draft or recovery session.

## Check Dependencies After Transfer

Verify referenced Tracks, app paths, variable names, screen zones, and block targets on the destination PC. Embedded image data travels with the saved graph, but an unresolved external image path must be corrected before it can be safely saved and run.

See [Editors And Saving](Editors-And-Saving.md), [Track](../Basics/Track.md), and [Premade Blocks](../Basics/Premade-Blocks.md).
