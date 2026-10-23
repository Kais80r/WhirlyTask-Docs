# Scroll Wheel

Sends mouse-wheel input for a configured duration.

| Field | Meaning |
| --- | --- |
| Direction | Up or Down |
| Speed per second | Scroll rate |
| Duration seconds | How long to send wheel input |

Place the cursor over the intended scrollable area and focus the correct application first. Applications interpret wheel input differently, so test the rate and duration on a small example.

```text
Start -> Focus Window: Report -> Set Cursor Position: report area
      -> Scroll Wheel: Down / chosen speed / 1
```

This does not scroll to a particular piece of content by itself. Use a later text or image check if reaching a visible target matters.
