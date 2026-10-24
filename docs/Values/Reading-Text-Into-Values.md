# Reading Text Into Variables

[Read Text](../Steps/Read-Text.md) recognizes visible text and stores the result in a variable. Use it when later steps need the words or number shown by the target app.

## Configure Read Text

1. Add **Read Text** to the connected main path or a Watcher action chain.
2. Set **Result variable** to a raw name such as `resultText`.
3. Choose a **Screen zone** that contains the intended text with some space around it.
4. Set **Read as** to the kind of result you need.
5. For **Custom chars**, supply **Keep characters**.
6. Test with Play before using the result in a later decision.

A Starter Variable with an empty Text start value is useful when other steps need the name to exist before the first read. It is also required if Reset Variable should later restore this name's initial state.

## Filter The Result

| Read as | Purpose |
| --- | --- |
| All text | Keep recognized text |
| Numbers only | Keep numeric characters and supported number punctuation |
| Letters only | Keep letters |
| Letters and numbers | Keep letters and digits |
| First number | Extract the first recognized number |
| Custom chars | Keep only the supplied characters |

These are output filters, not instructions that make uncertain recognition correct. A small selected area often helps more than an aggressive filter. See [Text Recognition](../Recognition/Text.md) for confidence, literal matching, and filtering limits.

## Use The Result

```text
Starter Variable: resultText = empty (Text)
Start
  Read Text: resultText / selected area / All text
  Status Message: Read: {resultText}
  If Variable: resultText / contains / Complete
```

Use the raw name `resultText` in the If Variable target, and `{resultText}` in a message. For numeric comparisons, choose an appropriate reading filter and verify that the result is a valid number.

A valid read with no recognized text can produce an empty result. A capture or OCR error is different from a successful empty read; do not treat an unavailable engine as proof that the screen contains nothing.

## Common Problems

| Symptom | Check |
| --- | --- |
| Result includes nearby labels | Use a smaller area with padding around the intended text |
| Digits are joined unexpectedly | Check the original text and selected filter; do not use letters-only data as a number |
| Reference fails | Match the result name exactly and execute Read Text first |
| Reset fails | Declare the name with Starter Variable before playback |

See [Read Text Is Wrong](../Troubleshooting/Read-Text-Is-Wrong.md) and [Making Areas Reliable](../Tips/Making-Areas-Reliable.md).
