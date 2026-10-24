# Focus Window

Brings a matching window to the foreground. Enter a distinctive title fragment in **Target**.

If the window is minimized, WhirlyTask attempts to restore it. Windows can restrict foreground changes, so an attempted focus action is not proof that subsequent input will reach the intended application.

```text
Start -> Focus Window: Report -> If Window: Report / is focused
  Then -> Press Key: Enter
  Else -> Status Message: Report did not receive focus
```

Choose a fragment that distinguishes the intended window from other open documents. Use [If Window](If-Window.md) to check state, [Open App/File](Open-App-File.md) to launch a target, or [Fullscreen Window](Fullscreen-Window.md) to maximize it.
