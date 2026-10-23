# Set Clipboard

Places **Message** text on the Windows clipboard. Supported `{name}` references are replaced with runtime variable values.

```text
Starter Variable: reportName = Daily report (Text)
Start -> Set Clipboard: {reportName}
```

This changes the shared clipboard; it does not type or paste into the application. Focus the intended input and send its paste command separately if that is part of the workflow. A later clipboard change by any application replaces this text.

Use [Read Text](Read-Text.md) to collect screen text into a variable first, and [Press Key](Press-Key.md) for key input. Image pasting into an editor's Image field is a separate editing feature, not this runtime step.
