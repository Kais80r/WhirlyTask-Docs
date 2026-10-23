# Wait For

Waits until a selected condition matches or the timeout expires, then follows its next link.

| Field | Meaning |
| --- | --- |
| Wait for | Text, Image, Window, or Internet |
| Text / Image / Window title | Target, where applicable |
| Mode | Desired visible, window, or connectivity state |
| Screen zone | Search region for Text or Image |
| Timeout seconds | Maximum configured wait |

**A timeout also continues execution.** Follow the wait with an If condition if the next action requires proof that the condition became true. Do not interpret completion of this step as proof of a match.

Text supports **Match characters** and, for Custom chars, **Keep characters**. The requested text must conform to that filter. OCR failures or invalid filtered queries do not count as valid absence; invalid text evaluation stops playback. See [text recognition](../Recognition/Text.md).

Wait For Image uses the image condition path; the Smart/Pixel selector documented for If Image, Click Image, If Image Click, and Image Watcher is not an additional field here.

Pick a small relevant screen area and a realistic positive timeout. Use [If Text](If-Text.md), [If Image](If-Image.md), [If Window](If-Window.md), or [If Internet](If-Internet.md) for the follow-up decision.
