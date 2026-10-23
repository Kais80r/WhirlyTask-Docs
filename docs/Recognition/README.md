# Screen Recognition

Choose recognition by what you need to identify on the visible screen.

| Target | Use | How it decides |
| --- | --- | --- |
| A readable label or number | [Text recognition](Text.md) | Local multilingual OCR reads the visible characters |
| The same icon, button artwork, or other reference image | [Smart image recognition](Images.md) | Learned image features and geometry verify the reference |
| An image that must appear at its original pixel size | [Pixel image recognition](Pixel.md#pixel-image-recognition) | Every included image pixel must satisfy the chosen RGB tolerance |
| Any pixel of a particular color | [If Pixel](../Steps/If-Pixel.md) | At least one observed pixel in the area must satisfy the color tolerance |

Text and Smart image recognition run locally. They do not send captured screen images to a remote recognition service. Recognition can still miss or misread a target; choose a specific reference and a useful search area, then test the intended positive and negative states.

## Search, Click, Or Branch

- [If Text](../Steps/If-Text.md) and [If Image](../Steps/If-Image.md) choose a branch after a valid check.
- [Click Text](../Steps/Click-Text.md) and [Click Image](../Steps/Click-Image.md) locate a target and verify it again before clicking.
- [Click If Image](../Steps/Click-If-Image.md) and [Click If Text](../Steps/Click-If-Text.md) choose Then only after a verified click was delivered. A valid absence or exhausted target loss chooses Else.
- [Read Text](../Steps/Read-Text.md) stores recognized text in a variable.
- [Watchers](../Watchers/README.md) check conditions while playback runs.

An unavailable check is different from a valid result saying the target was absent. Invalid configuration, capture failure, or an unavailable recognition worker must not activate an inverted watcher or authorize an Else branch.

## Pick A Useful Area

Include the complete target with some surrounding space. Exclude duplicate labels, unrelated controls, and changing artwork where possible. A smaller suitable area can reduce recognition work; a crop that cuts through a word or reference image can make detection fail.

See [Selected Area Problems](../Troubleshooting/Selected-Area-Problems.md) for a testing checklist.
