# Selected Area Problems

Recognition reads the visible pixels inside its search area. A valid area must cover the target at the moment the check runs.

## Quick Test

1. Keep the target window visible in its normal position.
2. Select the complete word, reference image, or indicator with some margin.
3. Test a visible positive state and a known negative state.
4. If the crop fails, enlarge it slightly and repeat.
5. If duplicates cause the wrong match, reduce the area around the intended copy.

Full Screen is useful for diagnosis, but a smaller suitable area reduces unrelated candidates and can reduce recognition work. An extremely tight crop can cut off accents, decimal points, shadows, or parts of the reference image.

## After Display Changes

Recheck the area after moving a window, changing zoom, resizing, switching fullscreen, or changing monitor layout/scaling. Areas refer to the screen region; they do not automatically follow every moving application control.

For Pixel image matching, the complete original-size template must fit in the area and on an observed physical monitor. For If Pixel, any matching color pixel in the area is enough, so a very broad area can match an unrelated object.

## Failure Is Not Absence

Malformed/out-of-screen areas and failed captures are errors. They must not activate inverted text/image/color checks or authorize Else. Check the status message rather than treating every unsuccessful check as “target not present.”

## Related Pages

- [Screen Recognition](../Recognition/README.md)
- [Read Text Finds Nothing](Read-Text-Finds-Nothing.md)
- [Text Clicks Wrong Place](Text-Clicks-Wrong-Place.md)
- [Image Not Found](Image-Not-Found.md)
