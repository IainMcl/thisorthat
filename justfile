db-start:
    cd backend && sudo docker compose up -d

db-stop:
    cd backend && sudo docker compose down

db-reset:
    cd backend && sudo docker compose down -v && sudo docker compose up -d

test:
    echo "Hello from justfile"

install-backend:
    echo "Installing backend..."
    cd backend && uv venv && uv pip install -e ".[dev]"

run-backend-dev-server: db-start
    echo "Running backend server..."
    cd backend && uv run uvicorn src.main:app --reload

run:
    # run dev environment
    just run-backend-dev-server
