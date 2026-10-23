# Stop Block

Stops the selected block while allowing other active blocks to continue. Choose the target in **Block**.

Stopping a block and finishing the sequence have different effects: use [Finish Sequence](Finish-Sequence.md) when the whole playback should end. Stop Block also does not create a resumable pause point. To start work again, explicitly use [Start Block at Step](Start-Block-at-Step.md) with the intended target.

A common recovery pattern is:

```text
Error Watcher -> Stop Block: Work
              -> recovery actions
              -> Start Block at Step: Work / retry-step
```

Give the Work block a clear name and give the retry action a stable **Step ID**. Check whether restarting that action might repeat an already completed external action before using this pattern.

Legacy Pause Sequence and Stop Sequence cards are normalized to current block control behavior. New sequences should use the current title and an explicit block target.
