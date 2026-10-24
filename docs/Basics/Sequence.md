# Sequence

A Sequence is an editable workflow. Connect steps to run actions, wait for a result, choose a branch, update variables, or react through Watchers.

Open **Sequence Editor...** from the main window. The toolbox has **All**, **Basic**, **Watcher**, and **Variable** tabs. Search the toolbox to find an action, then add it to the graph.

## Build The Main Path

1. Begin with a Start node and a small chain of actions.
2. Select a node to edit its settings on the right.
3. Connect each action to its successor. For conditions, connect the Then and Else paths deliberately.
4. Use **Save** to keep the document, then **Play** to validate and test the current graph.
5. Test the short path before extending it.

The settings panel hides when nothing is selected, leaving more space for the canvas. Select a step, Watcher, or editable block header to show the relevant settings again. The document name at the top is a label.

## Separate Responsibilities

| Part | Purpose |
| --- | --- |
| Starter Variable | Declare an initial value before playback begins |
| Main blocks | Perform the normal workflow |
| If steps | Choose Then or Else from a valid result |
| Watchers | Check side conditions while playback runs |
| Premade Blocks | Insert reusable copies of saved graph selections |

A recognition error is different from a confirmed negative result. Do not design a recovery path that assumes an unavailable screenshot or OCR engine means the target is absent.

## Saving Is Explicit

**Save** or **Ctrl+S** updates the file or Library entry you opened. A new document asks for a file name and location. **Save As** creates another file and switches to it. **More > Add to Library** creates an independent Library copy. New and Open ask how to handle unsaved edits. Automatic recovery preserves the editing session across restart.

See [Editors And Saving](../App-Features/Editors-And-Saving.md) before relying on any of these as a backup.

## Reuse A Working Section

Shift+drag to select nodes. The top **Import Premade Block** button becomes **Save Premade Block** while a selection exists. Save the selection as a named reusable copy, then clear the selection to import a saved block.

See [Premade Blocks](Premade-Blocks.md), [Variables](../Values/README.md), and [Watchers](../Watchers/README.md).
