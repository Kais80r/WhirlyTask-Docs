# Watcher Troubleshooting

## The Watcher Never Runs

1. Confirm playback is running and has not reached Finish Sequence.
2. Select the trigger and set **Enabled** to **On**.
3. Verify its condition, screen zone, and current value or window state.
4. Check cooldown and **If another watcher is already running**.
5. Connect a simple Status Message as the first action, then test with **Play**.

Image Watcher does not have a manual scan-interval field. A large OCR or image area can take longer than a simple variable check.

## The Negative Condition Does Not Fire

`is not seen` requires a valid scan that confirms absence. Capture failures, unavailable models, invalid filters, and invalid query text are errors, not absence.

For Variable Watcher, a missing variable is not a valid ordinary comparison. Use **exists** or **does not exist** if that is the condition you need.

## The Watcher Repeats

A persistent true condition can trigger again after cooldown. Clear the underlying condition during recovery, make the trigger more specific, or increase **Cooldown seconds**. Do not use a longer cooldown to hide a wrong screen area or wrong target.

## The Main Flow Keeps Running

This is expected. A Watcher runs beside the main flow. If it must take control, use **Stop Block** with the intended main block and an explicit continuation plan. Watcher conflict settings control other Watchers only.

## Recovery Stops And Never Resumes

Find the block you stopped. Use a valid **Start Block at Step** target when recovery is complete. Selecting an unknown Step ID does not automatically choose another step. Ensure the resume point is in the intended block and has the required state.

## Actions Compete

Two Watchers running alongside one another can both move the mouse, change focus, or write variables. Choose a suitable conflict policy and keep action chains short. A Watcher cannot use a Step ID jump into a different Watcher's chain.

See [Watcher Settings](Watcher-Settings.md), [Controlling Main Blocks](Steps/Controlling-Main-Blocks.md), and [Recognition](../Recognition/README.md).
