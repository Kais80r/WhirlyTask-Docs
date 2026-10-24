# Resetting A Variable

**Reset Variable** restores one variable to the value resolved from **Starter Variable** at the beginning of the current playback. It restores the stored Text or Math assignment mode too.

## Add The Step

1. Add **Starter Variable** and give the name an initial value.
2. Use Set Variable, Change Variable, or Read Text to change it later.
3. Add **Reset Variable** where it should return to that initial value.
4. Choose the same raw name in **Variable**.

```text
Starter Variable: attempts = 0 (Math)
Main flow:
  Change Variable: attempts / Add / 1
  Reset Variable: attempts
  Status Message: Attempts: {attempts}
```

The final message uses `0`.

## The Baseline Is A Snapshot

Suppose `base` starts at `10`, and `limit` starts with the Math expression `{base} + 1`. Playback resolves `limit` to `11` and stores that baseline. If `base` later changes to `20`, resetting `limit` restores `11`; it does not calculate `21`.

Reset requires a declared start value. A variable created only by Set Variable or Read Text has no baseline and causes an execution error when reset. Reset does not guess zero or delete the name. A Premade Block may use a baseline supplied by its calling Sequence, so the declaration does not have to be inside the saved selection.

Use [Set Variable](../Steps/Set-Variable.md) for an explicit new value, [Change Variable](../Steps/Change-Variable.md) for numeric changes, and [Reset and Restart Sequence](../Steps/Reset-And-Restart-Sequence.md) when the whole workflow must start again.
