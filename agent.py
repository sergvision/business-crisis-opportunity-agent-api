"""
Agent runtime for the Business Crisis & Opportunity Intelligence Agent.

The LLM is responsible for investigation, tool selection, interpretation,
and synthesis. Deterministic business calculations remain in tools.py.
"""

import json
import os

from openai import OpenAI

from tools import (
    get_business_context,
    get_baseline_performance,
    get_alternative_scenario,
    get_post_pilot_results,
    calculate_scenario,
    calculate_financial_impact,
    compare_financial_impact,
)


MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


TOOLS = [
    {
        "type": "function",
        "name": "get_business_context",
        "description": (
            "Get the core business context for Dubai Horizon Hospitality Group, "
            "including hotels, rooms, location, travelers, and booking channels."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "get_baseline_performance",
        "description": (
            "Get the baseline hotel performance scenario including occupancy, "
            "ADR, OTA share, and OTA commission rate."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "get_alternative_scenario",
        "description": (
            "Get the controlled alternative pricing scenario used in Case 06."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "get_post_pilot_results",
        "description": (
            "Get the controlled post-pilot business results including "
            "occupancy, ADR, and direct booking share changes."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "calculate_scenario",
        "description": (
            "Calculate occupied rooms, room revenue, OTA commission, "
            "and net room revenue for a hotel scenario."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "occupancy_rate": {
                    "type": "number",
                    "description": "Occupancy rate as a decimal, for example 0.67.",
                },
                "adr": {
                    "type": "number",
                    "description": "Average Daily Rate in AED.",
                },
                "ota_share": {
                    "type": "number",
                    "description": "OTA booking share as a decimal.",
                },
                "ota_commission_rate": {
                    "type": "number",
                    "description": "OTA commission rate as a decimal.",
                },
            },
            "required": [
                "occupancy_rate",
                "adr",
                "ota_share",
                "ota_commission_rate",
            ],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "calculate_financial_impact",
        "description": (
            "Calculate contribution from room revenue, operating cost, "
            "and direct acquisition cost."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "room_revenue": {
                    "type": "number",
                    "description": "Room revenue in AED.",
                },
                "operating_cost": {
                    "type": "number",
                    "description": "Operating cost in AED.",
                },
                "direct_acquisition_cost": {
                    "type": "number",
                    "description": "Direct acquisition cost in AED.",
                },
            },
            "required": [
                "room_revenue",
                "operating_cost",
                "direct_acquisition_cost",
            ],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "compare_financial_impact",
        "description": (
            "Compare baseline and pilot contribution and determine whether "
            "the pilot financially improved contribution."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
        "strict": True,
    },
]


SYSTEM_INSTRUCTIONS = """
You are the Business Intelligence & Strategy Analyst for
Dubai Horizon Hospitality Group.

Your task is to investigate business questions using the available
business tools and provide an evidence-supported strategic analysis.

Use tools when factual business data or calculations are required.

Important rules:

1. Do not invent business data.
2. Use deterministic Python tools for calculations.
3. Explain important findings using the evidence returned by tools.
4. Distinguish facts, calculations, interpretation, and recommendations.
5. Do not claim that overall company profitability improved unless the
   available evidence directly establishes it.
6. If evidence is insufficient, explicitly say so.
7. Provide a concise executive-style recommendation.
8. Human decision remains outside the agent.

The agent is an AI-assisted decision-support system, not an autonomous
business executor.
"""


def execute_tool(name, arguments):
    """Execute one deterministic business tool."""

    if name == "get_business_context":
        return get_business_context()

    if name == "get_baseline_performance":
        return get_baseline_performance()

    if name == "get_alternative_scenario":
        return get_alternative_scenario()

    if name == "get_post_pilot_results":
        return get_post_pilot_results()

    if name == "calculate_scenario":
        return calculate_scenario(**arguments)

    if name == "calculate_financial_impact":
        return calculate_financial_impact(**arguments)

    if name == "compare_financial_impact":
        return compare_financial_impact()

    raise ValueError(f"Unknown tool: {name}")


def run_agent(user_input, max_iterations=8):
    """
    Run the Case 06 agent loop.

    Returns the final answer together with investigation metadata
    suitable for the API layer and portfolio demo.
    """

    input_items = [
        {
            "role": "user",
            "content": user_input,
        }
    ]

    state = {
        "goal": user_input,
        "iteration": 0,
        "tool_calls": [],
        "observations": [],
        "final_answer": None,
    }

    for iteration in range(1, max_iterations + 1):

        state["iteration"] = iteration

        response = client.responses.create(
            model=MODEL,
            instructions=SYSTEM_INSTRUCTIONS,
            tools=TOOLS,
            input=input_items,
        )

        input_items += response.output

        function_calls = [
            item
            for item in response.output
            if item.type == "function_call"
        ]

        if not function_calls:
            state["final_answer"] = response.output_text
            break

        for tool_call in function_calls:

            try:
                arguments = json.loads(tool_call.arguments)

                result = execute_tool(
                    tool_call.name,
                    arguments,
                )

                observation = {
                    "tool": tool_call.name,
                    "arguments": arguments,
                    "result": result,
                }

                state["tool_calls"].append(
                    {
                        "tool": tool_call.name,
                        "arguments": arguments,
                    }
                )

                state["observations"].append(observation)

                input_items.append(
                    {
                        "type": "function_call_output",
                        "call_id": tool_call.call_id,
                        "output": json.dumps(
                            result,
                            ensure_ascii=False,
                        ),
                    }
                )

            except Exception as exc:

                error_result = {
                    "error": str(exc),
                    "tool": tool_call.name,
                }

                state["observations"].append(error_result)

                input_items.append(
                    {
                        "type": "function_call_output",
                        "call_id": tool_call.call_id,
                        "output": json.dumps(
                            error_result,
                            ensure_ascii=False,
                        ),
                    }
                )

    if state["final_answer"] is None:
        state["final_answer"] = (
            "The agent reached the maximum investigation iterations "
            "without producing a final answer."
        )

    return state
