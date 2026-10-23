# Finish Sequence

Ends the sequence's playback successfully. It has no action settings.

Connect this to a successful completion path or a deliberate limit, such as the Then output of `attempts >= 3`. Other active work should not be expected to continue after the sequence finishes.

```text
Start -> do work -> Status Message: Done -> Finish Sequence
```

A click being delivered does not prove the application accepted it. Add a confirmation condition before marking work complete when that distinction matters.

Use [Stop Block](Stop-Block.md) to stop only one block, and [Reset and Restart Sequence](Reset-And-Restart-Sequence.md) to initialize a new run. Older files can contain a Finish Advanced Track title; new graph workflows use Finish Sequence.
