# What Is A Watcher Trigger?

A trigger is the condition on the first card of a Watcher chain. It decides whether that Watcher's actions should start while playback is running.

For example, a Text Watcher can check for `Disconnected` in the app's notification area. The connected action can show a message, change a variable, or run explicit recovery steps.

## Condition And Actions Are Separate

The trigger does not itself click, pause the main flow, or perform recovery. Those actions belong to its connected chain. A Watcher can run alongside main steps, and some true conditions can trigger again after cooldown.

Choose a normal If or Wait For step when checking the condition is already part of the main path. Choose a Watcher when the event can occur unexpectedly while other work continues.

## Negative Results Must Be Valid

`is not seen` means a valid scan did not find the target. It does not include capture failure, invalid query/filter settings, or an unavailable recognition engine. Use status and error information to distinguish a failed check from genuine absence.

See [All Triggers](README.md), [Watcher Settings](../Watcher-Settings.md), and [Examples](../Examples.md).
