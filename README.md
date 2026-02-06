🧠 AI-Agents-for-Medical-Diagnostics

A Python-based experimental project that demonstrates how multiple AI agents can independently analyze a medical case and produce a combined, multidisciplinary assessment using a free large language model.

⚠️ Disclaimer
This project is intended only for learning and research.
It must not be used for real medical diagnosis, treatment, or clinical decision-making.

📖 Project Description

AI-Agents-for-Medical-Diagnostics explores the idea of agent-based reasoning in complex problem domains such as healthcare.

Instead of relying on a single AI response, the system distributes the same medical report to several specialized agents. Each agent analyzes the case from a different medical perspective, and the system then consolidates their findings into a final summary.

The emphasis of this project is on:

Multi-agent system design

Parallel execution and orchestration

Prompt-based role specialization

Clean and extensible Python architecture

🧩 Conceptual Motivation

Medical cases often involve overlapping symptoms that cannot be explained from a single viewpoint.
In real practice, specialists collaborate to reach better conclusions.

This project simulates that workflow by:

Running multiple AI agents independently

Preventing agents from influencing each other

Combining diverse perspectives into one output

The result is a clearer and more structured interpretation of complex input text.

🧑‍⚕️ Implemented AI Agents
🫀 Cardiologist Agent

Examines cardiovascular-related indicators

Looks for signs such as chest discomfort, arrhythmias, or abnormal vitals

Suggests possible cardiac evaluations

🧠 Psychologist Agent

Focuses on mental health and stress-related symptoms

Identifies anxiety, panic disorders, or psychosomatic patterns

Suggests psychological evaluation or therapy approaches

🌬️ Pulmonologist Agent

Analyzes respiratory symptoms

Evaluates possible breathing disorders or lung-related causes

Recommends pulmonary tests or follow-ups

Each agent works with the same input, but produces an independent analysis.

🛠️ Technical Details

Programming Language: Python

LLM Provider: Google Gemini (free API tier)

Concurrency: Python threading

Configuration: Environment variables

Design Style: Modular, agent-oriented architecture

The project avoids unnecessary frameworks to keep the logic transparent and easy to modify.

📁 Directory Structure
AI-Agents-for-Medical-Diagnostics/
├── agents/               # Specialist agent implementations
├── Medical Reports/      # Sample synthetic medical cases
├── Results/              # Generated outputs
├── main.py               # Core orchestration logic
├── gemini_client.py      # Gemini API interface
├── requirements.txt
└── README.md

⚙️ Installation & Usage
1️⃣ Clone the repository
git clone <repository-url>
cd AI-Agents-for-Medical-Diagnostics

2️⃣ Set up a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure API access

Create a file named apikey.env in the project root:

GEMINI_API_KEY=AIza...

5️⃣ Run the program
python main.py

📤 Output Behavior

Each agent produces a textual analysis of the case

A final combined summary is generated

Results are stored in the Results/ directory

The output is designed to be human-readable, not a clinical report.

🚧 Future Improvements

Add more specialist agents (Neurology, Endocrinology, Immunology)

Support local LLMs (Ollama, llama.cpp)

Structured output formats (JSON / schema validation)

Automated testing with mocked LLM responses

Better logging and error handling


🎯 Educational Value

This project is useful for learning:

Multi-agent AI systems

Parallel task execution

Prompt engineering for role specialization

Practical integration of LLM APIs

It is especially suitable for students, AI enthusiasts, and early-stage AI engineers.