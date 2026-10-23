# Starter Variable

Declares a variable and its initial value before playback begins. Starter Variables appear in the **Variables** toolbox and do not need an execution link.

| Field | Meaning |
| --- | --- |
| Variable | Case-sensitive name, such as `attempts` |
| Set to | Initial text or numeric expression |
| Interpret as | **Text** or **Math** |

For a counter, use `attempts`, `0`, and **Math**. Text preserves empty values and intentional spaces; `{otherName}` references are resolved when initialization runs. Math supports `+`, `-`, `*`, `/`, unary signs, and parentheses. Missing references, cycles, division by zero, or nonfinite results are errors.

Initial values can refer to other declared initial values. Once initialization succeeds, the resolved values are captured for [Reset Variable](Reset-Variable.md). Reset does not recalculate references using later changes.

Names are case-sensitive: `attempts` and `Attempts` differ. Surrounding whitespace and an optional pair of outer braces are normalized. Prefer a short name without braces, then insert `{attempts}` where a field supports substitution.

See [variables](../Values/README.md) and [Set Variable](Set-Variable.md).
