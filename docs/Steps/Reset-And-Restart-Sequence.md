# Reset and Restart Sequence

Ends the current run and starts the sequence again from its entry points, with runtime variables initialized again from Starter Variables. It has no action settings.

Use it for an intentional whole-workflow restart. Existing variable values and counters are not retained as a retry history across this restart. A counter used to enforce a run limit should therefore loop within the same playback instead.

```text
recover application state -> Reset and Restart Sequence
```

A restart does not undo application actions already performed, remove files, or reset the external application by itself. Add the required recovery actions before it.

For a retry that retains counters, use [Jump Block Step](Jump-Block-Step.md). To restore only one initial variable, use [Reset Variable](Reset-Variable.md).
