# Build a reliable sequence

Build one connected path, observe its result, then add branches and recovery. A graph that looks organized still needs valid links and targets.

## Establish a small path

Start with `Start -> Status Message -> Finish Sequence`. Name the block, add one action, and test with **Play**. Use **Save** to update its file or Library entry. Automatic recovery retains the editing session across restart.

Add an explicit readiness check before input. Focus a window when needed, choose a narrow relevant search area, and check text/images instead of relying only on long waits.

```text
Start -> Focus Window: Report
      -> Wait For: Text / Ready / 10 seconds
      -> If Text: Ready / is seen
           Then -> the intended action -> confirmation check
           Else -> Status Message: Report was not ready -> Finish Sequence
```

Wait For continues after its timeout. The If step makes the actual decision.

## Bound retries and parallel work

Use a Starter Variable counter and a limit check for retries. A whole-sequence restart resets that counter, so use a block jump for a retry that should retain it. Give jump targets stable Step IDs.

Before starting another block, consider If Block Running. Shared variables are shared across active blocks; avoid competing cursor/keyboard actions.

## Verify important actions

Click Text and image clicks verify recognition and current target pixels before input, but a delivered click does not prove the application completed the requested operation. Confirm a meaningful post-action state. Keep click offsets inside the verified target.

Use separate negative cases: absent target, a lookalike, a closed window, and unavailable recognition. Invalid recognition must not be treated as evidence of absence.

## Save a reusable result

Use **Save** to update the Sequence in its file or Library entry, or **Save As** to keep another version as a file. For a reusable fragment, [save selected nodes as a premade block](Reusable-Premade-Blocks.md). Add a Note explaining assumptions that another editor will need.

Related: [Counter Limit](../Examples/Counter-Limit.md), [recognition](../Recognition/README.md), and [testing a sequence](../Tips/Testing-A-Sequence.md).
