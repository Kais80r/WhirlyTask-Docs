# Blocks And Step IDs

A block is a named main-flow section with an entry point. Connections determine which action runs next; the visual position of a card does not change execution order.

Select a block's header to edit its settings. Give blocks distinct descriptive names before using block-control steps.

## Step IDs Are Targets

Step IDs identify addressable steps. They are not a promise that the graph executes in numeric order. The native runtime uses the selected block and raw Step ID to resolve a target.

**Jump Block Step** and **Start Block at Step** provide two dropdowns:

1. **Block** chooses the target block.
2. **Step ID** lists valid addressable targets in that block as `ID · Step title`.

The saved value is the ID. If you change the block and the previous target no longer belongs to it, select a valid target again. An unknown imported ID remains invalid; the editor does not silently substitute the first step. Fix ambiguous or duplicate IDs rather than assuming which node will run.

Watcher chains also have ownership. A step cannot jump by ID into a different Watcher's chain.

## Choose The Right Control

| Step | Purpose |
| --- | --- |
| [Stop Block](../Steps/Stop-Block.md) | Stop the selected block |
| [Start Block at Step](../Steps/Start-Block-at-Step.md) | Start the selected block at a chosen step |
| [Jump Block Step](../Steps/Jump-Block-Step.md) | Redirect to a chosen block/step target |
| [If Block Running](../Steps/If-Block-Running.md) | Branch from the selected block's running state |

A Watcher can stop a main block while handling a side event, but the block needs an explicit restart or other continuation afterward.

## Arrange The Graph

Use Auto Layout to arrange nodes and make branches easier to follow. It changes positions, not the workflow's connections. Use the minimap and zoom to navigate a large graph, then select a node to reopen its settings.

For reuse, Shift+drag to select a coherent section and save it as a [Premade Block](Advanced-Track.md). Internal Step IDs are remapped when that saved selection is imported as a copy.
