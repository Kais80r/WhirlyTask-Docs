# Clock Time

Clock Time triggers at a chosen clock time each day. Use Timer / Interval for a duration measured from playback startup.

## Fields

| Field | Meaning |
| --- | --- |
| Time | Clock time in HH:mm format |
| Time zone | Automatic computer time zone, UTC, or a supported fixed UTC offset |

The shared Enabled, Cooldown seconds, and conflict fields follow the schedule.

Choose Automatic when the event should follow the computer's local clock. A fixed UTC offset does not automatically change for daylight saving time. The schedule is checked only while the Sequence is running; closing or finishing playback does not leave an independent scheduled job behind.

Clock Time records the daily trigger so the same scheduled occurrence does not run continuously during its matching minute.

See [Timer / Interval](Timer-Interval.md) and [Watcher Settings](../Watcher-Settings.md).
