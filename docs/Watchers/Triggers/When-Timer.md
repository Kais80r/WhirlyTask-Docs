# When Timer

Use When Timer when a watcher should fire because time has passed while the sequence is running.

Timer triggers are useful for reminders, safety limits, periodic checks, or delayed side actions that do not depend on the screen.

## Modes

| Mode | Meaning |
| --- | --- |
| after | Fire once after the sequence has been running for the chosen number of seconds |
| every | Fire repeatedly every chosen number of seconds |

Timer triggers use their own seconds field. They do not use a scan interval row.

## Good Uses

- Stop a sequence if it has been running too long.
- Send a status message every few minutes.
- Run a periodic cleanup step.
- Trigger a delayed recovery path.

## Setup Example

```text
Watcher trigger:
When Timer after 300 seconds

Watcher steps:
1. Status Message Sequence has been running for 5 minutes
```

For a repeated timer:

```text
Watcher trigger:
When Timer every 60 seconds

Watcher steps:
1. Status Message Still running
```

## Tips

- Use `after` when the watcher should run once.
- Use `every` when the watcher should keep repeating.
- Use cooldown carefully with repeating timers so the watcher does not start again before the previous watcher path is finished.
- If the timer should stop the normal workflow, put Pause Sequence near the start of the watcher steps.

## More About

- [Watcher Settings](../Watcher-Settings.md)
- [Pause Sequence](../Steps/Pause-Sequence.md)
- [Status Message](../../Steps/Status-Message.md)
