# App Features

These pages cover WhirlyTask's editor, Library, recording, playback, appearance, and app-wide protections. Use the [step reference](../Steps/README.md) for actions inside a workflow.

| I want to... | Open |
| --- | --- |
| Add, connect, select, and arrange graph nodes | [Graph Editor](Graph-Editor.md) |
| Understand playable drafts, named saves, and session recovery | [Editors And Saving](Editors-And-Saving.md) |
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

## Saving Has Separate Layers

The graph editor's **Save Draft** applies the playable draft. **Save New** creates a named Library copy. Automatic session recovery preserves editing work separately, including invalid work that cannot yet be applied. Portable files are explicit copies for backup or transfer.

Validation errors block applying or saving the graph through Save Draft, Save New, and Save As. Warnings remain visible but do not block those actions. Read [Editors And Saving](Editors-And-Saving.md) for the distinction between recovery, playback, and a saved backup.

For a first workflow, start with [Getting Started](../Getting-Started.md). For screen checks, use [Recognition](../Recognition/README.md).
