# Set Variable

Creates or replaces a runtime variable when this step executes.

| Field | Meaning |
| --- | --- |
| Variable | Target name |
| Set to | Text or expression to assign |
| Interpret as | **Text** or **Math** |

**Text** resolves supported `{name}` references and stores the resulting text without calculating arithmetic. Assigning `1 + 2` as Text stores `1 + 2`, even if this variable previously used Math. An empty value clears its contents while keeping the variable present. Intentional whitespace is retained.

**Math** calculates a finite numeric result. For example, `{price} * {quantity}` requires both referenced variables to exist. Invalid expressions and missing references stop the action rather than silently substituting zero.

A variable created only by Set Variable has no declared initial value for [Reset Variable](Reset-Variable.md). Add a [Starter Variable](Starter-Variable.md) if reset behavior is needed.

```text
Start -> Set Variable: label = Finished (Text)
      -> Status Message: State: {label} -> Finish Sequence
```

See [Change Variable](Change-Variable.md) and [If Variable](If-Variable.md).
