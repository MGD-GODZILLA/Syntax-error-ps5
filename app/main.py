from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from app.schema import Ticket

app = FastAPI(title="TicketStruct AI")


@app.get("/")
def home():
    return {
        "project": "TicketStruct AI",
        "status": "running"
    }


@app.post("/validate")
def validate_output(payload: dict):
    try:
        result = Ticket.model_validate(payload)
        return {
            "valid": True,
            "data": result.model_dump()
        }
    except ValidationError as exc:
        raise HTTPException(
            status_code=422,
            detail=exc.errors()
        )