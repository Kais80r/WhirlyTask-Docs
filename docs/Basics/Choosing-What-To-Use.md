# Choosing What To Use

Choose based on how the action should respond to the app, rather than how long it is.

| Your task | Start with | Why |
| --- | --- | --- |
| Replay a short fixed keyboard or mouse action | [Track](Track.md) | Recording is quicker than rebuilding each input |
| Wait for a screen state, branch, or count attempts | [Sequence](Sequence.md) | Steps can use conditions and variables |
| React to an unexpected event during normal work | [Sequence with Watchers](../Watchers/README.md) | A Watcher checks alongside the main flow |
| Reuse a working group of steps | [Premade Block](Premade-Blocks.md) | Save selected nodes and import a copy later |
| Click the same visible target after finding it | [Click If Image](../Steps/Click-If-Image.md) | Then runs only after the accepted target is clicked |
| Click a recognized phrase and choose what happens next | [Click If Text](../Steps/Click-If-Text.md) | Then requires a verified text click; confirmed absence or target loss chooses Else |

## Combine Them When Useful

A Sequence can run a Track, wait for visible confirmation, store a result, and handle a warning through a Watcher. A frequently used part of that graph can become a Premade Block.

Build a small complete path first. Add a background Watcher when an event can happen unexpectedly; use a normal If or Wait For step when checking that event is already part of the expected path.

## Recognition Choice

Use text recognition for visible words, Smart image recognition for a visual target with some variation, or Pixel image recognition for the same image at its original size. [If Pixel](../Steps/If-Pixel.md) checks a color in an area and is a separate feature.

See [Recognition](../Recognition/README.md) for the limits and settings of each method.
