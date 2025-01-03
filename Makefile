# Variables
PYTHON = python3
UVICORN = uvicorn
APP = app.main:app  # Replace with your app's entry point (e.g., filename:FastAPI_instance)

# Targets
.PHONY: setup run clean

setup:  ## Create a virtual environment and install dependencies
    $(PYTHON) -m venv .venv
    . .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

run:  ## Activate the virtual environment and run Uvicorn
    . .venv/bin/activate && $(UVICORN) $(APP) --reload

clean:  ## Remove the virtual environment
    rm -rf .venv
