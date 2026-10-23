# Read Text Is Wrong

OCR can confuse similar glyphs, miss punctuation, or read an icon as a letter. The local multilingual model is not limited to English, but quality depends on the actual text and image.

## Isolate The Read

```text
1. Read Text
   Screen zone: selected complete line
   Read as: All text
   Result variable: resultText
2. Status Message: Read: {resultText}
```

Start with All text so that a filter does not hide the original error. Inspect `0/O`, `I/l/1`, signs, decimal separators, and accents carefully. Numbers only removes excluded characters; it cannot turn a misread `O` into the intended `0`.

## Improve The Captured Area

- Include complete letters, dots, accents, and a little margin.
- Avoid cutting through shadows or outlines.
- Exclude neighboring icons and duplicate labels.
- Wait until text stops animating; keep its window visible.
- Test the same positive and negative screen states several times.

Read Text stores text, even with Numbers only. If you later need arithmetic or a numeric comparison, check the stored value before using it.

For searches, keep All text unless you intentionally need a character filter. Do not remove punctuation just to force a near match: `1.0` and `10` describe different visible values.

## Related Pages

- [Text Recognition And Character Filters](../Recognition/Text.md)
- [Read Text](../Steps/Read-Text.md)
- [Selected Area Problems](Selected-Area-Problems.md)
- [Read Text Finds Nothing](Read-Text-Finds-Nothing.md)
