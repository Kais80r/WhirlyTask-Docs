# Take Screenshot

Captures the selected **Screen zone** and writes a timestamped BMP image. **File prefix** supplies the beginning of the filename; unsafe filename characters are sanitized.

Use **Pick Area...** for a small relevant region, or a named screen zone for a broader capture. The native result/status message reports the saved path. The usual folder is `%LOCALAPPDATA%\WhirlyTask\screenshots`.

```text
Start -> Take Screenshot: selected report area / report
      -> Status Message: Report capture requested
```

This captures visible screen pixels. It does not read text, export the application's underlying document, or prove a later action succeeded. A capture/save failure is reported in status; inspect the result when the file is required.

For OCR output, use [Read Text](Read-Text.md). For an image used to recognize a button, use the image helper in [Click Image](Click-Image.md).
