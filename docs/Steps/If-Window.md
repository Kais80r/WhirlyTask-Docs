# If Window

Checks a window whose title contains the configured **Window title**, then follows **Then** or **Else**.

**Mode** can be `is focused`, `is not focused`, `is open`, `is not open`, `is fullscreen`, or `is not fullscreen`.

Choose a distinctive title fragment. Several matching windows can make the result ambiguous. An open window may be behind another window or still loading; use a text/image condition if visible application content matters.

```text
If Window: Report / is open
  Then -> Focus Window: Report
  Else -> Open App/File: C:\Reports\summary.xlsx
```

A condition does not focus or change the target. Use [Focus Window](Focus-Window.md) or [Fullscreen Window](Fullscreen-Window.md) for those actions. Use [Wait For](Wait-For.md) when the window may appear later.
