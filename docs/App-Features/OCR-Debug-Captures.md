# OCR Debug Captures

The **Menu > OCR Debug Captures** toggle enables an optional diagnostic facility for OCR failures. It is separate from normal screen recognition and ordinary document saving.

Turning it on does not record every screen frame or guarantee that every failed step creates a file. The text-click path does not attach a debug-capture context, so a Click Text or Click If Text failure by itself may produce no debug files. Use [Read Text](../Steps/Read-Text.md) with a Status Message to inspect recognized text first.

## Files And Locations

When a supported diagnostic path saves a capture, it writes:

- A `.bmp` of the captured search area.
- A `.txt` report containing the action, target, zone, rectangle, image dimensions, search mode, attempt, saved image path, and diagnostic OCR-read result.

It first tries `ocr_debug` beside the WhirlyTask executable, then `%TEMP%\WhirlyTask_ocr_debug` if that directory cannot be created. Captures may contain visible text from the chosen area; inspect files before sharing them.

The report's OCR text is a diagnostic read of that saved image. It does not prove a click was delivered or that a filtered search had safe character-level coordinates.

## Using Existing Captures

Compare the image with the intended area. Look for cropped letters, missing punctuation, covering windows, unrelated icons, or a target that moved. Check the report's rectangle and OCR text together.

Turn the toggle off after a diagnostic session. Existing files are not automatically removed by disabling it; delete unwanted captures yourself when finished.

## Related Pages

- [Read Text Is Wrong](../Troubleshooting/Read-Text-Is-Wrong.md)
- [Text Clicks Wrong Place](../Troubleshooting/Text-Clicks-Wrong-Place.md)
- [Selected Area Problems](../Troubleshooting/Selected-Area-Problems.md)
