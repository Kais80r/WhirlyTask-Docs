# Press Mouse Button

Presses and releases a mouse button at the current cursor position.

| Field | Meaning |
| --- | --- |
| Mouse button | M1, M2, M3, M4, or M5 |
| Hold seconds | Duration of the press |

M1 and M2 are the usual left and right buttons; M3 is the middle button, and M4/M5 are auxiliary buttons. Use a positive hold duration for a click.

The step does not locate or verify a target. Move the cursor deliberately first, or use a recognition-based click step.

```text
Start -> Set Cursor Position: chosen point -> Press Mouse Button: M1 / 0.05
```

See [Set Cursor Position](Set-Cursor-Position.md) and [Click Image](Click-Image.md).
