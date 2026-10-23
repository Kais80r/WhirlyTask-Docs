# Keeping Watchers Predictable

Give each watcher one clear job, such as handling one warning or reporting one state change. Keep normal workflow steps in the main path.

## Trigger, Interval, And Cooldown

The scan interval controls when eligible checks are scheduled. Cooldown limits repeated activation after a trigger. Lowering cooldown does not make a slow OCR request finish sooner, and a very short interval is not a guarantee of instant detection.

For text/image checks, choose a useful area and test a visible positive plus a known negative. Unavailable recognition must not satisfy an is not seen trigger.

## Decide Who Owns Input

A watcher can run alongside the main sequence. If its recovery steps must take over, use Stop Block on the intended work block before sending competing clicks or keys.

Stop Block does not preserve a resumable pause position. Use Start Block at Step with an explicit target to start work again, Jump Block Step to transfer the current path, Reset and Restart Sequence for a fresh run, or Finish Sequence to end playback.

Start testing with `Status Message: Watcher fired`. Once the trigger is proven, test the stop/restart behavior and check that recovery cannot duplicate an already completed external action. Use cooldowns for repeated notifications.

See [Watchers](../Watchers/README.md), [Watcher Does Not Fire](../Troubleshooting/Watcher-Does-Not-Fire.md), and [Watcher Recovery Does Not Resume The Main Block](../Troubleshooting/Watcher-Recovery-Does-Not-Resume.md).
