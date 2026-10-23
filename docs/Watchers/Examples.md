# Watcher Examples

Use these as small patterns to test. They are not complete recovery systems for every app.

## Notify When Text Appears

```text
Text Watcher:
  Text: Disconnected
  Mode: is seen
  Screen zone: the app's notification area
  Cooldown seconds: 30
Actions:
  Status Message: Connection warning detected
```

The main flow keeps running. If the warning stays visible, another trigger is possible after cooldown. Use [Text Recognition](../Recognition/Text.md) to choose a suitable area and filter.

## React To A Variable

```text
Starter Variable: attempts = 0 (Math)
Variable Watcher:
  Variable: attempts
  Mode: >=
  Compare to: 3
Actions:
  Stop Block: Main
```

Name your actual main block `Main`, or select its real name. Missing variables are not valid numeric comparison results. A Starter declaration ensures the counter exists before it is checked.

## Check An Image

Use **Image Watcher**, choose or paste the image, and select **Smart** or **Pixel** recognition. Smart allows some visual variation; Pixel compares the original image size with the configured per-channel tolerance. Add a Status Message first, before adding a mouse action.

If the accepted image itself must be clicked, use **If Image Click** in the action chain rather than assuming a previous Watcher detection is still a safe click location.

## Take Control Deliberately

A recovery chain may use:

```text
Watcher condition
  Stop Block: Main
  Focus Window: target app
  recovery actions
  Start Block at Step: Main / selected Step ID
```

Choose a valid resume point whose preconditions recovery establishes. A Watcher does not pause the main flow automatically, and stopping a block does not itself restart it.

See [Controlling Main Blocks](Steps/Controlling-Main-Blocks.md), [Start Block at Step](../Steps/Start-Block-at-Step.md), and [Watcher Recovery](../Guides/Watcher-Recovery-Workflow.md).
