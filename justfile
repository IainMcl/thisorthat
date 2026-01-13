test:
    echo "Hello from justfile"

install-backend:
    echo "Installing backend..."
    cd backend && uv venv && uv pip install -e ".[dev]"

run-backend-dev-server:
    echo "Running backend server..."
    cd backend && uv run fastapi dev src/main.py

run:
    # run dev environment
    just run-backend-dev-server
