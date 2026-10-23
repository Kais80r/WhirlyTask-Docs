# Variables

Variables let steps share text or numbers. The current editor calls them Variables; some documentation URLs retain the older word Values.

```text
statusText = Ready
attempts = 0
```

The name identifies the stored value. A target field such as **Variable** uses the name `attempts`. A supported text or value field uses `{attempts}` to read its contents during playback.

## Choose The Right Step

| Need | Step |
| --- | --- |
| Declare a value at playback startup | [Starter Variable](../Steps/Starter-Variable.md) |
| Store text, clear a value, or calculate an expression | [Set Variable](../Steps/Set-Variable.md) |
| Add, subtract, or set a number | [Change Variable](../Steps/Change-Variable.md) |
| Restore one declared startup value | [Reset Variable](../Steps/Reset-Variable.md) |
| Choose Then or Else from a comparison | [If Variable](../Steps/If-Variable.md) |
| Store recognized screen text | [Read Text](../Steps/Read-Text.md) |
| React in the background | [Variable Watcher](../Watchers/Triggers/When-Sequence-Value.md) |

## Use The Variable Tab

Select **Variable** in the toolbox. It contains the variable actions and Variable Watcher. The **Variables used** overview lists names found in the document and where they are used.

**Start value** and **Configured value** describe values written in the graph. **Read Text result** identifies an output. **No configured source** means the name is referenced but no local source was found. This overview is not a live playback monitor; it does not claim to show the current runtime value.

Target and result fields offer name suggestions. You can still enter a new name. In supported input fields, choose a name in **Choose variable**, then click **Insert** or **Replace**. Choosing a name alone does not change the field.

## Learn The Rules

- [Names, initialization, and comparisons](What-Is-A-Value.md)
- [Insert references into text and numbers](Using-Values-In-Messages.md)
- [Read screen text into a variable](Reading-Text-Into-Values.md)
- [Restore a startup value](Resetting-Variables.md)

Use descriptive names such as `attempts`, `resultText`, or `orderTotal`. Names are case-sensitive: `resultText` and `resulttext` are different variables.
