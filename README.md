# Gemini-V1

Minimal command-line interface for Google Gemini Pro. Sends individual prompts and displays generated text — no conversation history.

## Setup

1. Install dependencies:
   ```bash
   pip install google-generativeai
   ```

2. Add your Gemini API key in `GeminiV1.py`:
   ```python
   genai.configure(api_key='YOUR_API_KEY')
   ```

## Usage

```bash
python GeminiV1.py
```

Enter a prompt and Gemini generates a single response. Type `END GEMINI` to exit.

## How It Differs from Gemini-V2

- No conversation history — each prompt is independent
- Output wrapped to 80 characters with `textwrap`
- Simpler codebase for learning the Gemini API basics
