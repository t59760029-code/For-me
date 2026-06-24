# Roadmap — Virtual MVP

Goal: create a fully virtual MVP for a home dashboard so development can proceed without hardware.

Milestones

1. Project scaffolding (current)
   - README, docs, docker-compose
   - Backend API + in-memory device store
   - Static frontend that polls backend
   - Simulator that sends HTTP updates to backend

2. Improve simulator
   - Multiple device types (temperature, humidity, switch)
   - Configurable scenarios and durations

3. Persistence & history
   - Add SQLite or Postgres to store time-series data
   - Endpoint to query historical data

4. Visualisation
   - Charts (Chart.js) for historical data
   - Device management UI (add/edit/remove virtual devices)

5. Integrations (optional)
   - MQTT support (mosquitto) and adapter
   - WebSocket push from backend to frontend for real-time updates

6. CI and tests
   - Unit tests for backend
   - Linting and formatting (pre-commit)
   - GitHub Actions workflow

How I can help next

- Add DB and historical endpoints
- Replace polling with WebSocket push
- Create GitHub Actions CI
- Open a PR to merge this branch into your default branch

