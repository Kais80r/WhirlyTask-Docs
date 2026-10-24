# Using Status Messages While Building

Status Message shows text in WhirlyTask's status display. It is a simple way to see which path ran without sending a Discord message.

```text
Status Message: Before read
Read Text into statusText
Status Message: Read: [{statusText}]
```

Brackets make an intentionally empty value easier to see. Use different Then/Else messages while testing conditions. Put a message at the start of a watcher to distinguish “trigger never ran” from “a later recovery step failed.”

Messages do not pause playback or guarantee that each message stays visible long enough to read. Add a short Wait while diagnosing if a later action immediately replaces it.

Variable references must exist when used. Missing or cyclic references are errors, not a reason to assume a blank string or default number. Avoid printing secrets into messages you might later copy or send elsewhere.

See [Status Message](../Steps/Status-Message.md), [Variables](../Values/README.md), and [Using Values In Text Boxes](Using-Values-In-Text-Boxes.md).
