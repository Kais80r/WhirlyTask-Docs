# If Block Running

Checks whether the selected **Block** is currently executing. Follow **Then** for a running block and **Else** for a block that is not running.

Use this before starting parallel work that should have only one active instance. The target must be a valid block in the current graph.

```text
If Block Running: Work
  Then -> Status Message: Work is already active
  Else -> Start Block at Step: Work / retry-step
```

This checks execution state, not whether a window is open, a task is complete, or an application is responsive. Use an appropriate text/image/window condition for those checks.

Related: [Start Block at Step](Start-Block-at-Step.md), [Stop Block](Stop-Block.md), and [blocks](../Basics/Blocks-And-Numbering.md).
