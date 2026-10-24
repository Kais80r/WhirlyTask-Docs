# WhirlyTask Help

WhirlyTask records input and runs editable workflows with conditions, variables, screen recognition, and background Watchers.

Start with [Getting Started](Getting-Started.md), then use the topic pages for the part you are building.

![WhirlyTask workflow](assets/diagrams/whirlytask-automation-flow.svg)

## Find A Topic

| Topic | What you will learn |
| --- | --- |
| [Getting Started](Getting-Started.md) | Build and test a small workflow |
| [Basics](Basics/README.md) | Tracks, Sequences, Premade Blocks, and block targets |
| [Graph Editor](App-Features/Graph-Editor.md) | Add, select, connect, and arrange nodes |
| [Steps](Steps/README.md) | Settings and behavior of individual actions |
| [Variables](Values/README.md) | Starter values, math, references, comparisons, and Reset |
| [Watchers](Watchers/README.md) | Background triggers and deliberate recovery |
| [Recognition](Recognition/README.md) | Text, Smart image, Pixel image, and color checks |
| [Editors And Saving](App-Features/Editors-And-Saving.md) | Save, Save As, Open, Library copies and session recovery |
| [Updates](App-Features/Updates.md) | Check for an update and install when ready to restart |
| [App Features](App-Features/README.md) | Recording, playback, appearance, hotkeys, and protections |
| [Guides](Guides/README.md) | End-to-end building workflows |
| [Examples](Examples/README.md) | Small patterns to adapt |
| [Tips](Tips/README.md) | Practical habits for reliable automation |
| [Troubleshooting](Troubleshooting/README.md) | Diagnose incorrect or missing behavior |
| [Glossary](Glossary.md) | Current terms used by the app and docs |

## Common Tasks

| I want to... | Open |
| --- | --- |
| Replay recorded input | [Track](Basics/Track.md) |
| Build a connected workflow | [Sequence](Basics/Sequence.md) |
| Reuse selected nodes | [Premade Blocks](Basics/Premade-Blocks.md) |
| Select a jump or resume target | [Blocks And Step IDs](Basics/Blocks-And-Numbering.md) |
| Insert a variable without typing braces | [Using Variable References](Values/Using-Values-In-Messages.md) |
| Restore one variable's start value | [Reset Variable](Steps/Reset-Variable.md) |
| Store screen text | [Read Text](Steps/Read-Text.md) |
| Filter recognized characters | [Text Recognition](Recognition/Text.md) |
| Click the same image that was found | [Click If Image](Steps/Click-If-Image.md) |
| Click recognized text and branch on delivery | [Click If Text](Steps/Click-If-Text.md) |
| Compare an image pixel for pixel | [Pixel Recognition](Recognition/Pixel.md) |
| Check a color in an area | [If Pixel](Steps/If-Pixel.md) |
| React when a variable changes | [Variable Watcher](Watchers/Variable-Watcher.md) |
| Recover after an unexpected event | [Watcher Examples](Watchers/Examples.md) |
| Understand what closing the editor preserves | [Editors And Saving](App-Features/Editors-And-Saving.md) |
| Check for or install an app update | [Updates](App-Features/Updates.md) |

## Variables And Reusable Steps

Use **Starter Variable** to declare a start value, **Set Variable** or **Change Variable** to update it, **Reset Variable** to restore its start value, and **If Variable** to choose a branch.

Save selected nodes as a **Premade Block** when they should be reused. Clear the selection to import a saved copy. Portable Premade Block files use **.prm**.
