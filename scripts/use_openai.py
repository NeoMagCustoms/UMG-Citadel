
import os
import openai

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

openai.api_key = api_key

# Example OpenAI GPT call
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant inside the UMG Citadel block builder."},
            {"role": "user", "content": "What is a MOLT block in UMG?"}
        ]
    )
    print("🤖 GPT Response:")
    print(response['choices'][0]['message']['content'])

except Exception as e:
    print(f"⚠️ Error contacting OpenAI: {e}")
