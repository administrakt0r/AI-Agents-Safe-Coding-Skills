---
name: azure-ai-translation-text-py
description: Azure AI Text Translation SDK for real-time text translation, transliteration, . Use for translating text content in applications.
risk: unknown
source: community
date_added: '2026-02-27'
---

# Azure AI Text Translation SDK for Python

Client library for Azure AI Translator text translation service for real-time text translation, transliteration, and language operations.

## Installation

```bash
pip install azure-ai-translation-text==2.0.0
```

## Environment Variables

```bash
AZURE_TRANSLATOR_KEY=<your-api-key>
AZURE_TRANSLATOR_REGION=<your-region>  # e.g., eastus, westus2
# Or use custom endpoint
AZURE_TRANSLATOR_ENDPOINT=https://<resource>.cognitiveservices.azure.com
```

## Authentication

### API Key with Region

```python
import os
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential

key = os.environ["AZURE_TRANSLATOR_KEY"]
region = os.environ["AZURE_TRANSLATOR_REGION"]

# Create credential with region
credential = AzureKeyCredential(key)
client = TextTranslationClient(credential=credential, region=region)
```

### API Key with Custom Endpoint

```python
endpoint = os.environ["AZURE_TRANSLATOR_ENDPOINT"]

client = TextTranslationClient(
    credential=AzureKeyCredential(key),
    endpoint=endpoint
)
```

### Entra ID (Recommended)

```python
from azure.ai.translation.text import TextTranslationClient
from azure.identity import DefaultAzureCredential

client = TextTranslationClient(
    credential=DefaultAzureCredential(),
    endpoint=os.environ["AZURE_TRANSLATOR_ENDPOINT"]
)
```

## Basic Translation

```python
# Translate to a single language
result = client.translate(
    body=["Hello, how are you?", "Welcome to Azure!"],
    to_language=["es"]  # Spanish
)

for item in result:
    for translation in item.translations:
        print(f"Translated: {translation.text}")
        print(f"Target language: {translation.to}")
```

## Translate to Multiple Languages

```python
result = client.translate(
    body=["Hello, world!"],
    to_language=["es", "fr", "de", "ja"]  # Spanish, French, German, Japanese
)

for item in result:
    print(f"Source: {item.detected_language.language if item.detected_language else 'unknown'}")
    for translation in item.translations:
        print(f"  {translation.to}: {translation.text}")
```

## Specify Source Language

```python
result = client.translate(
    body=["Bonjour le monde"],
    from_language="fr",  # Source is French
    to_language=["en", "es"]
)
```

## Transliteration

Convert text from one script to another:

```python
result = client.transliterate(
    body=["konnichiwa"],
    language="ja",
    from_script="Latn",  # From Latin script
    to_script="Jpan"      # To Japanese script
)

for item in result:
    print(f"Transliterated: {item.text}")
    print(f"Script: {item.script}")
```

## Get Supported Languages

```python
# Get all supported languages
languages = client.get_supported_languages()

# Translation languages
print("Translation languages:")
for code, lang in languages.translation.items():
    print(f"  {code}: {lang.name} ({lang.native_name})")

# Transliteration languages
print("\nTransliteration languages:")
for code, lang in languages.transliteration.items():
    print(f"  {code}: {lang.name}")
    for script in lang.scripts:
        print(f"    {script.code} -> {[t.code for t in script.to_scripts]}")


```

## Translation Options

```python
result = client.translate(
    body=["Hello, world!"],
    to_language=["de"],
    text_type="html",           # "plain" or "html"
    profanity_action="Marked",  # "NoAction", "Deleted", "Marked"
    profanity_marker="Asterisk", # "Asterisk", "Tag"
)

for item in result:
    translation = item.translations[0]
    print(f"Translated: {translation.text}")
```

## Async Client

```python
from azure.ai.translation.text.aio import TextTranslationClient
from azure.core.credentials import AzureKeyCredential

async def translate_text():
    async with TextTranslationClient(
        credential=AzureKeyCredential(key),
        region=region
    ) as client:
        result = await client.translate(
            body=["Hello, world!"],
            to_language=["es"]
        )
        print(result[0].translations[0].text)
```

## Client Methods

| Method | Description |
|--------|-------------|
| `translate` | Translate text to one or more languages |
| `transliterate` | Convert text between scripts |
| `get_supported_languages` | List supported languages |

## Best Practices

1. **Batch translations** — Send multiple texts in one request (up to 100)
2. **Specify source language** when known to improve accuracy
3. **Use async client** for high-throughput scenarios
4. **Cache language list** — Supported languages don't change frequently
5. **Handle profanity** appropriately for your application
6. **Use html text_type** when translating HTML content

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.
