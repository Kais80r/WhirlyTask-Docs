# Making Areas Reliable

Choose the smallest area that contains the complete target and enough surrounding context to identify it.

- Keep all letters, accents, signs, decimal points, shadows, and outlines inside a text crop.
- Keep the complete reference image inside an image-search area.
- Exclude duplicated labels, changing counters, and unrelated icons where possible.
- Recheck the area after moving/resizing the target window or changing display scale/zoom.
- Test both the visible target and an absent or similar-looking distractor.

A larger crop can repair cut-off text, but Full Screen also introduces more unrelated candidates and work. A smaller crop is useful only if it still contains the target.

Pixel image matching needs the original reference size. If Pixel color matching needs only one matching pixel, so a broad area containing a common color may satisfy the condition in an unrelated place.

Keep WhirlyTask and other covering windows away from the target during diagnosis. Minimized content is not visible screen content.

See [Selected Area Problems](../Troubleshooting/Selected-Area-Problems.md) and [Screen Recognition](../Recognition/README.md).
