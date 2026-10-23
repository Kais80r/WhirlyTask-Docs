# Step reference

These are the current graph editor's toolbox entries. Select a node to edit its fields in the inspector, and draw links to determine execution. Canvas position and displayed numbers do not replace links or stable Step ID targets.

Start with [Getting Started](../Getting-Started.md) or [Build a reliable sequence](../Guides/Build-A-Reliable-Sequence.md). For the distinction between recordings, sequences, and templates, see [Basics](../Basics/README.md).

## Flow Control

| Step | Purpose |
| --- | --- |
| [Start](Start.md) | Entry point for a connected path |
| [Stop Block](Stop-Block.md) | Stop one named block |
| [Jump Block Step](Jump-Block-Step.md) | Transfer execution to a stable target and end the source path |
| [Start Block at Step](Start-Block-at-Step.md) | Start another block at a stable target alongside current work |
| [Finish Sequence](Finish-Sequence.md) | End playback |
| [Reset and Restart Sequence](Reset-And-Restart-Sequence.md) | Begin a new run and initialize variables again |

## Tracks

| Step | Purpose |
| --- | --- |
| [Play Track](Play-Track.md) | Replay a saved input recording |

To reuse graph nodes, [save a selection as a premade block](../Guides/Reusable-Premade-Blocks.md) and import a copy from the Library. Templates use `.prm` files. There is no separate Premade Block Editor or current Run Premade Block toolbox card.

## Timing

| Step | Purpose |
| --- | --- |
| [Wait](Wait.md) | Fixed delay |
| [Random Wait](Random-Wait.md) | Delay between configured bounds |
| [Wait For](Wait-For.md) | Wait for a condition or timeout; either outcome continues |

## Input

| Step | Purpose |
| --- | --- |
| [Click Image](Click-Image.md) | Recognize an image and attempt a guarded click |
| [Click Text](Click-Text.md) | Find known text and attempt a guarded click |
| [Press Key](Press-Key.md) | Press/release a supported key |
| [Set Cursor Position](Set-Cursor-Position.md) | Move to a desktop point |
| [Press Mouse Button](Press-Mouse-Button.md) | Press/release at the current cursor position |
| [Scroll Wheel](Scroll-Wheel.md) | Scroll in a direction for a duration |

## Logic

| Step | Purpose |
| --- | --- |
| [If Text](If-Text.md) | Branch on recognized known text |
| [If Image](If-Image.md) | Branch on a Smart or literal Pixel template match |
| [If Image Click](If-Image-Click.md) | Then only after successful guarded click delivery |
| [If Pixel](If-Pixel.md) | Find at least one pixel of a selected color in an area |
| [If Window](If-Window.md) | Check open/focused/fullscreen state |
| [If Internet](If-Internet.md) | Check connectivity state |
| [If Block Running](If-Block-Running.md) | Check whether a named block is executing |
| [For Chance](For-Chance.md) | Chance-based Then/Else branch |

Text/image recognition can be unavailable. That is not evidence that a target is absent. See [Recognition](../Recognition/README.md) for filters, matching modes, precision limits, and fresh-click checks.

## Variables

| Step | Purpose |
| --- | --- |
| [Starter Variable](Starter-Variable.md) | Declare a value before playback |
| [Set Variable](Set-Variable.md) | Assign Text or calculated Math |
| [Change Variable](Change-Variable.md) | Add, subtract, or set a finite number |
| [Reset Variable](Reset-Variable.md) | Restore one resolved initial value |
| [If Variable](If-Variable.md) | Compare a valid value or check explicit presence |

Variables use case-sensitive names and `{name}` substitution in supported fields. [Variable Watcher](../Watchers/Variable-Watcher.md) is also available in the variable-related toolbox view. See [Variables](../Values/README.md).

## System

| Step | Purpose |
| --- | --- |
| [Read Text](Read-Text.md) | Read a screen region into a variable |
| [Take Screenshot](Take-Screenshot.md) | Save a timestamped BMP of a screen region |
| [Focus Window](Focus-Window.md) | Restore/activate a matching window |
| [Fullscreen Window](Fullscreen-Window.md) | Maximize a matching window |
| [Set Clipboard](Set-Clipboard.md) | Put text on the clipboard |
| [Open App/File](Open-App-File.md) | Open a target with Windows |
| [Open Link](Open-Link.md) | Open a URL with its default handler |
| [Close Window/App](Close-Window-App.md) | Request normal closing of a matching window |

## Output

| Step | Purpose |
| --- | --- |
| [Discord Message](Discord-Message.md) | Send configured webhook output |
| [Status Message](Status-Message.md) | Report transient local progress |
| [Note](Note.md) | Explain assumptions in the editor |

## Watchers

Watchers have trigger settings and their own action paths. They are covered in the [Watcher reference](../Watchers/README.md).

| Toolbox entry | Reference |
| --- | --- |
| Text Watcher | [Text trigger](../Watchers/Triggers/When-Text.md) |
| Image Watcher | [Image trigger](../Watchers/Triggers/When-Image.md) |
| Window Watcher | [Window trigger](../Watchers/Triggers/When-Window.md) |
| Variable Watcher | [Variable trigger](../Watchers/Variable-Watcher.md) |
| Time Watcher | [Clock-time trigger](../Watchers/Triggers/When-Time.md) |
| Timer Watcher | [Elapsed timer trigger](../Watchers/Triggers/When-Timer.md) |
| Chance Watcher | [Chance trigger](../Watchers/Triggers/For-Chance.md) |
| Internet Watcher | [Internet trigger](../Watchers/Triggers/When-Internet.md) |

## Older documentation links

Old Sequence Value names now point to the canonical Variable pages. Older Pause/Stop Sequence, numbered jumps, Return to Sequence, Repeat X Times, and Run Advanced Track pages remain as compatibility explanations; they are not additional current toolbox cards.

For complete connected patterns, see [Examples](../Examples/README.md). For draft recovery versus named saves and files, see [Editors and saving](../App-Features/Editors-And-Saving.md).
