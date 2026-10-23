# Time Watcher

Time Watcher schedules a daily trigger at a wall-clock time. Use Timer Watcher instead for a duration measured from playback startup.

## Fields

| Field | Meaning |
| --- | --- |
| Time | Clock time in HH:mm format |
| Time zone | Automatic computer time zone, UTC, or a supported fixed UTC offset |

The shared Enabled, Cooldown seconds, and conflict fields follow the schedule.

Choose Automatic when the event should follow the computer's local clock. A fixed UTC offset does not automatically change for daylight saving time. The schedule is checked only while the Sequence is running; closing or finishing playback does not leave an independent scheduled job behind.

Time Watcher records the daily trigger so the same scheduled occurrence does not run continuously during its matching minute. It is not Timer Watcher's after/every duration control.

See [Timer Watcher](When-Timer.md) and [Watcher Settings](../Watcher-Settings.md).
