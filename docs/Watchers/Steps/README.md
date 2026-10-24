# Watcher Actions

Watcher action chains use the same ordinary steps as the main graph. Add the trigger from **Watcher**, then add actions from **All**, **Basic**, or **Variable** and connect them to that trigger's chain.

| Need | Action |
| --- | --- |
| Report an event | [Status Message](../../Steps/Status-Message.md) or [Discord Message](../../Steps/Discord-Message.md) |
| Stop a main block during recovery | [Stop Block](../../Steps/Stop-Block.md) |
| Restart at a chosen main-block step | [Start Block at Step](../../Steps/Start-Block-at-Step.md) |
| Click a currently accepted visual target | [Click If Image](../../Steps/Click-If-Image.md) |
| Click recognized text and branch on delivery | [Click If Text](../../Steps/Click-If-Text.md) |
| Change a shared value | [Set Variable](../../Steps/Set-Variable.md) or [Change Variable](../../Steps/Change-Variable.md) |

The Watcher tab contains triggers rather than duplicates of all ordinary actions. [Controlling Main Blocks](Controlling-Main-Blocks.md) explains explicit recovery control.
