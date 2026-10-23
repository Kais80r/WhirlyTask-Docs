# Watcher Pauses And Never Continues

After Stop Block, recovery must decide where the work block should start again. Stop Block does not remember a resumable pause point. Reaching a later wait or failing a click is not a continuation instruction.

| Intended result | Action to consider |
| --- | --- |
| Start a work block at a known step | Start Block at Step |
| Transfer the current path to another block step | Jump Block Step |
| Start a fresh run from its initial state | Reset and Restart Sequence |
| End automation | Finish Sequence |

```text
Watcher steps:
1. Stop Block: Work
2. Click Text: OK
3. Start Block at Step: Work / retry-step-id
```

Check that the destination Step ID exists and belongs to the intended block. A recovery action can stop on missing variables, unavailable recognition, or failed input; read the status message before assuming the restart was reached.

Use Status Message before the recovery action and before the exit. Add bounded timeouts to waits and a cooldown so the same visible warning does not immediately retrigger recovery.

Reset and Restart Sequence restores the run's starting variable state; it is not merely a jump back to the first action.

See [Watchers](../Watchers/README.md), [Stop Block](../Steps/Stop-Block.md), [Start Block at Step](../Steps/Start-Block-at-Step.md), and [Reset and Restart Sequence](../Steps/Reset-And-Restart-Sequence.md).
