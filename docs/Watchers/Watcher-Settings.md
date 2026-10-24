# Watcher Settings

Select a Watcher trigger card to show its condition and run settings. No selection means the settings panel is hidden.

## Shared Run Settings

| Field | Meaning |
| --- | --- |
| Enabled | On or Off for this Watcher |
| Cooldown seconds | Minimum wait before the Watcher can trigger again |
| If another watcher is already running | Choose what to do when a different Watcher is active |

The conflict dropdown has these choices:

| Choice | Behavior |
| --- | --- |
| Don't run this watcher | Leave the other Watcher running and do not start this one in the conflict |
| Take over other watcher | Stop the active Watcher and run this one |
| Run alongside other watcher | Allow the Watcher chains to run concurrently |

These choices concern other Watchers, not the normal main flow. Concurrent actions can still compete for the mouse, keyboard, window focus, or variables.

## Check Rate Is Trigger-Specific

| Watcher | Timing field |
| --- | --- |
| Text, Window, Internet | Check every seconds |
| Chance | Roll every seconds |
| Timer / Interval | Trigger after/every, then Seconds |
| Clock Time | Time and Time zone |
| Image | Automatic scan scheduling; no manual interval field |
| Variable | No manual interval field |

A configured check interval is not a guarantee of recognition latency. Capturing and recognizing a large area can take time. Choose the smallest useful screen zone and measure the workflow on the machine that runs it.

## Cooldown Is Not A One-Shot Switch

Text, Image, Window, Internet, and ordinary Variable conditions may trigger again while the condition remains active after cooldown. Variable changed mode reacts to changes; Clock Time triggers at its chosen clock time; Timer / Interval uses its after or every elapsed-time behavior.

For a persistent warning, make the action chain clear the warning or use a suitably long cooldown. If repeated messages appear, inspect the condition before shortening the scan interval.

See [Triggers](Triggers/README.md), [Examples](Examples.md), and [Keeping Watchers Predictable](../Tips/Keeping-Watchers-Predictable.md).
