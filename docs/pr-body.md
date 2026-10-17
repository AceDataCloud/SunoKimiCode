Add **Suno by Ace Data Cloud** as a standalone Kimi Code plugin using the official `kimi.plugin.json` format. The plugin includes one hosted service with explicit environment-token binding, a narrowly scoped tool allowlist, a Skill, and check/create/status commands. It does not change the conversation’s model provider or copy the existing API implementation.

Onboarding is English and Chinese: native URL installation → Ace registration/login → General application or separate API Token → environment credential location → first use and same-task completion → errors, permissions and pricing. Reuses redacted Ace Key screenshots with source/date notes and all four currently accepted UTM fields. No official Suno / Moonshot affiliation is implied.

Validation (2026-10-18):
- `python3 -m unittest discover -s tests -v`: 3 tests pass, including single-service tool scope, secret binding, truthful catalog tier, four-field attribution and onboarding assets.
- Skill quick validation and `git diff --check`: pass.
- Actual official Kimi Code **2.2.0** `/plugins install <local-path>`: manifest accepted and copied to managed storage; one Skill, one MCP server, three commands.
- Runtime test changes only the installed copy’s endpoint to a loopback fake MCP and uses inert credentials. Three fake model turns call `suno_get_task` twice with the same existing ID, receive pending then complete, and finish. Native environment bearer binding verified. No generation tool is offered by the fake server; no real token or billable call is used.
- These checks do not prove remote GitHub URL installation, live hosted auth, generated media, billing or marketplace discoverability. See `docs/validation.json`.

Publication gates: reviewed merge/tag and ordinary remote install remain outstanding. Official Curated requires maintainer acceptance; the current upstream policy does not accept external feature PRs, so `docs/marketplace-candidate.json` is a review artifact, not a claim of official listing. No `official`/`curated` tier is assigned.

Scope: no shared MCP/Skills/SDK/Backend changes. Adversarial review not requested. Merge, paid requests and production deployment are not authorized.
