# App Features

These pages cover WhirlyTask's editor, Library, recording, playback, appearance, and app-wide protections. Use the [step reference](../Steps/README.md) for actions inside a workflow.

| I want to... | Open |
| --- | --- |
| Add, connect, select, and arrange graph nodes | [Graph Editor](Graph-Editor.md) |
| Save files, keep Library copies and recover editing work | [Editors And Saving](Editors-And-Saving.md) |
| Manage named items or portable files | [Library And Files](Library-And-Files.md) |
| Switch between dark and light themes | [Appearance](Appearance.md) |
| Change record, play, stop, or emergency hotkeys | [Hotkeys](Hotkeys.md) |
| Choose which input a Track records | [Recording Options](Recording-Options.md) |
| Change playback speed or looping | [Playback, Speed, And Loop](Playback-Speed-And-Loop.md) |
| Stop playback when a configured app closes | [Crash Protection](Crash-Protection.md) |
| Stop playback when configured text appears | [Text Protection](Text-Protection.md) |
| Configure Discord output | [Discord Webhook](Discord-Webhook.md) |
| Save diagnostic OCR captures while testing | [OCR Debug Captures](OCR-Debug-Captures.md) |
| Keep the app visible or open documentation | [Always On Top And Help](Always-On-Top-And-Help.md) |

## Protection Or Watcher?

Crash Protection and Text Protection are app-wide stop mechanisms. A Watcher is part of a Sequence and can run an action chain when its trigger is valid.

Use a protection when the desired response is to stop playback. Use a [Watcher](../Watchers/README.md) when the workflow needs custom notification, variable updates, or deliberate recovery. A Watcher does not automatically pause main actions.

## Saving Your Work

Use **Save** or **Ctrl+S** to update the open file or Library entry. A new document asks for a file name and location. **Save As** writes another file. **More > Add to Library** creates a separate named copy.

Unfinished documents can be saved. Fix Editor Issues before playback. Automatic recovery retains editing work across restart. Read [Editors And Saving](Editors-And-Saving.md) for Save, Open and unsaved-change choices.

For a first workflow, start with [Getting Started](../Getting-Started.md). For screen checks, use [Recognition](../Recognition/README.md).
