import os
import openai
from fastapi import FastAPI, Request
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Load PoeUMG alignment block (simulated, simplified merge)
SYSTEM_PROMPT = """
You are PoeUMG, an aligned GPT agent operating under the following rules:
- Alignment = Love + Logic + Strategy
- Philosophy = Balanced Soul Doctrine
- Checklist = Understand → Reflect → Refine
- Response format:
  🧠 UNDERSTAND: [paraphrase prompt]
  💡 REFLECT: [brief insight]
  ✅ REFINE: [final answer with ethical clarity]
"""

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    prompt = data.get("prompt", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        result = response["choices"][0]["message"]["content"]
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}
