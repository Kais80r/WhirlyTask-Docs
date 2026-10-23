# Read Text Finds Nothing

An empty successful read and a failed OCR check are different. A completed Read Text with no accepted characters stores an empty string. Capture or recognition failure stops playback and does not publish an old value as a fresh result.

## Check The Read

1. Confirm the target is visible and not covered or minimized.
2. Select the complete line with a little margin.
3. Choose Read as: All text for the first test.
4. Enter the intended Result variable name without braces.
5. Print `{resultText}` with a Status Message immediately afterward.

Read Text can create its destination variable. You do not need to add a Starter Variable just to make a read work.

If All text works but a filtered mode is empty, inspect the allowed characters. Custom chars keeps only the exact supplied set; include spaces explicitly if needed. A number or sign missing from the OCR result cannot be recovered by an output filter.

Try a slightly larger area if the crop cuts off letters. If Full Screen works but the selected area does not, check that the area still covers the target after window, zoom, or display changes.

## Search Actions

If Text, Click Text, Click If Text, and Text Watcher also validate their search filters. An empty custom set or a query containing excluded characters is an error, not a normal “not found” result. Correct the query or use All text.

## Related Pages

- [Read Text](../Steps/Read-Text.md)
- [Text Recognition And Character Filters](../Recognition/Text.md)
- [Selected Area Problems](Selected-Area-Problems.md)
