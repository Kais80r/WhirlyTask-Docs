# Value Is Blank

An existing variable containing `""` is different from a variable that does not exist. A missing or cyclic reference is an error; it is not silently replaced by an empty string.

## Check The Source

1. Use the exact case-sensitive name everywhere.
2. Confirm Starter Variable, Set Variable, or Read Text ran before the value was needed.
3. Enter the raw name in destination fields and `{name}` in supported interpolation fields.
4. Check whether Reset Variable or Reset and Restart Sequence restored an initial empty value.
5. For Read Text, inspect the area and output filter.

```text
Set Variable: statusText = Testing
Status Message: Value: [{statusText}]
```

Brackets make a real empty value visible. Use If Variable **exists / does not exist** to check presence, and **is empty / is not empty** to check an existing value's content.

Read Text can create its result variable, but a successful read with no accepted characters stores an empty string. An OCR failure stops instead of presenting an old result as fresh.

The Variable tab lists configured names and sources, not live runtime contents. For picker mistakes, choose a name and use Replace to replace the whole field with one reference.

See [Variables](../Values/README.md), [Using Variables In Text Boxes](../Tips/Using-Values-In-Text-Boxes.md), and [Read Text Finds Nothing](Read-Text-Finds-Nothing.md).
