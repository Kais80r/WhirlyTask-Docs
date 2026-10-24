# Text Clicks Wrong Place

First separate an incorrect text match from a duplicate label or an offset problem. Click Text and Click If Text use actual OCR boxes and verify the target again before mouse-down, but OCR can still misread a scene.

## Check In This Order

1. Set Click offset to `0,0`.
2. Restrict Screen zone to the intended control or dialog.
3. Search for a distinctive complete word or phrase.
4. Use All text until the basic match works.
5. Read the same area with Read Text and print the result.

The same `OK` label may appear in multiple windows. A smaller suitable area is more useful than assuming the first recognized copy is the desired one.

Offsets remain within the verified text target; they are not a way to click an unrelated control outside its bounds. Use an explicit mouse action for such a workflow.

## Filtered Targets

The query must already fit Match characters. Numbers only with query `12` may locate the digits in `Score:12`. If the model cannot separate those digits from excluded characters using actual OCR boxes, the check reports unavailable rather than estimating a click position.

Do not shorten a target to a common single character just to bypass a miss. Keep signs and decimals meaningful: `-10`, `10`, and `1.0` are different targets.

## Cancelled Or Skipped Clicks

The target may have changed during the configured delay or hover. WhirlyTask can retry up to three guarded attempts. If no stable target remains, ordinary Click Text skips and continues; Click If Text chooses Else. Then on Click If Text requires a delivered click. Unavailable verification or input-delivery failure stops playback without taking either branch. Inspect the status message before changing the area or delay.

## Related Pages

- [Click Text](../Steps/Click-Text.md)
- [Click If Text](../Steps/Click-If-Text.md)
- [Text Recognition And Character Filters](../Recognition/Text.md)
- [Selected Area Problems](Selected-Area-Problems.md)
