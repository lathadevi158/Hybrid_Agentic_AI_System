# 🧠 Enterprise Hybrid RAG Agent  
### Multi-Source Agentic AI System (PDF + Database + User Uploads)

An enterprise-grade **Hybrid Retrieval-Augmented Generation (RAG)** system that intelligently answers questions across multiple data sources using an agentic architecture.

This system integrates:

- 📄 Static PDF knowledge bases  
- 🗄 Structured SQL databases  
- 📂 User-uploaded documents  

The AI agent dynamically routes queries to the appropriate source (or combines them) and generates structured, context-grounded responses.

---

## 🚀 What Makes This Project Different?

Most RAG systems work on a single data source.

This system implements:

- 🧭 Intelligent query routing (Agentic decision-making)
- 🔀 Hybrid retrieval across structured + unstructured data
- 🛡 Prompt injection detection
- 🧠 Context-bound answer synthesis
- ⚡ Scalable backend architecture

This is a **real-world enterprise knowledge intelligence system**, not a simple demo chatbot.

---

## 💼 Business Use Cases

Designed for organizations where knowledge is distributed across:

- Contracts stored in databases
- Policy documents in PDFs
- Compliance documentation
- Uploaded agreements
- Operational reports

Example scenarios:

- "Compare contract details in database with policy document."
- "Summarize uploaded agreement and validate against stored compliance rules."
- "Retrieve Q4 sales from database and cross-reference with uploaded financial report."
- "Does this uploaded document violate company policy?"

---

## 🏗 Architecture Overview

User Query
↓
API Layer (FastAPI)
↓
Injection Detection Layer
↓
Router Agent
├── SQL Agent
├── Static Document Retrieval
├── User Upload Retrieval
└── Hybrid Mode (Multi-source synthesis)
↓
LLM Response Generator
↓
Structured Answer with Source Attribution


---

## 🧠 Core System Components

### 1️⃣ Router Agent
Classifies queries into:

- SQL
- STATIC_DOC
- UPLOAD_DOC
- HYBRID

Optimizes retrieval strategy and reduces unnecessary LLM cost.

---

### 2️⃣ SQL Agent
- Generates safe, SELECT-only queries
- Prevents data modification
- Enforces schema-bound access

---

### 3️⃣ Vector Retrieval Layer
- Embedding-based semantic search
- FAISS / Redis / Qdrant support
- Metadata filtering capability

---

### 4️⃣ Injection Detection
- Identifies prompt override attempts
- Blocks malicious or unsafe instructions
- Enforces system governance rules

---

### 5️⃣ LLM Synthesis Engine
- Uses only retrieved context
- Prevents hallucinations
- Produces structured responses
- Supports source citation

---

## 🧰 Tech Stack

Backend:
- FastAPI
- Python 3.11
- Gunicorn + Uvicorn Workers

LLM & Orchestration:
- LangChain
- Google Gemini (or pluggable LLM provider)

Vector Database:
- FAISS (default)
- Redis / Qdrant (production-ready options)

Infrastructure:
- Docker (multi-stage hardened build)
- Docker Compose
- Kubernetes-ready manifests
- Horizontal Pod Autoscaling support

Security:
- Environment-based secret management
- Non-root container execution
- Readiness & liveness probes

---


---

## 🔐 Enterprise Design Principles

- Context-restricted answering
- Zero hallucination policy
- Secure SQL generation
- Injection detection before processing
- Resource isolation in Kubernetes
- Horizontal scalability

---


☸️ Production Deployment

Supports:

Dockerized deployment

Kubernetes (AKS compatible)

Autoscaling via HPA

Rolling updates with zero downtime

Secret management via Kubernetes Secrets

📊 Example Hybrid Query

"Retrieve customer revenue from database and compare it with the uploaded quarterly report."

The system will:

Generate safe SQL query

Retrieve relevant document embeddings

Combine structured + unstructured results

Synthesize a unified answer

📈 Scalability & Extensibility

This architecture supports:

Multi-tenant isolation

Role-based access control

Cloud-native deployment

Additional connectors (S3, SharePoint, etc.)

On-prem LLM integration

Observability integration (Prometheus / Grafana)

🏆 Engineering Highlights

Agent-based routing architecture

Hybrid RAG implementation

Production-grade Docker configuration

Kubernetes deployment manifests

Secure secret injection pattern

Horizontal scalability

Modular, extensible codebase

📄 License

This project is licensed under the MIT License.

👩‍💻 Author

Marpally Latha Devi
Prompt Engineer | Generative AI Developer
Focused on Agentic AI, Hybrid RAG Systems, and Enterprise AI Architecture
