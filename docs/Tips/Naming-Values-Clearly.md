# Naming Variables Clearly

Name a variable for the information it stores: `statusText`, `retryCount`, `priceText`, or `buttonLabel` is easier to follow than several unrelated variables named `value1`.

Variable names are case-sensitive. `retryCount` and `RetryCount` do not refer to the same value. Keep spelling and Unicode characters consistent; visually similar letters are not automatically merged.

Enter the raw name in variable target/result fields. Use `{retryCount}` only when another supported field should expand its current value.

Use Starter Variables for values that should exist at playback start. Set Variable and Read Text can create destinations during playback. Add/Subtract requires an existing numeric value, so initialize a counter deliberately.

An empty value is different from a missing name. Use the appropriate If Variable presence or emptiness condition rather than assuming they are interchangeable.

The Variable library tab summarizes configured names and sources; it does not promise to display live runtime values. Avoid using that overview as a debugger for the value currently stored during playback.

See [Variables](../Values/README.md) and [Using Variables In Text Boxes](Using-Values-In-Text-Boxes.md).
