# Text Watcher

Text Watcher checks for visible text in a screen zone and starts its action chain when the selected seen/not-seen condition is valid.

## Fields

| Field | Set it to |
| --- | --- |
| Text | The literal word or phrase to find; supported variable references may supply it |
| Match characters | All text, Numbers only, Letters only, Letters and numbers, First number, or Custom chars |
| Keep characters | Allowed characters when Custom chars is selected |
| Mode | is seen or is not seen |
| Screen zone | Full Screen or the selected area containing the text |
| Check every seconds | The requested interval between checks |

The shared [run settings](../Watcher-Settings.md) follow these fields.

## Filtering And Matching

The character filter applies to recognized text. The query must already contain only characters allowed by that filter. With Numbers only, query `12` may match recognized `Score:12`; query `Score12` is invalid instead of being silently rewritten to `12`.

Matching preserves meaningful word boundaries and numeric punctuation. Do not expect `Start` to match `Restart`, or `10` to stand for `1.0`. Recognition can still be wrong, so test similar words and the absence case in your actual layout.

A scan or filter error does not fire `is not seen`. A visible condition may fire again after cooldown. Use a narrow area with padding and an action that clears the cause when repeated firing is unwanted.

A Watcher detection is not a permanent click position. Use [Click If Text](../../Steps/Click-If-Text.md) in the action chain to find and verify the text again; Then runs only after that click was delivered.

See [Text Recognition](../../Recognition/Text.md), [Watcher Settings](../Watcher-Settings.md), and [Text Watcher Examples](../Examples.md#notify-when-text-appears).
