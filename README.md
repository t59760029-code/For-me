# For-me

Virtual-first home project — MVP

This repository contains a virtual-only MVP for a home dashboard and device simulator so you can develop and iterate without physical devices.

MVP features

- Simulated devices that send periodic updates to the backend
- FastAPI backend that stores latest device state in-memory and exposes a JSON API
- Simple static frontend that polls the backend and displays device states
- Docker Compose to run backend + frontend + simulator locally

Tech stack

- Backend: FastAPI (Python)
- Frontend: static HTML/JS served by nginx
- Simulator: small Python service that POSTs simulated sensor readings to the backend
- Containerization: Docker Compose

Quick start (after cloning):

1. docker compose -f infra/docker-compose.yml up --build
2. Open http://localhost:3000

Notes

- This is intentionally minimal and meant for local development. Device state is stored in memory (for persistence add a DB).
- Branch with these changes: `virtual-mvp` (created by assistant). Create a PR to merge into your default branch when ready.
