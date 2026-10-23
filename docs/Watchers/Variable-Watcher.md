# Variable Watcher

Variable Watcher checks a variable while a Sequence runs. Add it from either **Watcher** or **Variable** in the toolbox, then connect the actions that should run when the condition is valid.

## Configure The Condition

| Field | Meaning |
| --- | --- |
| Variable | Raw case-sensitive name, such as attempts |
| Mode | changed, equals, not equals, contains, is empty, is not empty, exists, does not exist, >, >=, <, <= |
| Compare to | Shown only for modes that need a comparison value |

Use **Enabled**, **Cooldown seconds**, and **If another watcher is already running** to control execution. There is no manual Check every seconds field for Variable Watcher.

The target name does not interpolate. Use `attempts` to check that variable; use `{limit}` in a supported Compare to field when the comparison should read another value.

## Missing Is Different From Empty

**exists** and **does not exist** intentionally check whether the name is present. **is empty** checks an existing value's empty or whitespace state. Ordinary comparisons against a missing name fail safely instead of firing the Watcher.

An existing value containing unresolved or cyclic references is not a valid ordinary comparison either. Use Starter Variable to initialize expected names, and use existence modes when the absence of a name is intentional.

Text comparisons ignore letter case, but name lookup does not. Numeric comparisons require valid finite numbers. **changed** reacts to changes; other active conditions can repeat after cooldown while they remain true.

## Example: Retry Limit

```text
Starter Variable: attempts = 0 (Math)
Main actions increment attempts with Change Variable.

Variable Watcher:
  Variable: attempts
  Mode: >=
  Compare to: 3
Actions:
  Stop Block: Main
```

Select the actual main block rather than leaving a placeholder target. The Watcher conflict policy controls other Watchers; it does not automatically stop main actions.

See [Variables](../Values/README.md), [If Variable](../Steps/If-Variable.md), [Watcher Settings](Watcher-Settings.md), and [Controlling Main Blocks](Steps/Pause-Sequence.md).
