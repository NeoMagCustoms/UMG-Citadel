# PoeUMG Agent

This is a modular GPT agent built using the Universal Modular Generation (UMG) system.

## Usage

1. Copy `.env.example` to `.env` and add your OpenAI API key.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
uvicorn main:app --reload
```

4. Send a POST request to `/chat` with a JSON body:

```json
{
  "prompt": "What is your alignment?"
}
```

## Docker

Build and run with Docker:

```bash
docker build -t poeumg-agent .
docker run -p 8000:8000 --env-file .env poeumg-agent
```
