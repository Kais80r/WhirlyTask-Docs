# Open App/File

Opens **Target** through Windows' normal open action. It can be a program path, file, or folder supported by the system.

Prefer a full path when a short name is ambiguous. Opening a file uses its associated application; the step does not choose a different application or wait for document loading to finish.

```text
Start -> Open App/File: C:\Reports\summary.xlsx
      -> Wait For: Window / summary / is open / 30 seconds
      -> If Window: summary / is open
```

Wait For also continues after a timeout, so check the window before sending dependent input. Use [Open Link](Open-Link.md) for a URL, [Focus Window](Focus-Window.md) to activate an already open window, and [Close Window/App](Close-Window-App.md) to request closing it.
