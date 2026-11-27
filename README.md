
# RECLAIM - Route Recommendation Exercise

## Project Description

This project is part of the RECLAIM predoctoral training program.

It recommends routes based on travel time and PM2.5 air pollution levels.

The user can choose a less polluted route within an acceptable extra travel time and decide whether to remember this preference for the next journey.

## Project Structure

- `src/exercise.py`: Main project functions and route recommendation.
- `src/routes.csv`: Route data.
- `src/feedback.csv`: User preferences.
- `tests/`: Automated tests.
- `requirements.txt`: Project dependencies.

## Installation

Clone the repository:

```bash
git clone https://github.com/meryh-cell/reclaim-predoc.git
cd reclaim-predoc
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python src/exercise.py
```

## Run Tests

```bash
python -m pytest -v
```
