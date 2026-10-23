# Sequence

A Sequence is an editable workflow. Connect steps to run actions, wait for a result, choose a branch, update variables, or react through Watchers.

Open **Sequence Editor...** from the main window. The toolbox has **All**, **Basic**, **Watcher**, and **Variable** tabs. Search the toolbox to find an action, then add it to the graph.

## Build The Main Path

1. Begin with a Start node and a small chain of actions.
2. Select a node to edit its settings on the right.
3. Connect each action to its successor. For conditions, connect the Then and Else paths deliberately.
4. Use **Save Draft** to validate and apply the current graph for playback.
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

**Save Draft** updates the playable draft. **Save New** creates a named Library copy. Automatic session recovery also preserves editing work, including changes not yet applied for playback. Loading a saved item explicitly replaces the current editing document.

See [Editors And Saving](../App-Features/Editors-And-Saving.md) before relying on any of these as a backup.

## Reuse A Working Section

Shift+drag to select nodes. The top **Import Premade Block** button becomes **Save Premade Block** while a selection exists. Save the selection as a named reusable copy, then clear the selection to import a saved block.

See [Premade Blocks](Advanced-Track.md), [Variables](../Values/README.md), and [Watchers](../Watchers/README.md).
