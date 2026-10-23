# Controlling Main Blocks From A Watcher

A Watcher does not automatically pause the main workflow. For recovery that requires control of the app, use explicit block-control steps.

## Stop, Recover, Resume

1. Give the main block a clear name.
2. In the Watcher action chain, add **Stop Block** and select that block.
3. Perform the recovery actions.
4. Add **Start Block at Step**, select the same block, and choose a valid Step ID from its dropdown.

The Step ID dropdown lists addressable steps in the selected block. Unknown imported IDs stay invalid; the editor does not silently substitute the first available step. Select a resume point with the state that your recovery actually produces.

Stopping a block and ending the Watcher are separate events. A stopped main block needs an explicit continuation if it should run again. If playback should end instead, use an appropriate stop or finish action.

## Avoid Accidental Parallel Input

**Run alongside other watcher** allows concurrent Watcher chains. It does not suspend the main flow, either. If several paths can click or type, design who is allowed to control input before enabling concurrency.

See [Stop Block](../../Steps/Stop-Block.md), [Start Block at Step](../../Steps/Start-Block-at-Step.md), and [Watcher Settings](../Watcher-Settings.md).
