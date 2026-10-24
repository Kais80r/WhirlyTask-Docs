# Open Link

Opens the configured **URL** through Windows' registered handler, normally the default browser.

```text
Start -> Open Link: https://example.com
      -> Wait: 1 -> a page-readiness check
```

Use a complete URL. Opening the browser does not prove the page loaded, navigation succeeded, or the user is signed in. Add a visible text/image condition appropriate to the page before interacting with it.

A supported `{name}` reference can supply part of the URL. Construct and test the resulting address carefully; this step does not automatically encode variable contents as URL components.

See [Open App/File](Open-App-File.md) and [If Text](If-Text.md).
