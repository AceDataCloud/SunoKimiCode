---
name: suno-ace
description: Generate or edit Suno music through Ace Data Cloud and retrieve the same task’s final result in Kimi Code. Use for explicit Suno requests, not other media providers.
---

# Suno by Ace Data Cloud

This plugin exposes only the Suno workflow through the existing hosted Ace service. It does not change the conversation’s LLM provider.

Start by checking the connected tool schema. For a no-generation setup check call `suno_list_models` only, and report available Suno options. Never read, echo, or ask the user to paste an API Token into the conversation; it belongs in `ACEDATACLOUD_API_TOKEN` before Kimi starts.

For a new request, confirm the requested model/action, required inputs and current price are understood. Submit `suno_generate_music` once only when the user has authorized the operation and its cost. Do not enable automatic generation retries or substitute a different model family.

Save the exact returned task_id. Use `suno_get_task` to query that same task, observing server polling guidance. When it is still pending, explain that status and stop after a bounded check; let the user resume with the same ID. Never submit another generation to poll. Suno normalizes a successful response to state=complete. Treat pending/processing as unfinished; failed is terminal. Return the audio URLs only when the tool reports completion.

If the user supplies an existing task ID, query it directly without generating. If a request returns 401/403, explain key/scope or moderation errors without requesting secrets; for 429 wait and reduce concurrency; for 5xx/timeout inspect the existing task before any separately approved resubmission.

Setup and current service information: https://platform.acedata.cloud/documents/suno-audios?utm_source=agent_skill&utm_medium=referral&utm_campaign=evergreen&utm_content=suno_kimi_readme_docs
