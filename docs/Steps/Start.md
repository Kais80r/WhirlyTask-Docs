# Start

**Start** is an entry point for a connected execution path. Connect its output to the first action. It has no editable action settings.

A sequence can contain several Start blocks; their paths can run alongside each other. Name blocks clearly before using block controls. A Starter Variable is initialization data, not an action that needs to sit after Start.

```text
Start -> Status Message: Ready -> Wait: 1 -> Finish Sequence
```

A disconnected action is not made runnable by placing it near Start: draw the link. Use the editor's issues panel to check missing links and targets.

See [blocks](../Basics/Blocks-And-Numbering.md), [Stop Block](Stop-Block.md), and [Finish Sequence](Finish-Sequence.md).
