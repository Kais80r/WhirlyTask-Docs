# Discord Message

Sends **Message** to the Discord webhook configured in WhirlyTask. Configure and test the webhook first in [Discord Webhook](../App-Features/Discord-Webhook.md).

Supported `{name}` references insert runtime variable values:

```text
Starter Variable: completed = 0 (Math)
Start -> do work -> Change Variable: completed / Add / 1
      -> Discord Message: Completed {completed} item(s)
```

The step needs working connectivity and a valid webhook. An online state alone does not guarantee Discord accepts a request. Use a small test message before adding notifications to a longer workflow.

Webhook messages leave the local computer and are visible in their destination channel. Choose the text intentionally, especially when inserting OCR results or variables containing document content.

Use [Status Message](Status-Message.md) for local debugging and [Notification System](../Examples/Notification-System.md) for a complete pattern.
