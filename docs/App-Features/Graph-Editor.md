# Graph Editor

Open **Sequence Editor...** from the main window to build a connected workflow. The editor combines a toolbox, canvas, minimap, and settings for the current selection.

## Find And Configure Steps

| Control | Purpose |
| --- | --- |
| All | All available toolbox steps |
| Basic | Ordinary actions and conditions |
| Watcher | The eight background trigger cards |
| Variable | Starter, Set, Change, Reset, If Variable, and Variable Watcher |
| Toolbox search | Find types of steps to add |
| Search steps in the top bar | Find existing steps in the workspace |

Add a step from the toolbox, then select its card to edit settings on the right. The settings panel hides when no valid selection exists, giving the canvas the space back. Selecting a Watcher or an editable block header shows its own settings.

The name at the top identifies the loaded document. It is a static label, not a file-menu button.

## Connect The Workflow

Drag between step connectors to choose the next action. An If step has **Then** and **Else** outputs. Follow the connections when reading execution order; node position and Step ID numbering do not define the sequence.

Named blocks can be stopped, started, and targeted explicitly. **Jump Block Step** and **Start Block at Step** use a Block dropdown followed by a Step ID dropdown. Choose the intended target; missing or incompatible IDs are not automatically reassigned.

See [Blocks And Step IDs](../Basics/Blocks-And-Numbering.md).

## Selection And Reuse

Click a node to select it. Hold **Shift** and drag a rectangle over multiple nodes to select a group. Use the toolbar or right-click selection menu for Copy, Cut, Paste, Duplicate, and Delete.

With no selection, the top button is **Import Premade Block**. With selected nodes, it becomes **Save Premade Block**. The right-click menu also offers **Save as Premade Block**.

Saving creates a named Library copy of the selected nodes and their internal connections. It does not replace the active Sequence. Clear the selection to import a saved block as a new copy. See [Reusable Premade Blocks](../Guides/Reusable-Premade-Blocks.md).

## Navigate And Arrange

Use **Auto layout** to arrange the graph, **Fit view** to frame it, and the minimap to navigate larger workflows. Auto Layout changes node positions while preserving workflow connections. **Lock canvas** controls dragging.

Click **More** or press **Ctrl+K** for the command search. **Ctrl+F** focuses workspace search, and **Ctrl+0** fits the view. Graph Undo and Redo are available from the toolbar; editing text in a field retains normal input undo behavior. See [Hotkeys](Hotkeys.md) for app-wide shortcuts.

## Variables And Images

The Variable tab's **Variables used** overview shows configured names and sources, not live playback values. Target/result fields offer name suggestions. In supported text and value fields, choose a name and click **Insert** at the cursor or **Replace** for the entire field. Choosing a dropdown option alone does not edit the value.

Image fields support **Choose** and Ctrl+V image paste. Pasted pixels are embedded in the node. Changing a manually entered image path clears the old embedded preview, preventing an unrelated old image from remaining active.

See [Variables](../Values/README.md) and [Recognition](../Recognition/README.md).

## Read Issues Before Applying

The **Issues** badge opens errors and warnings. Select an issue to reveal its affected node and, when applicable, focus the field that needs attention. Diagnostics cover active field settings and graph structure, including invalid options, numbers, missing targets, duplicate Step IDs, and unreachable steps.

You can save unfinished documents. **Errors** must be fixed before playback; **warnings** remain visible for review. Variable references whose values are only available during playback still require runtime validation; editor checks cannot guarantee that every future screen or variable value will be valid.

Your editing session is retained while you work. Use **Save** to update the open file or Library entry and **Play** to validate and test the open graph. See [Editors And Saving](Editors-And-Saving.md).
