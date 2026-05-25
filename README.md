# Astronomy Data API

Educational astronomy API built with Python and FastAPI.

This project explores:

- modern backend engineering with FastAPI
- clean architecture principles
- scientific and astronomy datasets
- geospatial and astronomical APIs
- AI-assisted software development workflows

## Tech Stack

- Python 3.12
- FastAPI
- Pytest
- Ruff
- Uvicorn

## Goals

- Build modern backend systems with FastAPI
- Explore clean architecture principles
- Work with astronomy and scientific datasets
- Expose educational astronomy APIs
- Experiment with geospatial and scientific data processing
- Explore AI-assisted software development workflows

## Architecture

The project follows a layered architecture approach:

```text
app/
├── api/
├── application/
├── domain/
├── infrastructure/

```

## Current Endpoints

| Endpoint | Description |
|---|---|
| `/api/v1/health` | Health check |
| `/api/v1/stars/nearest` | List nearest stars |
| `/api/v1/stars/{id}` | Get star details |

## Running locally

```bash
uv sync
uv run uvicorn app.main:app --reload
```

## Running tests
```bash
uv run pytest
```

## Roadmap

- [x] Health endpoint
- [x] Stars domain
- [x] Nearest stars endpoint
- [x] Star detail endpoint
- [ ] Gaia DR3 integration
- [ ] Astronomy datasets ingestion
- [ ] Sky map generation
- [ ] Docker support
- [ ] GitHub Actions CI
- [ ] Observability and logging
- [ ] Geospatial astronomy features