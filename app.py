"""
FastAPI application for the Business Crisis & Opportunity Intelligence Agent.

This module exposes the Case 06 agent runtime as a REST API.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import run_agent


app = FastAPI(
    title="Business Crisis & Opportunity Intelligence Agent",
    description=(
        "API backend for the Case 06 Agentic AI Engineering portfolio project."
    ),
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AskRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "status": "SUCCESS",
        "service": "Business Crisis & Opportunity Intelligence Agent",
        "case": "Case 06",
        "version": "1.0.0",
    }


@app.get("/health")
def health():
    return {
        "status": "SUCCESS",
        "service": "business-crisis-opportunity-agent-api",
    }


@app.post("/api/v1/ask")
def ask_agent(request: AskRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty.",
        )

    try:
        state = run_agent(question)

        return {
            "status": "SUCCESS",
            "answer": state["final_answer"],
            "iteration": state["iteration"],
            "toolCalls": state["tool_calls"],
            "observations": state["observations"],
            "decisionLoop": len(state["tool_calls"]),
        }

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=f"Agent execution failed: {str(exc)}",
        )
