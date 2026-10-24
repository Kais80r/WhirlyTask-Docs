# Fullscreen Window

Restores, focuses, and maximizes a matching window. **Target** is a window-title fragment.

The current native action maximizes the Windows window. It does not send an application's own fullscreen shortcut or request exclusive fullscreen mode.

```text
Start -> Fullscreen Window: Report -> Wait: 0.5 -> next action
```

Window geometry can change after maximizing. Recheck fixed mouse coordinates and saved screen areas before using them. For content-dependent readiness, add a text/image/window condition.

See [Focus Window](Focus-Window.md), [If Window](If-Window.md), and [selected areas](../Troubleshooting/Selected-Area-Problems.md).
