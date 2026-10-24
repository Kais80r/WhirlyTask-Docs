# Watcher Does Not Fire

Put `Status Message: Watcher fired` as the first watcher step. If it appears, the trigger worked and the failure is later in its actions.

## Trigger Checklist

- The intended sequence is running and the watcher is On.
- The trigger can become true in the selected area/window/time context.
- Its scan interval allows a check and its cooldown has expired.
- Required variables exist with the exact case-sensitive names.
- The text/image reference and recognition mode are correct.
- For text filters, the query already fits Match characters and Custom chars is nonempty.

A background OCR request can take longer than the scan interval. Lowering cooldown does not speed up recognition. Invalid capture or unavailable recognition does not count as image/text absence and must not activate is not seen.

For a Variable Watcher, distinguish a presence/content comparison from **changed**. Changed reacts to a value-change signal during playback; an initial configured value alone is not the same event. Resetting to the same content need not produce a change.

Test one watcher at a time with its exact positive and negative states. Print relevant variables using Status Message.

See [Watchers](../Watchers/README.md), [Triggers](../Watchers/Triggers/README.md), and [Keeping Watchers Predictable](../Tips/Keeping-Watchers-Predictable.md).
