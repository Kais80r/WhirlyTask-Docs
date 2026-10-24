# Internet Watcher

Internet Watcher checks the computer's online or offline state while Sequence playback is running.

| Field | Choices or meaning |
| --- | --- |
| Mode | is online or is offline |
| Check every seconds | Requested interval between checks |

Set the shared Enabled, Cooldown seconds, and conflict fields afterward.

An online result does not prove a particular website, game server, or request is working. Use an app-specific text, image, or variable condition when that is what the workflow needs to know.

The condition can remain true and trigger again after cooldown. Start with a Status Message before adding actions that stop blocks or change app state.

See [Watcher Settings](../Watcher-Settings.md) and [Watcher Examples](../Examples.md).
