# Discord Webhook

WhirlyTask can send Discord Message steps and optional protection alerts to a server channel through an incoming webhook. This output uses the network; local OCR and image recognition do not use Discord.

## Configure It

1. Create an incoming webhook for the intended server channel in Discord. You need the appropriate channel/server permission.
2. Copy its webhook URL.
3. Open **Menu > Discord Webhook > Set Webhook...** in WhirlyTask.
4. Paste the complete URL and confirm.
5. Use **Test Message**, then check the destination channel.

The status **Discord test queued** means the send was queued, not that Discord delivery has already been confirmed. Check the channel and any reported error.

## Use It In A Sequence

```text
Discord Message: Workflow finished. Result: {resultText}
```

Test the same text with Status Message first. Crash Protection and Text Protection each have their own Discord Message toggle; enabling those alerts is separate from adding an ordinary message step.

## Troubleshooting

- Check the channel belonging to the webhook, rather than a direct message.
- If the webhook was deleted or changed, replace the URL in WhirlyTask.
- Check connectivity if no queued message arrives.
- Use cooldowns or fewer message steps if a watcher repeats an alert too often.

The URL grants posting access to that webhook. Keep it private and replace it if exposed. Check variable-expanded message content before sending private text or paths. **Clear Webhook** removes the configured URL from WhirlyTask.
