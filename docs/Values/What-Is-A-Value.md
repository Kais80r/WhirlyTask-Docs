# What Is A Variable?

A variable is a named value shared by steps during playback. It can contain text, an empty string, or a number represented as text.

## Names And References

| Field or usage | Example | Meaning |
| --- | --- | --- |
| Variable target | `attempts` | Write or compare the variable with that name |
| Read Text result variable | `resultText` | Store the OCR result under that name |
| Reference in a supported field | `{attempts}` | Substitute its value during playback |

Use raw names in target fields. Names are case-sensitive, and the name suggestions retain that spelling. Avoid relying on visually similar Unicode characters or different capitalization to refer to the same name.

## Declare A Start Value

Add **Starter Variable** from the Variable tab, set **Variable**, **Set to**, and **Interpret as**. Starter Variables are declarations initialized before the normal connected steps begin.

Use **Text** for literal text or a blank value. Use **Math** for an expression such as `(2 + 3) * 4` or `{unitPrice} * 2`. References in startup values must resolve successfully; missing or cyclic references are errors.

A variable can also be created later by Set Variable or Read Text. That does not give it a declared Reset Variable baseline.

## Change Or Clear A Value

**Set Variable** replaces the value. In Text mode, clearing **Set to** stores an empty string; it does not retain the previous text. Whitespace entered deliberately is preserved.

**Change Variable** supports **Add**, **Subtract**, and **Set number**. Give it a valid numeric amount. Math expressions and numeric comparisons require valid finite numbers; invalid arithmetic is not silently changed to zero.

## Compare A Variable

**If Variable** and **Variable Watcher** offer these comparison modes:

| Mode | Use |
| --- | --- |
| equals / not equals | Compare text, ignoring letter case |
| contains | Check whether the text contains the comparison text |
| >, >=, <, <= | Compare numeric values |
| is empty / is not empty | Check for empty text or ordinary surrounding whitespace |
| exists / does not exist | Check whether the name has been created |

The empty and existence modes do not show **Compare to**. Variable Watcher also offers **changed**.

A missing variable is not an empty variable. Ordinary comparisons against a missing name fail safely instead of selecting Then or firing a watcher. Use **exists** or **does not exist** when absence is the condition you intend. Existing values with unresolved or cyclic references also cannot be used as valid ordinary comparisons.

## Reset One Variable

[Reset Variable](Resetting-Variables.md) restores the resolved value captured from Starter Variable at the beginning of playback. It does not re-evaluate that declaration using later values.

See [Using Variable References](Using-Values-In-Messages.md) and the individual [variable step pages](README.md#choose-the-right-step).
