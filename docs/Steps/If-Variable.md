# If Variable

Checks a runtime variable and follows **Then** when the condition matches or **Else** when a valid check does not match.

| Field | Meaning |
| --- | --- |
| Variable | Target name |
| Mode | Comparison to perform |
| Compare to | Right-hand value, shown only for modes that need one |

Modes are `equals`, `not equals`, `contains`, `is empty`, `is not empty`, `exists`, `does not exist`, `>`, `>=`, `<`, and `<=`.

Text equality and contains comparisons ignore case. Numeric comparisons require finite numbers. Empty checks treat whitespace-only contents as empty. An existing empty variable differs from a missing variable: `exists` is true for the former.

Ordinary comparisons require the variable and its references to exist. Missing or cyclic references and invalid numeric comparisons are errors; they do not authorize either branch. Use **exists** or **does not exist** when checking presence deliberately.

```text
If Variable: attempts >= 3
  Then -> Status Message: Limit reached -> Finish Sequence
  Else -> the next attempt
```

See [Counter Limit](../Examples/Counter-Limit.md) and [Variable Watcher](../Watchers/Variable-Watcher.md).
