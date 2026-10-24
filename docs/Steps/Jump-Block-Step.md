# Jump Block Step

Transfers execution to a particular step in a selected block. The source block stops following its current path.

| Field | Meaning |
| --- | --- |
| Block | Destination block |
| Step ID | Destination chosen from the available step IDs |

Use the Step ID selector rather than counting cards by their position on the canvas. Stable IDs identify actions after layout changes; displayed order is not a substitute for an execution link.

```text
Work: Start -> do one attempt -> If Variable: attempts < 3
  Then -> Jump Block Step: Work / attempt-start
  Else -> Finish Sequence
```

Include a Wait or a real bounded action in loops so they do not spin continuously. Validate that the target still exists after deleting or moving steps.

Use [Start Block at Step](Start-Block-at-Step.md) to start a destination alongside the current path. Use [If Block Running](If-Block-Running.md) before starting work that should not run twice.
