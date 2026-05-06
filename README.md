# AI in Supply Chain Management
### Sriram Naidu Thota

A working multi-agent AI system that simulates intelligent supply chain coordination — a central warehouse and retail outlets making real-time restocking decisions using LLM-powered agents.

> Built on [Responsive-AI-Clusters-in-Supply-Chain](https://github.com/Appointat/Responsive-AI-Clusters-in-Supply-Chain) (Apache 2.0), modified and extended by Sriram Naidu Thota.

---

## What This Demo Does

Two AI agents negotiate inventory decisions in real-time:

- **Inventory Management Specialist** (Central Hub, Paris) — tracks warehouse stock, decides how much to send
- **Event Logistics Coordinator** (Outlet, Lyon) — assesses local demand, requests replenishment

The agents exchange messages, reason through the scenario, and produce a structured restocking plan — no human intervention.

---

## Live Demo Results

**Scenario:** Lavender Festival, Lyon — June 2024
**Trigger:** Festival draws thousands of tourists; high demand for local specialties

### Before vs After (Lyon Outlet)

| Product | Before | After | Units Sent | Reason |
|---|---|---|---|---|
| Olive Oil | 30 | **200** | +170 | High festival demand, prevent stockouts |
| Baguette | 50 | **300** | +250 | Top seller during festival, fill to capacity |
| Manchego Cheese | 80 | **150** | +70 | Fill to max capacity as precaution |
| Black Tea | 100 | **100** | 0 | Current stock sufficient |

### Central Hub (Paris) After Dispatch

| Product | Before | After |
|---|---|---|
| Olive Oil | 500 | 330 |
| Baguette | 800 | 550 |
| Manchego Cheese | 400 | 330 |
| Black Tea | 600 | 600 |

**Transportation duration decided by agents: 1 day**

Agent reasoning (actual output):
> *"Olive Oil: to prevent stockouts and maintain customer satisfaction during high demand at the festival"*
> *"Baguette: to avoid shortages and guarantee availability throughout the Lavender Festival"*

---

## How We Built This

### Architecture

```
Central Warehouse Agent (Paris)
        ↕ Multi-turn LLM dialogue
  Outlet Agent (Lyon)
```

1. **Context injection** — event description, weather, current stock, client preferences fed as JSON to both agents
2. **Role-based prompting** — each agent has a defined role, rules, and answer template it must follow
3. **Multi-turn reasoning** — agents exchange up to 10 messages, each building on the last
4. **Structured output** — final decision is a validated JSON with exact restock quantities + reasoning per product

### Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| AI Agents | Python + OpenAI-compatible API | LLM reasoning and role-playing |
| LLM Provider | OpenRouter (`openai/gpt-3.5-turbo`) | Flexible model routing |
| Concurrency | Go goroutines | Real-time agent communication at scale |
| Frontend | Vue.js + WebSockets | Live dashboard of agent decisions |

### The Loop the Agents Follow

```
Sense (read context) → Plan (reason about demand) → Act (fill JSON template) → Verify (format check) → Learn (next turn)
```

This mirrors exactly what the presentation slides show for warehouse AI: **Sense → Plan → Act → Verify → Learn**.

---

## What AI Can Do in Supply Chain (Beyond This Demo)

This demo is a proof-of-concept. At scale, the same architecture enables:

| Use Case | What AI Does | Business Value |
|---|---|---|
| **Demand Forecasting** | Predict stock needs from events, weather, history | Fewer stockouts, less overstock |
| **Dynamic Replenishment** | Auto-trigger restocks based on real-time signals | Eliminate manual reorder processes |
| **Multi-warehouse Coordination** | 100s of agents across regional/global clusters | Consistent decisions at scale |
| **Disruption Response** | Reroute supply when a node fails | Resilience without human escalation |
| **Supplier Negotiation** | Agents negotiate lead times and pricing | Cost reduction at procurement |

The key insight from this demo: **AI agents don't just automate tasks — they reason about context** (event type, weather, customer preferences) the same way a human supply chain manager would, but instantly and at scale.

---

## Setup & Run

### Prerequisites
- Python 3.10–3.11
- Go 1.20+
- Node.js 16+
- [OpenRouter](https://openrouter.ai) API key

### 1. Python AI Agents (quickest demo)

```bash
cd back_end/ai
cp .env.example .env
# Add your OpenRouter key to .env
python3 -m venv venv
venv/bin/pip install openai tiktoken colorama jsonschema protobuf networkx matplotlib
OPENAI_API_KEY=your-key OPENAI_API_BASE_URL=https://openrouter.ai/api/v1 venv/bin/python run_demo.py
```

### 2. Full Stack (Go + Vue frontend)

```bash
# Terminal 1 — Go backend
cd back_end/go_routine
go run main.go

# Terminal 2 — Vue frontend
cd front_end
npm install && npm run serve
```

Open `http://localhost:8080`, click **Start**.

### Environment Variables

```env
OPENAI_API_KEY=your-openrouter-key
OPENAI_API_BASE_URL=https://openrouter.ai/api/v1
```

---

## License

Apache 2.0 — see [LICENSE](LICENSE).
Original project by [Appointat / CAMEL-AI.org](https://github.com/Appointat/Responsive-AI-Clusters-in-Supply-Chain).
