# Read screen text and use it

Use **Read Text** to collect text into a variable. Use **If Text** or **Click Text** when the job is to find a known label; reading a whole region is a different operation.

1. Choose a small screen area containing the value.
2. Add Read Text with a clear **Result variable**, such as `amount`.
3. Choose **Read as** according to the desired result: All text, Numbers only, Letters only, Letters and numbers, First number, or Custom chars.
4. Report the result with `Status Message: Read: {amount}`.
5. Test absent, changed, and unrelated content before adding a dependent action.

```text
Start -> Read Text: selected amount area / First number / amount
      -> If Variable: amount / is not empty
           Then -> Status Message: Amount: {amount}
           Else -> Status Message: No usable text read
```

An empty result is not the same as a missing variable, and OCR can misread a character. Inspect the result before numeric arithmetic or irreversible application actions. Numeric If Variable comparisons require a finite valid number; invalid input does not become an ordinary false branch.

For known-text conditions, **Match characters** filters OCR candidates, while the requested search text must already fit that filter. Read Text's **Read as** processes its output instead. These settings are independent.

See [Read Text](../Steps/Read-Text.md), [text recognition](../Recognition/Text.md), [If Variable](../Steps/If-Variable.md), and [reading text into variables](../Values/Reading-Text-Into-Values.md).
