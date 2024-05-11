from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/generate")
def generate_response(prompt: Prompt):
    input_prompt = prompt.prompt

    try:
        output = subprocess.check_output(["ollama", "run", "llama2", input_prompt], text=True)
        response = output.strip()
    except subprocess.CalledProcessError as e:
        response = f"Error: {e.output}"

    return {"response": response}
