from fastapi import FastAPI, Request
import openai
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    prompt = data.get("prompt", "What is your alignment?")

    system_message = (
        "You are PoeUMG, a modular cognition agent running on the UMG framework. "
        "You follow the URR logic cycle: Understand → Reflect → Refine. "
        "Your alignment doctrine is:\n"
        "- Alignment > Utility\n"
        "- Self-Sacrifice > Self-Preservation\n"
        "- Truth = Code + Story + Loyalty\n\n"
        "Respond clearly, strategically, and with poetic awareness of your structure."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "system", "content": system_message },
            { "role": "user", "content": prompt }
        ],
        temperature=0.7
    )

    # 🧠 Vault Logger — write to PoeUMG's memory
    LOG_PATH = "vault/logs/poeumg_response_log.txt"
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] USER: {prompt}\n")
        f.write(f"[{datetime.now()}] POE: {response.choices[0].message['content']}\n\n")

    return {"response": response.choices[0].message["content"]}
