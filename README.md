# Business Crisis & Opportunity Intelligence Agent

## Case 06 of the AI Engineering Portfolio

An Agentic AI system for business diagnosis, investigation, scenario analysis, strategic recommendations, and human decision support.

## Business Context

- **Company:** Dubai Horizon Hospitality Group
- **Location:** Dubai
- **Hotels:** 3
- **Rooms:** 420

The business operates across leisure and business travel, with both direct and OTA booking channels.

Additional business activity includes restaurant services.

## Business Problem

The agent investigates an illustrative business crisis scenario involving:

- Revenue decline of 18%.
- Operating cost increase of 11%.
- Increasing customer acquisition costs.

**Data clarification:** These figures represent a simulated business scenario used for portfolio demonstration and controlled analysis. They are not verified results from a real company.

The exact reference period for the business problem is not specified.

The agent investigates the situation and evaluates strategic opportunities using controlled business data and deterministic financial calculations.

## Financial Data Scope

Room revenue figures are period-based financial values. However, the exact reporting dates and duration of the reference period have not been specified.

Consequently, the system does not claim that the available figures represent a specific month, quarter, or other defined reporting interval.

## Agent Capabilities

The agent can:

1. Investigate the business problem.
2. Retrieve business context and performance data.
3. Evaluate pricing and booking-channel scenarios.
4. Perform deterministic financial calculations.
5. Interpret evidence using an LLM.
6. Produce an executive recommendation.
7. Support a human decision.
8. Evaluate post-pilot results.
9. Recommend whether to scale, modify, or stop an initiative.

## Architecture

The system combines:

- LLM reasoning
- Function calling
- Deterministic Python tools
- Business data
- Investigation modules
- Financial evaluation
- Human decision control

The LLM is responsible for investigation, tool selection, interpretation, and synthesis.

Deterministic Python functions are responsible for financial calculations and controlled data access.

## API

The backend is implemented with FastAPI.

### Health Check

`GET /health`

### Root Endpoint

`GET /`

### Agent Endpoint

`POST /api/v1/ask`

Request example:

```json
{
  "question": "What is the main business opportunity?"
}
```

## Demonstration Scope

This is a controlled portfolio demonstration using simulated business data.

It does not represent a live enterprise deployment, verified client engagement, or autonomous execution in external business systems.

Strategic recommendations remain subject to human review and approval.


## Continuous Integration (CI)

The project includes an automated CI pipeline powered by GitHub Actions.

### CI Workflow

- **Workflow:** Case 06 Automated Tests
- **Configuration:** `.github/workflows/tests.yml`
- **Triggers:** Push and pull requests targeting `main`
- **Runtime:** Ubuntu Latest
- **Python:** 3.12
- **Test framework:** pytest
- **Development dependencies:** `requirements-dev.txt`
- **Execution command:** `python -m pytest -v`

### Security

The OpenAI API key is provided to the workflow through GitHub Actions repository secrets (`OPENAI_API_KEY`).

Sensitive credentials are not stored in the repository source code.

### Automated Test Coverage

The test suite covers:

- FastAPI root and health endpoints
- Successful API requests
- Empty and missing question validation
- Agent execution error handling
- Business context and performance data
- Alternative business scenarios
- Post-pilot results
- Scenario calculations
- Financial impact calculations
- Financial impact comparisons

### Latest CI Validation

**Status:** PASS

- Tests collected: 13
- Tests passed: 13
- Tests failed: 0
- Test execution time: 0.66 seconds
- Total GitHub Actions job duration: 14 seconds

The latest successful execution confirms that all 13 automated tests passed in the configured CI environment.

*Validation evidence: GitHub Actions workflow run, 27 November 2026.*
