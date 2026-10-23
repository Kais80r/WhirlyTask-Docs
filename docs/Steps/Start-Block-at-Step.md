# Start Block at Step

Starts execution at a selected step in another block while the current path continues.

| Field | Meaning |
| --- | --- |
| Block | Destination block |
| Step ID | First destination action to run |

This is useful when a watcher has recovered a problem and should start a work block again. Choose an actual stable Step ID from the selector; do not enter a visual row number.

Starting another block introduces parallel work. Shared variables remain shared, and input actions from parallel paths can interfere. Use [If Block Running](If-Block-Running.md) to avoid an unintended duplicate and [Stop Block](Stop-Block.md) to end a target explicitly.

```text
Recovery -> If Block Running: Work
  Then -> Status Message: Work is already active
  Else -> Start Block at Step: Work / retry-step
```

For a transfer that ends the source path, use [Jump Block Step](Jump-Block-Step.md).
