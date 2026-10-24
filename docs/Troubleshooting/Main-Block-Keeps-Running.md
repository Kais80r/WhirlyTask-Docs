# Main Block Keeps Running During Watcher Recovery

Triggering a watcher does not automatically give it exclusive control of the main sequence. Watcher actions can run alongside the main path. Use **Stop Block** when recovery must stop a particular work block.

If recovery must take over, select the intended Block on Stop Block and put it before recovery clicks, keys, or state changes.

```text
Watcher steps:
1. Stop Block: Work
2. Handle the warning
3. Start Block at Step: Work / chosen-step-id
```

Steps before Stop Block can overlap the work block. This can be intentional for a notification, but it is usually unsuitable for two paths sending input to the same application.

Verify the trigger first with Status Message. Then confirm Stop Block is reached and points to the correct block. It does not preserve a resumable pause point; choose where work should start again explicitly.

See [Stop Block](../Steps/Stop-Block.md), [Start Block at Step](../Steps/Start-Block-at-Step.md), [Recovery Does Not Continue](Watcher-Recovery-Does-Not-Resume.md), and [Keeping Watchers Predictable](../Tips/Keeping-Watchers-Predictable.md).
