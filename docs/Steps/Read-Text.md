# Read Text

Read Text reads visible screen text locally and stores the result as text in a variable. It uses the same multilingual OCR worker as text-search actions.

## Fields

| Field | Meaning |
| --- | --- |
| Screen zone | The visible area to read |
| Read as | Which recognized characters to retain |
| Result variable | The variable receiving the final text; enter the name without braces |
| Keep characters | Exact allowed characters when Read as is Custom chars |

Read as offers **All text**, **Numbers only**, **Letters only**, **Letters and numbers**, **First number**, and **Custom chars**. Normal filters preserve whitespace between retained groups. Custom chars keeps only characters you explicitly include, including any spaces.

These are output filters. Unlike a search action, Read Text has no query to validate. Numbers only still stores text; it does not perform arithmetic or turn the variable into a number automatically.

## Example

```text
1. Read Text
   Screen zone: selected status area
   Read as: All text
   Result variable: statusText
2. Status Message: Read: {statusText}
```

The destination can be created by the read. A Starter Variable is optional if you also need an initial value or reset behavior.

To retain a price, choose Custom chars with `0123456789.,-+` in Keep characters. Include a space only if you want spaces in the result.

## Empty Results And Failures

A completed read with no accepted text stores an empty string. Check the area and filter if that is unexpected. If capture or OCR fails, playback stops; the failed read does not overwrite the destination with a fabricated result or continue using an old value as if it were fresh.

Select the full line with some margin around the letters. Avoid unrelated icons and duplicated text. Read Text reads what is visible; it cannot read a minimized or covered target through another window.

## Related Pages

- [Text Recognition And Character Filters](../Recognition/Text.md)
- [Variables](../Values/README.md)
- [Read Text Is Wrong](../Troubleshooting/Read-Text-Is-Wrong.md)
- [Read Text Finds Nothing](../Troubleshooting/Read-Text-Finds-Nothing.md)
