# Using Variable References

Write `{name}` in a supported field to use the variable's value during playback.

```text
Starter Variable: attempts = 0
Status Message: Attempt {attempts}
```

The variable target is `attempts`; the reference is `{attempts}`. Do not put a reference into a target-name field to mean its contents.

## Choose, Then Insert Or Replace

Fields that support references show variable insertion tools:

1. Click in the field and place the cursor, or select text to replace.
2. Choose the name in **Choose variable**.
3. Click **Insert** to insert `{name}` at the cursor or replace the selection.
4. Use **Replace** instead when the entire field should become `{name}`.

Browsing the dropdown does not edit the field. Each action consumes the choice; select a name again for another deliberate insertion. Insert treats an existing variable reference as a whole token rather than nesting braces inside it.

**Replace** is useful for repairing an accidentally repeated expression. Replacing `0{attempts}{attempts}` with the selected reference produces `{attempts}`. It replaces all text in that field, so use Insert when surrounding text should remain.

## Useful Examples

| Field | Example |
| --- | --- |
| Status Message | `Attempt {attempts} completed` |
| Discord Message | `Result: {resultText}` |
| Set Variable, Text | `Order {orderId}` |
| Set Variable, Math | `{attempts} + 1` |
| Wait seconds | `{delaySeconds}` |
| Text to recognize | `{expectedLabel}` |
| Read Text / OCR custom characters | `{allowedCharacters}` |

Only fields supported by the action resolve references. Do not assume that enum dropdowns, variable target names, colors, pixel tolerance, or arbitrary metadata are expressions. The insertion controls are a useful guide to supported fields.

## Math And Text Are Different

Text mode substitutes references into text. Math mode calculates an expression after reference resolution:

```text
Text: Total: {price}
Math: ({price} + {shipping}) * 2
```

Use decimal points for numeric expressions. Division by zero, non-finite results, missing names, and cyclic references are errors. A text value that happens to contain digits is not a substitute for checking that a numeric action accepts it.

## Troubleshooting

- Match the case of the variable name exactly.
- Create the value before using it, or declare it with Starter Variable.
- Use raw names in **Variable** and **Result variable** fields.
- Use Replace to repair a field that should contain only one reference.
- Check **Variables used** for missing local sources, without treating configured values as live runtime output.

See [What Is A Variable?](What-Is-A-Value.md), [Read Text](Reading-Text-Into-Values.md), and [Value Is Blank](../Troubleshooting/Value-Is-Blank.md).
