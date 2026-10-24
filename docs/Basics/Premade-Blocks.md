# Premade Blocks

A Premade Block is a saved selection of graph nodes that you can insert into a Sequence. The file format is **.prm**.

Create and edit reusable step selections in the Sequence graph editor.

## Save A Selection

1. Open the Sequence containing the working steps.
2. Hold **Shift** and drag a rectangle over the nodes to select them.
3. Click **Save Premade Block** at the top, or right-click the selection and choose **Save as Premade Block**.
4. Enter a unique name in the native naming dialog.

The saved block contains the selected nodes and connections between them. Connections to unselected nodes are omitted. Saving creates a Library copy and preserves your open Sequence and selection. Cancelling the name dialog leaves the workflow unchanged.

Choose a coherent runnable section. A Watcher action chain needs its selected trigger. Ambiguous fragments or invalid references are rejected rather than being silently connected to a different entry or target. Include a Starter Variable when the reusable section must declare its own start value.

## Import A Saved Block

1. Clear the current selection.
2. Click **Import Premade Block**.
3. Choose the saved Library block.
4. Position and connect the imported nodes to the surrounding workflow.
5. Check block targets, variable names, and screen areas before playback.

Import inserts a copy. Editing that copy does not update the saved Library block, and changing the Library block does not update copies already inserted. Internal Step IDs are remapped during import to avoid collisions.

## Share A File

Use the Library's Blocks file actions to save or load a **.prm** file. A named Library item and a portable file are separate copies; keep file backups when needed.

For a complete walkthrough, see [Reusable Premade Blocks](../Guides/Reusable-Premade-Blocks.md). For saving the open workflow to a file, see [Editors And Saving](../App-Features/Editors-And-Saving.md).
