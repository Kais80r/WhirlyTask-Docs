# Read Text

Read Text reads visible screen text and stores the result in a sequence value.

The technical word for this is OCR. It means WhirlyTask looks at an image of the screen and tries to turn the visible letters into normal text.

## Fields

| Field | Meaning |
| --- | --- |
| Area | Where to read screen text |
| Mode | What WhirlyTask keeps from the OCR result |
| Value name | The sequence value that receives the final text |
| Keep | The exact characters to keep when Mode is `Custom chars` |

The step is shown like this:

```text
Read text from [Area] as [Mode] into [Value name]
```

When Mode is `Custom chars`, a `keep` box appears at the end of the row.

## Modes

| Mode | What gets saved |
| --- | --- |
| All text | The OCR result as WhirlyTask read it |
| Numbers only | Digits, plus `.`, `,`, `-`, and `+` |
| Letters only | Letters only |
| Letters and numbers | Letters and digits only |
| First number | The first number-like value in the OCR result |
| Custom chars | Only the exact characters typed in the `keep` box |

Spaces are kept for the normal filter modes when they separate kept text. In `Custom chars`, spaces are only kept if you type a space in the `keep` box.

## What It Actually Does

Read Text scans the chosen area, filters the detected text using the selected mode, then puts the result into the value you choose. After that, other steps can use it:

```text
{statusText}
```

## Setup From Scratch

1. Add a Starting Value, for example `statusText`.
2. Set its starting text to empty.
3. Add Read Text.
4. Choose Full Screen for the first test, or select the area where the text appears.
5. Choose the mode to keep, such as `All text`, `Numbers only`, or `Custom chars`.
6. Choose `statusText` as the destination value.
7. If using `Custom chars`, type the allowed characters into `keep`.
8. Add Status Message with `{statusText}`.
9. Run the sequence and check what was read.

## Example: Read And Print

```text
Starting value:
statusText starts as empty

Main steps:
1. Read Text from selected status area as All text into statusText
2. Status Message Read: {statusText}
```

## Example: Keep A Price

```text
Starting value:
priceText starts as empty

Main steps:
1. Read Text from selected price area as Custom chars into priceText keep 0123456789.,
2. Status Message Price: {priceText}
```

This keeps only digits, dots, and commas from the OCR result.

## Example: Read And Decide

```text
1. Read Text from selected status area as All text into statusText
2. If Sequence Value statusText contains Complete
   Then:
   1. Status Message Done
   Else:
   1. Wait 2 seconds
   2. Jump Sequence Step 1
```

## Area Tips

- Select the full text line with a little space around it.
- Include a little space around the full letters.
- Avoid cutting off dots, shadows, or outlines.
- Avoid nearby icons if they are being read as letters.
- Bigger areas can read better than tiny areas because OCR gets more context.

## Useful For

- Reading a status label.
- Capturing a result number or message.
- Sending screen text in a Status or Discord message.
- Letting If Sequence Value decide based on text that changes.
- Letting a watcher react when a value changes.

## Troubleshooting

| Problem | What to try |
| --- | --- |
| The result value is blank | Create the destination value in Starting Values before reading into it |
| You want to use the text later | Use the saved value with `{ValueName}` or a separate input step |
| Text is missing or wrong | Select a larger area with margin around the text |
| A later comparison fails | Use `contains` if OCR adds spaces or line breaks |
| Custom chars saves nothing | Add every character you want to allow to the `keep` box |
| Custom chars drops spaces | Put a space in the `keep` box too |

## More About

- Full screen text workflow: [Screen Text Reading Workflow](../Guides/Screen-Text-Reading-Workflow.md)
- Values: [Values](../Values/README.md)
- Using read text later: [Using Values In Text Boxes](../Tips/Using-Values-In-Text-Boxes.md)
- Checking read text with a branch: [If Sequence Value](If-Sequence-Value.md)
- Selected area problems: [Selected Area Problems](../Troubleshooting/Selected-Area-Problems.md)
- Wrong read results: [Read Text Is Wrong](../Troubleshooting/Read-Text-Is-Wrong.md)
