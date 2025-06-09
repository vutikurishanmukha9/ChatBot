# AI-Powered Dual-Engine Chatbot & Prompt Generator

A production-ready FastAPI service that answers user queries and generates engine-specific prompts using OpenAI (ChatGPT) and Anthropic (Claude).

---

## Features

- **Multi-Engine Support**: Seamlessly switch between OpenAI and Anthropic APIs for diverse AI responses.
- **Prompt Generation**: Engine-specific prompt templates powered by Jinja2 for customizable interactions.
- **Query Logging**: All user queries and AI responses are logged in a PostgreSQL database for auditing and analytics.
- **Caching**: Redis-based caching to speed up repeated requests and reduce API costs.
- **Containerized Deployment**: Ready-to-use Docker and Kubernetes manifests for easy local and production deployment.

---

## Repository Structure

llm-chatbot/
├── app/
│ ├── main.py
│ ├── orchestrator.py
│ ├── config.py
│ ├── db/
│ │ └── models.py
│ ├── modules/
│ │ ├── qa.py
│ │ └── prompt_gen.py
│ ├── adapters/
│ │ ├── openai_adapter.py
│ │ └── anthropic_adapter.py
│ └── templates/
│ ├── openai.json
│ └── anthropic.json
├── docker/
│ ├── Dockerfile
│ └── docker-compose.yml
├── k8s/
│ ├── deployment.yaml
│ ├── service.yaml
│ └── ingress.yaml
├── tests/
│ ├── test_main.py
│ └── test_adapters.py
├── .env.example
├── requirements.txt
└── README.md
---

## Prerequisites

- Python 3.10+
- Redis server (local or cloud)
- PostgreSQL database
- API keys for OpenAI and Anthropic

---

## Quickstart

1. Clone the repository:

   ```bash
   git clone https://github.com/vutikurishanmukha9/ChatBot.git
   cd ChatBot
Copy the example environment file and configure your secrets:

bash
Copy
Edit
cp .env.example .env
Fill in your API keys and database URLs inside .env.

Build and run using Docker Compose (recommended):

bash
Copy
Edit
docker-compose up --build -d
Test the chatbot API:

bash
Copy
Edit
curl -X POST http://localhost:8000/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"Hello, chatbot!", "mode":"answer"}'
Deployment
Use the Kubernetes manifests in the k8s/ folder for production-grade deployment.

Configure secrets securely using Kubernetes Secrets.

Make sure Redis and PostgreSQL are accessible by the deployment.

Development
Run tests using pytest:

bash
Copy
Edit
pytest tests/
Use the app/main.py FastAPI app as the entry point.

Modify prompt templates in app/templates/ as needed.

Contributing
Fork the repo

Create a feature branch: git checkout -b feature/my-feature

Commit your changes

Push your branch: git push origin feature/my-feature

Open a Pull Request

License
MIT © Shanmukh Vutikuri
