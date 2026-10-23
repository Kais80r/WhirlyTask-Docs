# Status Message

Writes **Message** to WhirlyTask's status output. It is useful for checking which branch ran and what a variable contains.

```text
Start -> Status Message: Starting attempt {attempts}
```

Declare or assign referenced variables before the message executes. Variable names are case-sensitive. Use short labels such as `Found target`, `Retry {attempts}`, and `Limit reached` while building a graph.

Status is transient output, not a persistent execution log. Later application/runtime messages can replace it, including completion messages. Do not use the status line as the stored result of your automation; use a variable or the application's own output.

For an external notification, use [Discord Message](Discord-Message.md). For an editor explanation that does not report runtime progress, use [Note](Note.md).
