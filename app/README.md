# FoxCloud — current Reflex app

This is the canonical guide for the **current FoxCloud Reflex app**. It is a Persian-language (RTL) tool for generating a **VLESS URI** and **manual Base64 subscription text** from the settings of a server you already control. The output is configuration text, not a connection or an active service. The [root README](../README.md) and the older documents under `docs/` describe the historical Cloudflare Worker project; they are **not** instructions or a feature list for this Reflex app. Those older documents have not been updated here.

## Pages and use

- `/` — Persian introduction, usage steps, and an explanation of what the app does and does not provide.
- `/sub` — configuration form and generated results. Open it from the home page's configuration-tool link.

On `/sub`, enter the actual settings of an **external compatible VLESS server**:

| Input | What to enter |
| --- | --- |
| User UUID | The UUID configured for your user on the server. |
| Server address | A valid domain, IPv4 address, or IPv6 address, without a scheme or port; IPv6 may be entered in brackets. |
| Port | The server's port, from 1 to 65535. |
| Security | `TLS` or `none`, matching the server. |
| SNI | A domain name matching the server's certificate when TLS is selected; not needed when TLS is off. |
| WebSocket path | A path beginning with `/`, matching the server's WebSocket configuration. |
| Display name | A nonempty label to show in a compatible client. |

Press **ساخت لینک و اشتراک** (Generate link and subscription). Invalid input produces a Persian validation message; a new submission clears any previous output before generating again. When successful, the page displays a copyable `vless://` URI with WebSocket settings and a Base64-encoded UTF-8 text containing that same URI. Copy the URI or the encoded text into a compatible client that supports the corresponding import format. The Base64 text is a **manual subscription payload**, not a subscription URL: there is no hosted subscription endpoint or automatic update feed.

## Boundaries and data

The Reflex app does **not** run or host a VLESS proxy, forward WebSocket traffic, or provide a `/ws` endpoint. Publishing this interface cannot make a server available. You must separately obtain and configure an accessible, compatible external server, and the UUID, address, port, security, SNI, and WebSocket path must agree with its actual settings. Generating a syntactically valid link does not verify the server or guarantee a working connection.

Form inputs and generated results are handled in application state for the current interaction; this app does **not** save them to a database or file. Do not treat the tool as storage for your configuration. Copy any output you need before leaving or refreshing the page.

## Publish in Reflex Build

1. Open **this FoxCloud app** in Reflex Build and confirm that `/` shows the Persian home page and `/sub` shows the generator form.
2. Use the **Publish** button in Reflex Build to start publishing the Reflex app.
3. Open the **Publishing** tab to check the publishing status and, once available, the published app. Check both `/` and `/sub` there. Publishing the UI does not deploy a VLESS server or a hosted subscription service.

**This process has NOT clicked Publish.** No live deployment or published URL is claimed by this guide.
