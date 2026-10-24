# Basic loop

A graph loop connects a later decision back to a stable Step ID. Start with the bounded [Counter Limit](Counter-Limit.md) pattern while testing.

For a condition-driven loop, name a block `Work`, give the condition node Step ID `check-state`, and connect:

```text
Start -> If Text: Ready / is seen [Step ID: check-state]
  Then -> one small action -> Wait: 0.5
       -> Jump Block Step: Work / check-state
  Else -> Status Message: Ready is no longer visible -> Finish Sequence
```

Choose a narrow search area and a distinctive target. If recognition is unavailable, the condition must not interpret that error as valid absence. An ordinary Else means a valid check did not match.

The loop repeats while the selected state remains true. Add an attempt/time limit when endless repetition would be undesirable. Include a meaningful delay or bounded action so the loop does not spin continuously.

Use [Reset and Restart Sequence](../Steps/Reset-And-Restart-Sequence.md) when the whole workflow should begin again and reinitialize its variables.
