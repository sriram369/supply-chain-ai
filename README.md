# AI in Supply Chain Management — Sriram Naidu Thota

A multi-agent AI system simulating intelligent supply chain coordination between a central warehouse and retail outlets.

> Built on top of [Responsive-AI-Clusters-in-Supply-Chain](https://github.com/Appointat/Responsive-AI-Clusters-in-Supply-Chain) (Apache 2.0) — modified and extended by Sriram Naidu Thota.

## What It Does

AI agents (1 central warehouse + 4 retail outlets) communicate in real-time to make inventory decisions based on:
- Upcoming local events (festivals, holidays)
- Weather conditions
- Customer preferences
- Current stock levels

The agents use the **Sense → Plan → Act → Verify → Learn** loop demonstrated in the supply chain presentation.

## Architecture

```
Central Warehouse Agent (Paris)
        ↕ WebSocket
  ┌─────┴─────┐
Outlet 1   Outlet 2   Outlet 3   Outlet 4
(Lyon)    (Marseille) (Nice)    (Bordeaux)
```

- **Python** — AI agents powered by LLMs via OpenRouter
- **Go** — concurrent goroutines for real-time agent communication  
- **Vue.js** — live dashboard showing agent decisions

## Setup

### Prerequisites
- Python 3.10+
- Go 1.20+
- Node.js 16+

### 1. Python backend (AI agents)

```bash
cd back_end/ai
cp .env.example .env
# Edit .env and add your OpenRouter API key
pip install poetry
poetry install
python app.py
```

### 2. Go backend (communication layer)

```bash
cd back_end/go_routine
go run main.go
```

### 3. Frontend

```bash
cd front_end
npm install
npm run serve
```

Open `http://localhost:8080` and click **Start**.

## Environment Variables

```env
OPENAI_API_KEY=your-openrouter-key
OPENAI_API_BASE_URL=https://openrouter.ai/api/v1
```

## Demo Scenario

Default scenario: **Lavender Festival in Lyon** — agents decide how much Olive Oil, Baguette, Manchego Cheese, and Black Tea to restock based on the event context.

## License

Apache 2.0 — see [LICENSE](LICENSE).
