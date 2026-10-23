# Recover with a watcher

A watcher monitors a trigger while the sequence runs. Its action path should leave the application in a known state and make continuation explicit.

## Choose one trigger

Use a distinctive text/image/window signal. Limit visual recognition to the relevant area. Configure Enabled, Cooldown, and the conflict behavior intentionally; do not assume the same watcher can safely start repeated input paths at once.

## Stop the affected block

Name the main work block `Work`. Give its safe retry action a stable Step ID such as `retry-step`. When an error watcher triggers, use **Stop Block: Work** before performing recovery input.

Stop Block does not remember a resumable pause position. **Start Block at Step** starts at the target you choose; **Jump Block Step** transfers execution and ends the source path.

## Verify recovery before restarting

```text
Text Watcher: Connection lost
  -> Stop Block: Work
  -> recovery actions
  -> If Text: Connection lost / is not seen
       Then -> If Block Running: Work
                   Then -> end this watcher path
                   Else -> Start Block at Step: Work / retry-step
       Else -> Status Message: Recovery failed -> Finish Sequence
```

End the watcher action path normally when it has nothing else to do. Do not add Finish Sequence merely to return from a watcher: it ends playback.

A negative text/image check is usable only when recognition completed validly. Errors are not proof that the problem disappeared. Bound recovery attempts with a shared counter and consider whether retrying an application action could duplicate external work.

See [watcher settings](../Watchers/Watcher-Settings.md), [Watcher Recovery example](../Examples/Watcher-Recovery.md), and [Counter Limit](../Examples/Counter-Limit.md).
