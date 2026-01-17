db-start:
    cd backend && docker compose up -d

db-stop:
    cd backend && docker compose down

db-reset:
    cd backend && docker compose down -v && docker compose up -d

install-backend:
    echo "Installing backend..."
    cd backend && uv venv && uv pip install -e ".[dev]"

run-backend-dev-server: db-start
    echo "Running backend server..."
    cd backend && uv run uvicorn src.main:app --reload

run:
    # run dev environment
    just run-backend-dev-server
