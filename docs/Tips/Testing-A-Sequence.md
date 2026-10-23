# Testing A Sequence

Test the smallest connected path that demonstrates the behavior you need. Keep Stop and Emergency available before sending mouse or keyboard input.

1. Add a Status Message before the action.
2. Use a harmless action or branch message for the first test.
3. Print any relevant `{variables}`.
4. Add a Status Message afterward.
5. Check Editor Issues, then use Play to test the current graph.
6. Run the intended positive and negative cases.

For If Text, If Image, or If Pixel, put a different message in Then and Else. Test with the target present and absent. An unavailable capture or invalid configuration is a third outcome, not evidence that Else is correct.

For If Image Click, test delivery separately from application success. Then means the click was delivered; use Wait For afterward to confirm the expected visible response.

Keep watchers disabled while isolating the main path, then test them one at a time. Add cooldowns and decide whether recovery should stop a work block before it sends competing input.

Use Save to keep your work. Use Save As to preserve another version in a different file.

See [Status Messages](Using-Status-Messages-While-Building.md), [Screen Recognition](../Recognition/README.md), and [Editors And Saving](../App-Features/Editors-And-Saving.md).
