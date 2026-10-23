# Counter limit

Run at most three attempts within one playback, then end deliberately. This pattern retains the counter between retries.

Add **Starter Variable**: `attempts`, `0`, **Math**. Name the work block `Work`; give its limit-check node the stable Step ID `check-limit`.

```text
Start -> If Variable: attempts >= 3 [Step ID: check-limit]
  Then -> Status Message: Limit reached -> Finish Sequence
  Else -> Change Variable: attempts / Add / 1
       -> Status Message: Attempt {attempts}
       -> one attempt
       -> Wait: 0.5
       -> Jump Block Step: Work / check-limit
```

Increment before the attempt so even failed attempts count. With a starting value of zero, the action is reached at most three times. Connect the paths rather than relying on their visual order.

Do not use Reset and Restart Sequence for the loop: that initializes `attempts` again and defeats this limit. Reset Variable also clears this attempt history if placed inside the loop.

Replace `one attempt` with a small tested action and a confirmation condition. A delivered click alone is not application success.

See [Change Variable](../Steps/Change-Variable.md), [If Variable](../Steps/If-Variable.md), and [Jump Block Step](../Steps/Jump-Block-Step.md).
