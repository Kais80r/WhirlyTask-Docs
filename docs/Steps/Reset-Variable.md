# Reset Variable

Restores one variable to the resolved value configured by **Starter Variable** at the beginning of this playback.

The only field is **Variable**. It is a literal target name; choose the same case-sensitive name used by the declaration.

```text
Starter Variable: attempts = 0 (Math)
Start -> Change Variable: attempts / Add / 1
      -> Reset Variable: attempts
      -> Status Message: Attempts: {attempts}
```

The message displays `0`. Reset restores the stored Text/Math assignment mode as well as the value.

If `total` initially used `{unitPrice} * 2`, Reset Variable restores that resolved initial total. It does not calculate a different total after `unitPrice` changes. A variable without an initial declaration causes an error; Reset does not guess zero or delete it. A declaration inherited from a calling workflow can supply the start value.

To restart the entire workflow and initialize every variable, use [Reset and Restart Sequence](Reset-And-Restart-Sequence.md). To replace a value directly, use [Set Variable](Set-Variable.md).
