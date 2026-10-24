# Watcher Triggers

A trigger card defines when its connected Watcher actions may run. Add it from the **Watcher** tab, select it to edit the condition, then connect ordinary actions from the other toolbox tabs.

| Card | Condition | Guide |
| --- | --- | --- |
| Text Watcher | Text is seen or not seen | [Text](When-Text.md) |
| Image Watcher | Image is seen or not seen | [Image](When-Image.md) |
| Window Watcher | Window open, focus, or fullscreen state | [Window](When-Window.md) |
| Variable Watcher | Value comparison, existence, or change | [Variable](../Variable-Watcher.md) |
| Clock Time | Daily wall-clock time | [Clock time](Clock-Time.md) |
| Timer / Interval | Elapsed duration | [Timer / interval](Timer-Interval.md) |
| Chance Watcher | Probability roll | [Chance](For-Chance.md) |
| Internet Watcher | Online or offline state | [Internet](When-Internet.md) |

Every trigger has **Enabled**, **Cooldown seconds**, and **If another watcher is already running**. Timing fields vary by trigger. See [Watcher Settings](../Watcher-Settings.md).

A trigger needs a valid result. An OCR error is not confirmed missing text, and a missing variable is not an empty value for ordinary comparisons.
