# AI Idea Evaluation Agent

An AI-powered Venture and Product Evaluation Agent built using the Google GenAI SDK.

This project evaluates startup ideas, products, or technical concepts by:
- Performing intelligent web research using the Exa API
- Analyzing markets, competitors, and feasibility
- Synthesizing structured evaluations using Gemini models
- Managing autonomous evaluation workflows using function calling

---

# Features

- AI-driven idea evaluation
- Real-time web search using Exa API
- Structured venture analysis workflow
- Competitor and market research
- Technical feasibility assessment
- Tool-calling architecture using Google GenAI SDK
- Autonomous reasoning loop with controlled iteration
- Modular and extensible tool system

---

# Current Tooling

## Enabled Tools

### Exa Web Search
Used for:
- Market research
- Competitor discovery
- Trend analysis
- Technical research
- Gathering real-world validation data

### stop_response Tool
Used for:
- Explicitly terminating the reasoning loop
- Preventing unnecessary generations after completion

---

# Disabled Tooling

## Alpha Vantage API
The Alpha Vantage integration has currently been disabled from active model access.

The schema and infrastructure may still exist in the project for future re-enablement, but the model no longer has access to:
- Stock analytics
- Market financial metrics
- Stock exchange news retrieval

---

# Project Structure

```bash
project/
│
├── config.py
├── main.py
├── pyproject.toml
│
├── Functions/
│   ├── websearch_results.py
│   ├── stop_response.py
│   ├── call_function.py
│   └── alpha_vantage_data.py
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

---

# Install Dependencies

Using pip:

```bash
pip install -r requirements.txt
```

Or using uv:

```bash
uv sync
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
EXA_API_KEY=your_exa_api_key
```

---

# Running the Agent

```bash
python main.py "Your startup or product idea here"
```

Example:

```bash
python main.py "An AI-powered platform for predicting EV battery degradation"
```

---

# How It Works

The agent follows a structured evaluation workflow:

## 1. Idea Deconstruction
Breaks the idea into:
- Target market
- Value proposition
- Technical feasibility
- Competitive landscape

## 2. Research Phase
Uses Exa search to:
- Validate assumptions
- Discover competitors
- Analyze trends
- Find technical constraints

## 3. Synthesis
Generates:
- Risks
- Strengths
- Market opportunities
- Strategic recommendations

## 4. Task Completion
Uses the `stop_response` tool to terminate execution cleanly after evaluation completes.

---

# Core Files

## config.py

Contains:
- System prompts
- Agent behavior definitions
- Iteration configuration

---

## main.py

Handles:
- Gemini client initialization
- Tool registration
- Function calling loop
- Message orchestration

---

## websearch_results.py

Implements:
- Exa API integration
- Search result extraction
- Highlight formatting

---

# Dependencies

Main dependencies from `pyproject.toml`:

- google-genai
- exa-py
- python-dotenv
- beautifulsoup4
- pandas
- firecrawl
- serpapi

---

# Example Use Cases

- Startup validation
- Product strategy analysis
- SaaS idea evaluation
- AI product feasibility analysis
- EV/Automotive technology assessment
- Market opportunity research
- Competitor intelligence

---

# Future Improvements

- Memory-enabled agents
- Multi-agent collaboration
- Report export system
- RAG/vector database integration
- UI dashboard
- Autonomous long-form research
- Re-enable Alpha Vantage selectively

---

# License

MIT License
