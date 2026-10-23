# Troubleshooting

Read the status message before changing several settings. Distinguish a valid negative condition from an unavailable check, a missing variable, or failed input delivery.

| Symptom | Start here |
| --- | --- |
| Text is wrong | [Read Text Is Wrong](Read-Text-Is-Wrong.md) |
| Read Text stores nothing | [Read Text Finds Nothing](Read-Text-Finds-Nothing.md) |
| A crop fails | [Selected Area Problems](Selected-Area-Problems.md) |
| Text click is misplaced or skipped | [Text Clicks Wrong Place](Text-Clicks-Wrong-Place.md) |
| Reference image is missed | [Image Not Found](Image-Not-Found.md) |
| Watcher never runs | [Watcher Does Not Fire](Watcher-Does-Not-Fire.md) |
| Main keeps running during recovery | [Main Block Keeps Running](Main-Block-Keeps-Running.md) |
| Main does not resume after recovery | [Watcher Recovery Does Not Resume The Main Block](Watcher-Recovery-Does-Not-Resume.md) |
| Variable seems empty or missing | [Value Is Blank](Value-Is-Blank.md) |
| Editor and playback show different work | [Editor Changes Disappear](Editor-Changes-Disappear.md) |
| Input reaches another application | [Wrong Window Or Focus](Wrong-Window-Or-Focus.md) |

## Small Test Pattern

1. Isolate one connected action or branch.
2. Add a Status Message before and after it.
3. Print the variables it uses.
4. Save Draft and confirm validation succeeded.
5. Test the intended positive and negative states.
6. Add watchers back one at a time.

Save Draft applies the playback graph. Session recovery, a named Library item, and a file backup are different; see [Editors And Saving](../App-Features/Editors-And-Saving.md).

For global stops, check [Crash Protection](../App-Features/Crash-Protection.md) and [Text Protection](../App-Features/Text-Protection.md). For missing external notifications, check [Discord Webhook](../App-Features/Discord-Webhook.md).
