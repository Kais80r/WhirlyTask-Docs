# Watcher recovery example

Recover one error while keeping retries explicit and bounded.

Declare `recoveries = 0` as a Math Starter Variable. Name the main block `Work` and give its safe retry entry a Step ID such as `retry-step`.

```text
Text Watcher: Connection lost / is seen
  -> Stop Block: Work
  -> Change Variable: recoveries / Add / 1
  -> If Variable: recoveries > 3
       Then -> Status Message: Recovery limit reached -> Finish Sequence
       Else -> recovery actions
            -> If Text: Connection lost / is not seen
                 Then -> Start Block at Step: Work / retry-step
                 Else -> Status Message: Error remains -> Finish Sequence
```

Use a relevant selected area for the watcher and the final check. Configure a cooldown and conflict behavior that prevent overlapping recovery input. The counter is shared across blocks and watchers during this playback.

Recovery actions depend on the target application: they might close a dialog and wait for reconnection. Test them with a harmless case first. Before restarting at `retry-step`, determine whether a previously completed external action could be repeated.

Stop Block is an explicit stop, not a resumable pause. The chosen Step ID determines where work starts again. Let the watcher path end when done; Finish Sequence is for ending all playback.

See [Watcher Recovery Workflow](../Guides/Watcher-Recovery-Workflow.md) and [watchers](../Watchers/README.md).
