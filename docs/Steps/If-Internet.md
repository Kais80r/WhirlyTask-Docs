# If Internet

Checks the app's connectivity state and branches using **Mode**: `is online` or `is offline`.

```text
If Internet: is online
  Then -> continue network-dependent work
  Else -> Status Message: Waiting for a connection
```

This is a general connection check. It does not guarantee that a particular website, account, Discord webhook, or remote service is available. Confirm service-specific results separately when necessary.

For a bounded wait, use [Wait For](Wait-For.md) with Internet. For background monitoring, use an [Internet Watcher](../Watchers/Triggers/When-Internet.md).
