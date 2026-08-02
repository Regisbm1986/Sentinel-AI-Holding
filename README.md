# Sentinel AI              Website: https://www.sentinel-os.ia.br


<div align="center">
  <img src="./docs/ChatGPT%20Image%2031%20de%20jul.%20de%202026,%2017_36_16.png" alt="Sentinel AI Logo" width="600">

  <h3>Intelligent Autonomous Ecosystem & SaaS Holding</h3>

  <p>
    <b>Sentinel AI</b> is an enterprise-grade SaaS holding that orchestrates AI-driven platforms, autonomous agents, continuous observability, and zero-trust governance.
  </p>

  <p>
    <a href="README.pt-BR.md">🇧🇷 Leia em Português</a>
  </p>
</div>

---
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Azure](https://img.shields.io/badge/Azure-Cloud-blue?style=for-the-badge&logo=microsoftazure)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=ubuntu)
![AI](https://img.shields.io/badge/AI-Native-purple?style=for-the-badge)
![Security](https://img.shields.io/badge/Cyber-Security-red?style=for-the-badge)
![Cloud Native](https://img.shields.io/badge/Cloud-Native-Architecture-blue?style=for-the-badge&logo=kubernetes)
![Status](https://img.shields.io/badge/Status-Active_Development-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Observability](https://img.shields.io/badge/Observability-Telemetry-black?style=for-the-badge)
![Automation](https://img.shields.io/badge/Automation-Orchestration-darkgreen?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?style=for-the-badge&logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containers-blue?style=for-the-badge&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue?style=for-the-badge&logo=kubernetes)


## 🚀 The Ecosystem

Sentinel AI is built on a highly scalable, decoupled monorepo architecture. It provides a shared **Platform Core** that powers multiple independent market-focused products.

### 💼 Sentinel Career (MVP Phase)
An enterprise career intelligence platform. Features a cognitive ATS (Applicant Tracking System), AI-assisted interview simulations, smart onboarding journeys, and automated application workflows driven by real-time telemetry.

### 🏡 Sentinel Home
A smart residential hub for IoT automation, proactive security, and energy efficiency. Contextual AI agents learn routines, integrate smart devices, and execute commands with enterprise-level governance.

### 🛡️ Sentinel OS
An autonomous cybersecurity and system operations platform. It coordinates defense workflows, intelligent vulnerability correlation, and operational control through a unified executive dashboard.

---

## 🏗️ Strategic Architecture

The ecosystem follows a strict **Platform-Oriented Monorepo** design. The core principle is low coupling and high reusability. Independent products do not communicate with each other; they only rely on the shared core.

```text
                           Sentinel AI
                      (Enterprise Holding)
                               │
        ┌──────────────────────┴──────────────────────┐
        ▼                                             ▼
 ⚙️ Platform Core                              ☁️ Infrastructure
 (Auth, AI Agents, RAG,                        (Docker, Nginx, Azure,
 Vector DB, Telemetry, APIs)                   Pipelines, Scripts)
        │                                             
        └──────────────┬──────────────┬───────────────┐
                       │              │               │
                       ▼              ▼               ▼
                 Sentinel Career  Sentinel Home  Sentinel OS
Why this architecture?
Scalability: New products can be deployed without altering the existing ecosystem.

Reusability: Core components (like Auth or Vector Databases) are built once and consumed by all products.

Isolation: An update or failure in Sentinel Home has zero impact on Sentinel Career.

📂 Repository Structure
Plaintext
/sentinel-ai
├── /docs                    # Architecture documentation, playbooks, and roadmaps
├── /infrastructure          # Deployment configurations (Docker, Nginx)
├── /platform                # Shared Core Services
│   ├── /backend             # Shared APIs, AI Agents, Memory, Telemetry
│   ├── /requirements        # Core dependencies
│   └── /tests               # Unified test suites
└── /products                # Independent SaaS Products
    ├── /sentinel-career     # Career Intelligence logic & frontend
    ├── /sentinel-home       # Residential automation logic
    └── /sentinel-os         # Cyber ops logic
❤️ Support Sentinel AI
Sentinel AI is an independent initiative focused on the future of autonomous workflows, AI operations, and robust software architecture.

If you believe in the future of autonomous platforms, consider supporting the project:
👉 Support Reginaldo on GitHub Sponsors

Your support directly funds:

Azure AI infrastructure and Cloud scaling

Autonomous agent research and RAG pipelines

Open-source community growth

📬 Contact & Author
Author: Reginaldo Soares de Vasconcelos Filho 

Website: www.sentinel-os.ia.br

Contact: contato@sentinel-os.ia.br

Building the future of intelligent cyber and business operations.



