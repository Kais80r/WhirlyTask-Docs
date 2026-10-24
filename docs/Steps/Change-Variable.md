# Change Variable

Updates a numeric variable without building a separate assignment expression.

| Field | Meaning |
| --- | --- |
| Variable | Target name |
| Mode | **Add**, **Subtract**, or **Set number** |
| Amount | Finite number or supported numeric expression/reference |

Add and Subtract require an existing numeric value. Text such as `ready`, a missing value, invalid arithmetic, division by zero, or overflow is an error; the previous value is retained. Set number can create the target variable.

Counter updates are applied atomically, including when parallel blocks change the same counter. The value remains shared across those blocks; this does not make a whole multi-step workflow atomic.

```text
Starter Variable: attempts = 0 (Math)
Start -> Change Variable: attempts / Add / 1
      -> Status Message: Attempt {attempts}
```

Variable names are case-sensitive. Use [Set Variable](Set-Variable.md) for text, [Reset Variable](Reset-Variable.md) for the resolved start value, and [If Variable](If-Variable.md) to enforce a limit.
