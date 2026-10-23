# Text Recognition And Character Filters

WhirlyTask reads visible text using a local multilingual PaddleOCR pipeline. The current pipeline combines the PP-OCRv6 medium detector with the PP-OCRv6 small recognizer. It supports more than English, but results depend on the language, font, size, contrast, and captured area. It does not translate text.

Use [Read Text](../Steps/Read-Text.md) to store text, or search for a phrase with [If Text](../Steps/If-Text.md), [Click Text](../Steps/Click-Text.md), [Wait For Text](../Steps/Wait-For.md), and [Text Watcher](../Watchers/Triggers/When-Text.md).

## Matching Rules

Searches ignore letter case and normalize ordinary whitespace, composed/decomposed accents, and fullwidth ASCII forms. They retain punctuation and numeric identity. Under **All text**, these are different targets:

| Visible text | Search | Result |
| --- | --- | --- |
| `Restart` | `Start` | Does not match part of the longer word |
| `1.0` | `10` | Does not match |
| `19,99` | `19.99` | Does not match |
| `-10` or `−10` | `10` | Does not match the unsigned number |
| `Server: Online` | `Online` | Can match the complete word when its position is available |

Very short searches need especially strong recognition confidence. A high confidence score is still not a guarantee that OCR read every glyph correctly. Prefer a distinctive word or phrase over a common single character.

## Match Characters

Text-search actions have a **Match characters** setting. **All text** is the default. This filter changes recognized candidates; it does not silently rewrite your search query.

| Setting | Recognized characters retained |
| --- | --- |
| All text | The complete recognized text |
| Numbers only | Decimal digits, signs, dots, and commas; whitespace separates retained groups |
| Letters only | Letters, including their combining accents; whitespace separates retained groups |
| Letters and numbers | Letters and decimal digits; whitespace separates retained groups |
| First number | The first signed number-like run, including decimal punctuation |
| Custom chars | Only the exact characters in **Keep characters** |

For example, choose **Numbers only** and search for `12` to find the number in `Score:12`. Do not enter `Score12`: that query contains characters the selected filter excludes and produces an error. To search for the label and number together, use **All text**.

Normal filter modes preserve separating whitespace; removing other characters does not automatically add a space. For example, **Letters only** changes `A-B` into `AB`. Filters intentionally change candidate identity, so choose only the restriction you need. Numbers only preserves signs and decimal punctuation, including supported width variants; it must not turn a negative or decimal number into an unsigned whole number.

**First number** selects the first number in each recognized text candidate, not every later number on that line. Enter only that number as the query. It is a text filter, not a locale-aware numeric parser or a numeric comparison.

**Custom chars** is an exact allowed-character set. Include a literal space if spaces should survive. The set can come from a `{variable}`. An unknown mode, empty custom set, empty effective query, or query that does not fit the filter is an error. It is not treated as a valid absence.

## Positions And Click Safety

Whole-line matches can use the detected line bounds. Matching part of a line uses actual OCR character-group boxes. WhirlyTask does not estimate a substring position by dividing the line width by the character count.

Sometimes the model puts wanted and excluded characters in one inseparable box. For example, the colon and minus in `Score: -12.50` may share a box. A filtered search cannot safely guess the minus position in that case and reports that exact character bounds are unavailable. Keep the full phrase with **All text**, or choose a clearer target/area.

[Click Text](../Steps/Click-Text.md) checks the same text and filter again before mouse-down, then verifies that the target pixels remained stable. A changed target can be retried or skipped; an unavailable check stops playback instead of treating it as a negative result.

## Speed And Repeated Checks

The OCR worker keeps its models resident. Exact repeated image pixels can reuse recognized entries while each search query, filter, and focus area is evaluated separately. A previously validated positive may also be reused after its surrounding patch is verified against a fresh capture. Changed pixels require recognition again.

Startup, new scenes, large areas, and unsuccessful searches can take longer. Use an area that contains the whole target without unnecessary screen content. A very low watcher interval does not make a recognition pass complete faster.

## Related Pages

- [Read Text Is Wrong](../Troubleshooting/Read-Text-Is-Wrong.md)
- [Read Text Finds Nothing](../Troubleshooting/Read-Text-Finds-Nothing.md)
- [Text Clicks Wrong Place](../Troubleshooting/Text-Clicks-Wrong-Place.md)
