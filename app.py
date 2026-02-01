from fastapi import FastAPI, Query
from pydantic import BaseModel
import re

app = FastAPI(title="Number Counter", version="v1")

class Health(BaseModel):
    ok: bool

class NumberCountResponse(BaseModel):
    input: str
    number_count: int

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/number-count", response_model=NumberCountResponse)
def number_count(text: str = Query(..., description="Text to count numeric characters for")):
    digits = re.findall(r"\d", text)
    return {"input": text, "number_count": len(digits)}
