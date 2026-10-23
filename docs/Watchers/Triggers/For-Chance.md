# Chance Watcher

Chance Watcher makes probability rolls while a Sequence runs. A successful roll makes its action chain eligible to start.

| Field | Meaning |
| --- | --- |
| Chance percent | Probability for each roll |
| Roll every seconds | Requested interval between rolls |

Set Enabled, Cooldown seconds, and the conflict policy in the shared [Watcher Settings](../Watcher-Settings.md).

A chance is evaluated per roll, not as a guarantee over a chosen time span. Even a high percentage can fail, and repeated rolls can succeed close together when cooldown allows it.

Use this for optional variation or randomized behavior, not for a safety check or a mandatory recovery. Use a real state condition when an action must happen because of the screen, window, or variable state.
