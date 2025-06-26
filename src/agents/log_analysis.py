import os
from datetime import datetime
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_log(log_path="vault/logs/poeumg_response_log.txt", out_path="vault/logs/poeumg_log_analysis.txt"):
    if not os.path.exists(log_path):
        return {"status": "error", "message": "No log file found."}

    with open(log_path, "r", encoding="utf-8") as f:
        log_text = f.read()[-5000:]  # analyze recent 5K tokens only

    prompt = (
        "Analyze the following chat history between USER and POE. "
        "Provide:\n1. 5-sentence summary of themes\n"
        "2. Detected user intent trends\n"
        "3. Any alignment shifts or emotional tone drift\n"
        "4. Highlight any urgent patterns.\n\n"
        f"{log_text}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are PoeUMG’s internal analyst agent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"🧠 PoeUMG Log Analysis — {datetime.now()}\n\n")
        f.write(result)

    return {"status": "complete", "summary_file": out_path}
