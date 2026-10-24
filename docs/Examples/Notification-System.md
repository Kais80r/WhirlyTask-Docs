# Progress and completion notifications

Keep local progress messages short, and send an external completion message only after checking the result.

Declare `completed = 0` as a Math Starter Variable.

```text
Start -> Status Message: Starting report
      -> report actions
      -> If Text: Export complete / is seen
           Then -> Change Variable: completed / Add / 1
                -> Status Message: Reports completed: {completed}
                -> Discord Message: Report export confirmed; count {completed}
                -> Finish Sequence
           Else -> Status Message: Export was not confirmed -> Finish Sequence
```

Replace the confirmation with a signal that distinguishes success in your application. Set the screen area deliberately and test the absent state too. Recognition errors do not authorize an ordinary negative branch.

Configure and test the Discord webhook before running this pattern. OCR results and variable text inserted into a Discord message are sent to that destination, so choose the content intentionally.

The local status line can be replaced by later runtime messages. Store a value or inspect the application's output when you need a durable result.

See [Discord Message](../Steps/Discord-Message.md), [Status Message](../Steps/Status-Message.md), and [If Text](../Steps/If-Text.md).
