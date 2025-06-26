import os
from datetime import datetime
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def compact_memory(
    source_path="vault/logs/poeumg_response_log.txt",
    output_path="vault/logs/poeumg_memory_compact.txt"
):
    if not os.path.exists(source_path):
        return {"status": "error", "message": "No source log."}

    with open(source_path, "r", encoding="utf-8") as f:
        raw_text = f.read()[-8000:]

    prompt = (
        "Compress the following memory log into its essential statements. "
        "Preserve important insights, directives, and changes in tone. "
        "Use short bullet points or numbered reflections. Omit fluff.\n\n"
        f"{raw_text}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a memory compression engine for a synthetic cognition agent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    result = response.choices[0].message.content
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"🧠 PoeUMG Compacted Memory — {datetime.now()}\n\n{result}")

    return {"status": "done", "summary": result[:300]}
