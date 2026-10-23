# Timer / Interval

Timer / Interval triggers from elapsed time during Sequence playback.

| Field | Choices or meaning |
| --- | --- |
| Trigger | after or every |
| Seconds | The elapsed duration |

Set the shared [Enabled, cooldown, and conflict settings](../Watcher-Settings.md) as well.

**after** is a one-shot trigger measured from the start of playback. **every** repeats, measuring the next interval from the previous trigger, or from playback startup before the first trigger.

For example, every / 60 with a Status Message action provides a periodic reminder while the main workflow is still running. Cooldown and other active Watchers can affect whether an eligible trigger starts; this is not a hard real-time scheduler.

Use [Clock Time](Clock-Time.md) for a particular daily clock time, and [Wait](../../Steps/Wait.md) when the main path itself should wait before its next action.
