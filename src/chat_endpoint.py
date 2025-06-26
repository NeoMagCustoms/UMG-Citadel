from fastapi import FastAPI, Request
import uvicorn
from poeumg_engine import respond

app = FastAPI()

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    prompt = data.get("prompt", "")
    return {"response": respond(prompt)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
