# Text Protection

Text Protection is a global stop rule for a visible phrase. Set it with **Menu > Text Protection > Set Text...**. Choose Off to disable it.

It checks before playback starts and periodically during playback. It is not a continuous guarantee that every briefly displayed message will be observed.

## Detection And Failure

The current production path uses the local multilingual text-search worker. It searches the visible full screen using the normal unfiltered matching rules. This global menu does not expose the sequence actions' Match characters filters.

If the phrase is found, playback is stopped or not started. If recognition is unavailable, protection also prevents/halts playback because it cannot declare the screen safe. The status distinguishes unavailable recognition from a phrase being found.

Choose a clear, distinctive phrase. Test it in the actual font and screen state; OCR can miss or misread text. Avoid a generic word that appears in unrelated windows.

## Alerts And Alternatives

After configuring [Discord Webhook](Discord-Webhook.md), its separate Discord Message toggle can notify you about a confirmed protection stop. An unavailable OCR check must not be reported as if the phrase had been recognized.

Use [Wait For Text](../Steps/Wait-For.md) to pause one point in a workflow. Use a [Text Watcher](../Watchers/Triggers/When-Text.md) when you need a chosen area, a character filter, cooldown, or custom recovery steps.

See [Text Recognition And Character Filters](../Recognition/Text.md) for the shared matching rules and limitations.
