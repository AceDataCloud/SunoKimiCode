---
description: Retrieve an existing Suno task without generating again
---

Use `suno_get_task` with the existing task ID in $ARGUMENTS. Suno normalizes a successful response to state=complete. Treat pending/processing as unfinished; failed is terminal. Return the audio URLs only when the tool reports completion. Never create a new task to retrieve this result.
