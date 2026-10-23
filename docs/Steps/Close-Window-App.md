# Close Window/App

Requests that a window with the configured title fragment in **Target** closes.

The native action sends the normal Windows close request. It is not a force-termination action: an application may display a save prompt or decline to close. Other windows from the same program can remain open.

```text
Start -> Close Window/App: Report
      -> Wait For: Window / Report / is not open / 10 seconds
      -> If Window: Report / is not open
```

Choose a distinctive title fragment and check the result if later actions depend on it. Closing a window can affect unsaved work in that application, just as using its own close button would.

See [If Window](If-Window.md) and [Focus Window](Focus-Window.md).
