# For Chance

Performs a chance-based branch when this node executes. Set **Chance percent**, then connect **Then** for a successful roll and **Else** otherwise.

At `0`, Then is never selected. At `100`, Then is always selected. A value such as `25` describes a chance per evaluation, not a promise that every fourth execution will choose Then.

```text
For Chance: 25
  Then -> Status Message: Extra check selected
  Else -> continue normal work
```

This is not a repeat counter or a reliability check. Use [If Variable](If-Variable.md) for a deterministic limit. Use a [Chance Watcher](../Watchers/Triggers/For-Chance.md) for periodic background rolls.
