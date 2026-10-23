# Image Watcher

Image Watcher looks for a reference image and starts its action chain when the selected seen/not-seen condition is valid.

## Configure The Target

1. Add Image Watcher from the Watcher tab.
2. Select it and set **Image** using Choose or by pasting an image into the image field with Ctrl+V.
3. Choose **Recognition**: Smart or Pixel.
4. Choose **Mode** and **Screen zone**.
5. Configure Enabled, Cooldown seconds, and the Watcher conflict policy.

**Smart** uses learned image recognition to tolerate some visual changes. **Pixel** compares the template at its original size. Pixel mode shows **Pixel tolerance (0-255)**; zero requires exact participating RGB pixels, and a larger value permits that maximum difference in each color channel. Pixel does not scale the template or fall back to Smart.

Use a normal screen crop for transparent images. See [Pixel Recognition](../../Recognition/Pixel.md) for transparency and screen-coverage restrictions.

## Timing And Click Safety

Image Watcher has automatic scan scheduling, not an editable Check every seconds field. A larger area or uncertain target may take longer to evaluate.

The target can move or disappear after the Watcher fires. Use **Click If Image** when the action should search and click the same accepted target, then continue only after a delivered click. Do not assume a Watcher result is a permanently safe click position.

A valid scan with no target is different from an unavailable capture or engine. Errors do not count as `is not seen`. Persistent conditions can trigger again after cooldown.

See [Image Recognition](../../Recognition/Images.md), [Click If Image](../../Steps/Click-If-Image.md), and [Watcher Settings](../Watcher-Settings.md).
