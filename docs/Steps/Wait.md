# Wait

Delays the current execution path by **Seconds** before following its next link. Other active paths and watchers may still run.

Use a small delay to avoid a tight retry loop or to allow an animation to settle. A fixed delay does not confirm readiness; [Wait For](Wait-For.md) or a condition is better when there is a visible signal.

```text
Start -> Wait: 0.5 -> Status Message: Continuing
```

The app accepts fractional seconds. Timing also depends on the system and the work being performed, so do not treat a short wait as a real-time timing guarantee.

For a delay selected between two bounds, use [Random Wait](Random-Wait.md).
