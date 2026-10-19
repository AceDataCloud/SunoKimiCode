![Suno integration icon](assets/service-icon.png)

# Suno by Ace Data Cloud for Kimi Code

A standalone **Suno** plugin for Kimi Code’s native plugin manager. Install only this service, use your own Ace API Token, and retrieve the exact same task until its final result is ready. Maintained by **Ace Data Cloud**, not an official Suno or Moonshot product. It does not replace your chat model.

[简体中文](readme/README_zh_Hans.md) · [Current pricing](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=suno_kimi_readme_pricing) · [Service documentation](https://platform.acedata.cloud/documents/suno-audios?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=suno_kimi_readme_docs)

## 1. Install in Kimi Code

Requires Kimi Code 2.2.0 or newer. In Kimi’s terminal interface:

```text
/plugins install https://github.com/AceDataCloud/SunoKimiCode/releases/tag/v0.1.0
```

This installs the pinned **v0.1.0** GitHub release. It is independently distributed by Ace Data Cloud and is not listed in Kimi’s Official or Curated catalog. Inspect the source and Kimi’s third-party trust prompt before selecting **Trust and install**. Installation copies this plugin into your user plugin directory. Keep existing plugins; do not replace global configuration.

Kimi’s [official plugin guide](https://moonshotai.github.io/kimi-code/zh/customization/plugins) describes `/plugins`, **Custom**, installation and `/reload`. The official/curated catalog does not currently list this plugin.

## 2. Register, sign in and obtain the right token

1. Open [Ace Data Cloud → Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=suno_kimi_readme_key). Register or sign in first.
2. Find **General application**; choose **Initialize General Application** if needed. Check Suno access, available balance and [current prices](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=suno_kimi_readme_price_check). A dedicated application is limited to its service; access to task queries does not authorize generation.
3. Copy the API Key on the application card, or choose **Manage Keys → Create** for a separately revocable token named `Kimi Code Suno`.
4. Review expiration, usage limits and **Allowed APIs**. If restricted, allow the operations you need: `/suno/audios`, `/suno/tasks`. Only use API paths available to your account and current service contract.

![Copy a redacted API key or open Manage Keys](assets/tutorial/get-api-key-en.png)

![Create a separate restricted token; choose a Kimi-specific name](assets/tutorial/create-api-key-en.png)

Screenshots are reused from Ace’s existing Dify guide, with secrets redacted. The example key name says `Dify tutorial`; use your own Kimi name. [Sources and dates](assets/tutorial/sources.json). Copy only the raw token, without `Bearer `, spaces or quotes. A `platform-...` management token cannot replace a service API Token.

## 3. Make the token available to Kimi

Set `ACEDATACLOUD_API_TOKEN` in the environment of the process that launches `kimi`. The manifest uses Kimi’s supported `bearerTokenEnvVar` field; it does not expand `${...}` in a header or store your key in this repository. Example macOS/Linux session (input is hidden):

```bash
read -r -s ACEDATACLOUD_API_TOKEN
export ACEDATACLOUD_API_TOKEN
kimi
```

PowerShell 7.1+:

```powershell
$env:ACEDATACLOUD_API_TOKEN = Read-Host -MaskInput
kimi
```

Enter the key when prompted by the hidden input. Never put it in a chat message, screenshot, project `.env`, workflow export or Git. Restart Kimi after changing the process environment, then run `/reload` or `/new`.

The server is `https://suno.mcp.acedata.cloud/mcp`. This plugin uses a Bearer token and does not start an OAuth login. Kimi’s trust prompt is separate from account authorization.

## 4. Check and use

Run `/suno-by-ace:check` to call `suno_list_models` and inspect available options. This performs no media generation; review account rules for any other usage.

For an existing task:

```text
/suno-by-ace:status YOUR_EXISTING_TASK_ID
```

For a new paid operation, first prepare a request:

```text
/suno-by-ace:create A short gentle instrumental piano melody for sunrise, no vocals.
```

Review the model, fields, price and requested spend before confirming submission. A media service operation and the LLM orchestrating it may both consume credits according to their respective accounts. The request is submitted once; keep the returned `task_id`. Suno normalizes a successful response to state=complete. Treat pending/processing as unfinished; failed is terminal. Return the audio URLs only when the tool reports completion. Use the same ID for later checks. Do not rerun `create` because a result is pending.

No generated-media example in this repository is presented as a completed live run. Local mock checks do not prove real generation, final media retrieval or billing.

## Troubleshooting and privacy

- **401/403:** check token value, expiration, API scope and balance. A content-policy refusal stays a refusal. Never send your key to an issue.
- **Missing tools:** `/plugins info suno-by-ace`, `/plugins mcp enable suno-by-ace suno`, then `/reload`; inspect `/mcp` for authentication or network errors.
- **Pending/timeout:** query the original ID. A failed request is not permission for automatic paid retries.
- **429:** wait and reduce concurrency.
- **No media URL:** inspect terminal success/error first; check final returned links separately. Do not invent a result.

The plugin connects to `suno.mcp.acedata.cloud`; service inputs and the Bearer token go to Ace Data Cloud. No credentials are included in the package. It reuses [SunoMCP](https://github.com/AceDataCloud/SunoMCP) and does not copy its API implementation. The manifest exposes only the listed service workflow tools: `suno_list_models`, `suno_list_actions`, `suno_generate_music`, `suno_generate_custom_music`, `suno_get_task`.

[Source](https://github.com/AceDataCloud/SunoKimiCode) · [Issues](https://github.com/AceDataCloud/SunoKimiCode/issues) · dev@acedata.cloud · [MIT](LICENSE)
