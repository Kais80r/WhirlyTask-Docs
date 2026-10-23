# Glossary

These terms describe the controls and behavior in WhirlyTask.

## Workflows And Editor

| Term | Meaning |
| --- | --- |
| Track | Recorded keyboard and mouse input that can be replayed |
| Sequence | Editable workflow of connected actions, decisions, blocks, variables, and optional Watchers |
| Premade Block | Saved selection of graph nodes imported later as a reusable copy; portable files use .prm |
| Node / step | A card in the graph representing an action, condition, declaration, or trigger |
| Connection | Link that determines where execution continues |
| Block | Named main-flow section that can be targeted by block-control steps |
| Step ID | An addressable target within a block; it is not a visual execution-order number |
| Then / Else | The paths selected by a valid conditional result |
| Auto Layout | Reposition graph nodes to make connections easier to follow |
| Inspector / settings panel | Right-hand settings for the selected step, Watcher, or editable block; hidden without a selection |

## Variables

| Term | Meaning |
| --- | --- |
| Variable / value | Named data stored during playback |
| Raw name | A target name such as attempts, entered without reference braces |
| Reference | A token such as {attempts} that resolves in a supported input field |
| Starter Variable | Declaration initialized before normal playback actions |
| Set Variable | Store or calculate a replacement value; empty Text clears it |
| Change Variable | Add, subtract, or set a numeric value |
| Reset Variable | Restore one declared variable's resolved startup snapshot and assignment mode |
| Text / Math | Treat an assignment as substituted text or as a calculated expression |
| Variables used | Configured names, sources, and uses in the graph; not a live runtime monitor |
| Insert / Replace | Explicitly insert a chosen reference at the cursor, or replace the whole field |
| Exists | The name has been created; different from whether its value is empty |

Variable names are case-sensitive. A missing name is not an empty string for ordinary comparisons. See [Variables](Values/README.md).

## Recognition

| Term | Meaning |
| --- | --- |
| OCR / text recognition | Read letters and numbers from captured screen pixels |
| Screen zone | Full Screen or a selected area used by a screen-based action |
| Read Text | Store recognized text in a result variable |
| Read as | Filter the output produced by Read Text |
| Match characters | Filter recognized candidates for text finding; the query must already fit the filter |
| Smart image recognition | Learned matching that tolerates some visual differences |
| Pixel image recognition | Compare a reference image at its original size with a per-channel RGB tolerance |
| If Pixel | Check for a chosen color anywhere in a screen area; distinct from Pixel image matching |
| If Image Click | Find and click the same accepted image target; Then requires a delivered click |
| Confirmed absence | A valid scan did not find the target; an error is not absence |

See [Recognition](Recognition/README.md) for supported filters, capture limits, and matching behavior.

## Watchers And Control

| Term | Meaning |
| --- | --- |
| Watcher | A trigger and action chain checked alongside the normal workflow |
| Clock Time | Watcher that runs at a chosen daily clock time and time zone |
| Timer / Interval | Watcher that runs once after a delay or repeats at an elapsed-time interval |
| Trigger | Condition that makes a Watcher eligible to run |
| Cooldown | Minimum wait before that Watcher may trigger again |
| Watcher conflict policy | What to do when another Watcher is active; it does not pause main blocks |
| Stop Block | Stop the selected main block |
| Start Block at Step | Start a selected block at a chosen Step ID |
| Jump Block Step | Redirect to an explicit block/step target |
| Reset and Restart Sequence | Begin the workflow again with startup initialization |
| Finish Sequence | End Sequence playback, including its Watchers |

A Watcher does not automatically stop or pause the main flow. See [Watchers](Watchers/README.md).

## Saving And App Features

| Term | Meaning |
| --- | --- |
| Save | Update the open file or Library entry; choose a file location for a new document |
| Save As | Write a different file and continue editing it |
| Add to Library | Create a separate named Library copy of the open workflow |
| Session recovery | Automatically preserve editing work and UI state separately from playable and named copies |
| Library | Named saved Tracks, Sequences, and Premade Blocks |
| File copy | Portable copy saved with explicit Library/file actions |
| Status Message | Message shown inside WhirlyTask |
| Discord webhook | URL used by Discord Message to post to a channel |
| Crash Protection | Stop playback when a configured app or window closes |
| Text Protection | Stop playback when configured text is detected |
| Emergency Stop | Configured hotkey used to stop playback |

See [Editors And Saving](App-Features/Editors-And-Saving.md), [Library And Files](App-Features/Library-And-Files.md), and [App Features](App-Features/README.md).
