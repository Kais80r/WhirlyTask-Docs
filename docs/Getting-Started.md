# Getting Started

Start with one short working path, then add decisions and background recovery as the workflow needs them.

## Choose Your Starting Point

| Need | Start here |
| --- | --- |
| Replay a fixed keyboard or mouse action | [Record a Track](Basics/Track.md) |
| Wait, branch, recognize the screen, or use variables | [Build a Sequence](Basics/Sequence.md) |
| Reuse a working group of nodes | [Save a Premade Block](Basics/Premade-Blocks.md) |
| React to an unexpected event during playback | [Add a Watcher](Watchers/README.md) |

## Build A Small Sequence

1. Put the target app into the state the automation expects.
2. Open **Sequence Editor...** from WhirlyTask's main window.
3. Find actions in the toolbox's **All** or **Basic** tab and build a short connected path from Start.
4. Select each node to edit its settings. The right-hand settings panel hides when nothing is selected.
5. Add an appropriate readiness check before the next action. Prefer Wait For when you need a condition, rather than guessing a long fixed delay.
6. Click **Save Draft** to validate and apply the graph for playback.
7. Run that short workflow once and verify its effect before extending it.

Connections determine order. An If node has Then and Else paths; arrange and connect both deliberately. [Blocks And Step IDs](Basics/Blocks-And-Numbering.md) explains named blocks and targeted jumps.

## Remember And Reuse Information

Open the **Variable** toolbox tab. Add a Starter Variable such as `attempts` with a starting value of `0`, or an empty Text value such as `resultText`.

Use the raw name in **Variable** or **Result variable** fields. Use `{resultText}` in supported text fields to read the value. The insertion tools let you choose a name, then explicitly click **Insert** at the cursor or **Replace** for the whole field. Browsing the dropdown alone does not edit the field.

The Variables used overview shows configured sources, not live runtime values. See [Variables](Values/README.md) for setting, comparing, clearing, and resetting values.

## Choose Recognition Deliberately

| Situation | Useful step or setting |
| --- | --- |
| Wait for a visible phrase | [Wait For, Text](Steps/Wait-For.md) |
| Store text from an area | [Read Text](Steps/Read-Text.md) |
| Click a recognized word | [Click Text](Steps/Click-Text.md) |
| Click an image and branch after the click | [If Image Click](Steps/If-Image-Click.md) |
| Recognize a visual target with some variation | Smart image recognition |
| Compare an image at its original size | Pixel image recognition |
| Check a color anywhere in an area | [If Pixel](Steps/If-Pixel.md) |

Use a small screen zone that includes the target with padding. Test an absent target and a similar wrong target too. A failed capture or recognition error is not a confirmed negative result. See [Recognition](Recognition/README.md).

## Add A Watcher For Side Events

Use **Watcher** for events that may occur while normal steps are running. Add a trigger, configure it, then connect ordinary actions from the other tabs. Variable Watcher is also available in Variable.

A Watcher does not automatically pause main steps. If recovery must take control, explicitly stop the affected block and plan how to resume it. Start with a simple notification while testing, and choose a cooldown suitable for conditions that can stay true.

See [Watcher Settings](Watchers/Watcher-Settings.md) and [Examples](Watchers/Examples.md).

## Save The Right Copy

**Save Draft** applies the playable draft. **Save New** creates a named Library copy. Automatic session recovery separately preserves editing work when closing or reopening; recovered work may not yet be the version applied for playback or saved under a Library name.

For a reusable selection, hold Shift and drag over its nodes. The top button becomes **Save Premade Block**. After saving, clear the selection to use **Import Premade Block** again. Premade files use **.prm**.

Read [Editors And Saving](App-Features/Editors-And-Saving.md) and [Library And Files](App-Features/Library-And-Files.md) before relying on a saved copy as a backup.

## Continue Learning

- [Step reference](Steps/README.md)
- [Guides](Guides/README.md)
- [Examples](Examples/README.md)
- [Troubleshooting](Troubleshooting/README.md)
- [Glossary](Glossary.md)
