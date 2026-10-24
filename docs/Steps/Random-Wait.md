# Random Wait

Delays the current path by a duration between **Minimum seconds** and **Maximum seconds**.

Set a nonnegative minimum and a maximum no smaller than it. For example, `0.5` to `1.5` varies the pause between attempts. This changes delay timing; it does not verify the target application is ready or make repeated actions succeed.

```text
Start -> do an attempt -> Random Wait: 0.5-1.5 -> next check
```

Keep [Wait](Wait.md) for a fixed delay. Use [Wait For](Wait-For.md) when progress depends on text, an image, a window, or connectivity.
