---
name: atlas-cloud-media-generation
description: "Integrate optional Atlas Cloud image and video generation with live model discovery, schema validation, and safe asynchronous polling."
category: ai-media
risk: safe
source: community
date_added: "2026-08-28"
author: binyangzhu000-sudo
tags: [atlas-cloud, image-generation, video-generation, api]
tools: [claude, cursor, codex, gemini]
---

# Atlas Cloud Media Generation

## Overview

Use Atlas Cloud as an optional provider for asynchronous image or video
generation. This skill keeps model IDs and request fields live by discovering
the current catalog and reading the selected model's schema before submission.

## When to Use This Skill

- Use when a project needs an optional remote image or video generation provider.
- Use when the user asks to call an Atlas Cloud media model.
- Use when an agent must discover a currently available model before building a request.

Do not replace an application's existing default provider unless the user asks
for that behavior explicitly.

## Prerequisites

- An Atlas Cloud API key stored in `ATLASCLOUD_API_KEY`.
- Network access to `https://api.atlascloud.ai` and the selected schema URL.
- User approval before a billable generation request.

Never print, log, commit, or place the API key in a request body. Send it only in
the `Authorization: Bearer ...` header.

## Workflow

### 1. Discover a Current Model

Fetch `GET https://api.atlascloud.ai/api/v1/models`. This catalog endpoint does
not require authentication. Select only an entry where `display_console` is
`true` and whose `type` matches the requested media type.

Do not copy a model ID from an old example. Confirm the exact `model` value in
the live catalog every time.

### 2. Read the Model Schema

Fetch the URL in the selected entry's `schema` field. Use its required fields,
types, ranges, and enum values to build the request. Different models use
different names for dimensions, duration, reference media, and other options.

### 3. Submit Exactly Once

After confirming cost and user intent, send one request to:

- Image: `POST /api/v1/model/generateImage`
- Video: `POST /api/v1/model/generateVideo`

Do not automatically retry a generation `POST`. A timeout can happen after the
server accepts a billable job, so retrying can create duplicate charges. Record
the returned prediction ID before doing any other work.

### 4. Poll With Bounded Backoff

Poll the result URL returned by the submission response. If the response does
not include one, use `GET /api/v1/model/prediction/{prediction_id}`. Retry only
these `GET` requests, with bounded backoff such as 2, 4, 8, and 10 seconds.

Stop when the job reaches a terminal state. Treat `completed` or `succeeded` as
success and `failed` or `canceled` as failure. Return the URLs from `outputs` or
`output` without assuming which field a model uses.

## Python Example

The following standard-library example submits one image request. Replace the
model and input fields with values validated against the live catalog and schema.

```python
import json
import os
import time
import urllib.request

BASE_URL = "https://api.atlascloud.ai/api/v1"
API_KEY = os.environ["ATLASCLOUD_API_KEY"]


def request_json(url, *, method="GET", payload=None):
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


# Submit once. Do not wrap this call in an automatic retry loop.
submitted = request_json(
    f"{BASE_URL}/model/generateImage",
    method="POST",
    payload={
        "model": "MODEL_ID_FROM_LIVE_CATALOG",
        "prompt": "A precise description of the requested image",
    },
)
prediction = submitted.get("data", submitted)
prediction_id = prediction["id"]
result_url = prediction.get("urls", {}).get("result")
if not result_url:
    result_url = f"{BASE_URL}/model/prediction/{prediction_id}"

for delay in (2, 4, 8, 10, 10, 10):
    time.sleep(delay)
    result = request_json(result_url)
    data = result.get("data", result)
    status = str(data.get("status", "")).lower()
    if status in {"completed", "succeeded"}:
        print(json.dumps(data.get("outputs", data.get("output", []))))
        break
    if status in {"failed", "canceled"}:
        raise RuntimeError(data.get("error") or f"Generation {status}")
else:
    raise TimeoutError(f"Prediction {prediction_id} is still running")
```

## Best Practices

- Keep Atlas Cloud opt-in and preserve existing provider defaults.
- Validate the selected model's live schema immediately before submission.
- Show the model, important parameters, and estimated cost before generating.
- Use one submitted prediction ID as the idempotency boundary for a job.
- Download output URLs only after checking the final status and content type.
- Keep polling bounded so an agent cannot wait forever.

## Limitations

- Model availability, schemas, and pricing can change; this skill intentionally
  does not provide a static model table.
- Generation is asynchronous and may finish after the local polling deadline.
- A client-side timeout does not prove that a generation `POST` was rejected.
- Atlas Cloud account, quota, safety, and regional policies still apply.

## Common Pitfalls

- **Problem:** A request uses an outdated model ID or field name.
  **Solution:** Fetch the catalog and selected schema again before submission.
- **Problem:** A timed-out `POST` is retried and creates duplicate charges.
  **Solution:** Never retry generation submissions automatically; reconcile the
  original request or history first.
- **Problem:** Polling expects only one status or output field name.
  **Solution:** Normalize documented terminal states and accept both `output`
  and `outputs` after inspecting the live response.

## Related Resources

- [Atlas Cloud](https://www.atlascloud.ai/)
- [Atlas Cloud model catalog](https://api.atlascloud.ai/api/v1/models)
