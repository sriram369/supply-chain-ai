"""
Demo runner — Sriram Naidu Thota
AI Supply Chain Multi-Agent Demo
Scenario: Lavender Festival, Lyon outlet requesting restocks from Paris warehouse
"""
import sys
import os

# Load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv optional; export env vars manually

from multi_agent_communication_supply_chain import role_playing
from camel.types import ModelType

request_json = {
    "outlet_id": "outlet_01",
    "outlet_location": "Lyon",
    "central_hub_location": "Paris",
    "date": "2024-06-15T10:00:00Z",
    "event": "Lavender Festival",
    "event_description": (
        "The annual Lavender Festival in Lyon draws thousands of tourists. "
        "High demand expected for local specialties — Olive Oil and Baguette "
        "are top sellers during this period."
    ),
    "client_preferences": (
        "Customers prefer locally sourced, artisanal products. "
        "Olive Oil and Baguette are particularly popular."
    ),
    "weather": "sunny",
    "outlet_inventory": {
        "olive_oil":       {"current_storage_amount": 30,  "max_storage_amount": 200},
        "baguette":        {"current_storage_amount": 50,  "max_storage_amount": 300},
        "manchego_cheese": {"current_storage_amount": 80,  "max_storage_amount": 150},
        "black_tea":       {"current_storage_amount": 100, "max_storage_amount": 200},
    }
}

central_hub_json = {
    "central_hub_inventory": {
        "olive_oil":       {"current_storage_amount": 500},
        "baguette":        {"current_storage_amount": 800},
        "manchego_cheese": {"current_storage_amount": 400},
        "black_tea":       {"current_storage_amount": 600},
    }
}

print("\n" + "="*60)
print("  SRIRAM | AI SUPPLY CHAIN DEMO")
print("  Scenario: Lavender Festival — Lyon Outlet")
print("="*60 + "\n")

result, updated_hub = role_playing(
    model_type=ModelType.GPT_3_5_TURBO,
    chat_turn_limit=10,
    request_json=request_json,
    central_hub_json=central_hub_json
)

print("\n" + "="*60)
print("  DEMO COMPLETE")
print("="*60)
