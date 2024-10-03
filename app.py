from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests
import base64

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process")
async def process(request: Request, prompt: str = Form(...), image: UploadFile = File(...)):
    image_content = await image.read()
    image_base64 = base64.b64encode(image_content).decode("utf-8")

    ollama_url = "http://localhost:11434/api/generate"
    payload = {
        "model": "minicpm-v",
        "prompt": prompt,
        "images": [image_base64],
        "stream": False
    }

    response = requests.post(ollama_url, json=payload)
    print(response)
    result = response.json()

    return templates.TemplateResponse("result.html", {"request": request, "result": result["response"]})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)