# Messages and variables

Declare variables for the state you need, update them deliberately, and report them at meaningful points.

```text
Starter Variable: completed = 0 (Math)
Start -> do one item
      -> Change Variable: completed / Add / 1
      -> Status Message: Completed {completed} item(s)
      -> Finish Sequence
```

Use Set Variable with Text for labels and Math for calculations. Text can be explicitly empty; it does not keep a stale earlier value. Change Variable requires a numeric current value for Add/Subtract and fails instead of treating invalid text as zero.

Variable names are case-sensitive. `{completed}` uses that exact variable; `{Completed}` is a different name. Use the variable picker/suggestions in fields that support insertion. Display metadata, target variable names, and block/Step ID selectors are not arbitrary expression fields.

Status messages help locate branches but are transient: a later runtime message can replace them. A message that says an action started is not proof it succeeded. Put completion messages after a meaningful confirmation check.

For Discord output, configure a webhook first and decide which variable contents should leave the computer. Keep a short local status message while debugging.

See [Set Variable](../Steps/Set-Variable.md), [Status Message](../Steps/Status-Message.md), [Discord Message](../Steps/Discord-Message.md), and [variables](../Values/README.md).
