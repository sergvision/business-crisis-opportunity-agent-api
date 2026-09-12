# Business Crisis & Opportunity Intelligence Agent

Case 06 from the AI Engineer Portfolio.

An agentic AI system for business diagnosis, investigation, scenario analysis, strategic recommendation, and human decision support.

## Business Context

**Company:** Dubai Horizon Hospitality Group  
**Location:** Dubai  
**Hotels:** 3  
**Rooms:** 420  

The business operates across leisure and business travel, with both direct and OTA booking channels.

## Business Problem

The company is experiencing:

- Revenue decline of 18% over three months
- Operating cost increase of 11%
- Increasing customer acquisition costs

The agent investigates the situation and evaluates strategic opportunities using controlled business data and deterministic financial calculations.

## Agent Capabilities

The agent can:

1. Investigate the business problem
2. Retrieve business context and performance data
3. Evaluate pricing and booking-channel scenarios
4. Perform deterministic financial calculations
5. Interpret evidence using an LLM
6. Produce an executive recommendation
7. Support a human decision
8. Evaluate post-pilot results
9. Recommend whether to scale, modify, or stop an initiative

## Architecture

The system combines:

- LLM reasoning
- Function calling
- Deterministic Python tools
- Business state
- Investigation metadata
- Financial evaluation
- Human decision control

The LLM is responsible for investigation, tool selection, interpretation, and synthesis.

Deterministic Python functions are responsible for business calculations and controlled data access.

## API

The backend is implemented with **FastAPI**.

### Health Check

`GET /health`

### Root Endpoint

`GET /`

### Agent Endpoint

`POST /api/v1/ask`

Request:

```json
{
  "question": "What is the main business opportunity?"
}
