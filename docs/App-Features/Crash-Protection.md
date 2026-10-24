# Crash Protection

Crash Protection stops playback when the selected application's process is no longer running. Choose its target from **Menu > Crash Protection** while the application is open.

The menu also offers Off and a separate Discord Message alert toggle.

## What It Watches

WhirlyTask stores the selected running process as the target. It does not prove that the application is responsive, ready for input, or focused. Closing one window may leave the same process running, so use a [Window condition or watcher](../Watchers/Triggers/When-Window.md) when a particular window state matters.

After restarting an application, reselect its process if necessary. Avoid selecting a short-lived launcher or temporary dialog process.

## Test It

1. Choose the intended application in Crash Protection.
2. Start a short harmless playback.
3. Verify the protection target is the process you intended.
4. Turn protection Off for workflows that deliberately terminate that process.

For an alert, first configure [Discord Webhook](Discord-Webhook.md), then enable Discord Message in the Crash Protection submenu. Protection alerts and ordinary Discord Message steps are separate settings.

Use a sequence watcher when you need recovery steps, a notification, or a conditional continuation instead of a global stop.
