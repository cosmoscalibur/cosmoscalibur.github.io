---
date: 2026-02-21
tags: antigravity, ampcode, windows, authentication, browser
category: technology, programming
language: en
---

# Authentication Error in Antigravity and AmpCode on Windows

If you've installed
[Antigravity](/en/blog/2026/herramientas-de-ia-gratuita-para-desarrolladores-en-2026.md)
or [AmpCode](https://ampcode.com/install) on Windows 11 and found it impossible
to log in, you're not alone. This authentication issue is more common than it
seems and the usual solutions don't always work. Here's how I solved it.

## The Problem

When trying to log in to both Antigravity and AmpCode, the browser-based
authentication process doesn't complete. In Antigravity, the login screen stays
unresponsive or fails to finish the flow. In AmpCode, the authentication link
generated in the terminal fails to complete the authorization.

## Common Solutions That Didn't Work

Searching through forums and issue reports, the most frequently mentioned
solutions are:

### `HOME` and `APPDATA` Environment Variables

The most referenced solution suggests verifying or modifying the `HOME` and
`APPDATA` user environment variables in Windows. The idea is that these
variables should correctly point to the user's profile folder, as some tools
depend on them to store credentials and configuration.

To verify them, you can open a terminal (PowerShell or CMD) and run:

```{code} powershell
echo $env:HOME
echo $env:APPDATA
```

### Copying the *Local Storage* Folder

Another mentioned solution consists of copying the *Local Storage* folder from a
successful installation (for example, from another computer or user session) to
the Antigravity or AmpCode configuration directory. While it may work as a
temporary patch, it's not a sustainable solution and doesn't address the root
cause.

### Chrome Not Detected

Some reports mention that the issue is related to Chrome not being detected by
the tool, but they don't offer a clear solution beyond pointing out the symptom.

## The Solution: Change the Default Browser to Chrome

None of the above solutions worked in my case. My default browser was Firefox,
and after exhausting the options, I tried something simple: **changing the
default browser to Google Chrome**.

To change the default browser on Windows 11:

1. Open **Settings** ({kbd}`Win+I`).
2. Go to **Apps** > **Default apps**.
3. Search for **Google Chrome** in the list.
4. Click **Set as default**.

After making this change, both Antigravity and AmpCode authentication worked
perfectly. The login flow in Antigravity completed without issues, and the
AmpCode authentication link in the terminal correctly opened the browser and
finished the authorization.

## Why Does It Work?

The OAuth authentication flow of these tools opens a URL in the system's default
browser. Although Firefox is a compatible browser, the redirect (*callback*)
flow seems to depend on a specific integration with Chrome (or Chromium-based
browsers). Since these tools are part of the Google ecosystem or rely on its
authentication infrastructure, the integration with Chrome is more robust.

## Conclusion

If you're on Windows 11 with Firefox as your default browser and can't
authenticate in Antigravity or AmpCode, try changing your default browser to
Chrome. It's a simple solution that can save you hours of frustration with
environment variables and manual patches.

## References

- [Antigravity](https://antigravity.google/download). Google DeepMind.
- [AmpCode](https://ampcode.com/install). Sourcegraph.
