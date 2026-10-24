# Using Variables In Text Boxes

Use `{name}` in a supported text field to read a variable's current value. Enter just `name`, without braces, in a field that names the destination variable itself.

```text
Set Variable
Name: statusText
Value: Ready

Status Message: Current status: {statusText}
```

Names are case-sensitive: `x` and `X` are different. Use the same spelling and Unicode characters everywhere. A missing or cyclic reference stops an action that requires it; it does not silently become an empty value.

## Variable Picker

In interpolation-supported fields, **Choose variable** selects a pending name only. Browsing choices does not edit the field.

- **Insert** replaces the selected text, or inserts at the caret.
- **Replace** replaces the whole field with one `{name}` reference, useful for repairing a damaged expression.
- An action consumes the choice; choose again before another insertion.

Check the caret or text selection before Insert. For a destination/name field, use the raw-name suggestions instead of adding braces.

Not every field expands variables. Use the controls offered by that field, and check validation before playback. Numeric fields can resolve supported expressions, but an invalid number or division by zero is not converted into a usable value.

See [Variables](../Values/README.md), [Naming Variables Clearly](Naming-Values-Clearly.md), and [Value Is Blank](../Troubleshooting/Value-Is-Blank.md).
