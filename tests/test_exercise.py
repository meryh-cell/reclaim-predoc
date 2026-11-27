
import pandas as pd

from src.exercise import find_best_route


def test_find_best_route():
    routes = pd.DataFrame([
        {
            "journey_id": "J01",
            "route_id": "R1",
            "duration_min": 20,
            "pm25_ug_m3": 30
        },
        {
            "journey_id": "J01",
            "route_id": "R2",
            "duration_min": 23,
            "pm25_ug_m3": 10
        },
        {
            "journey_id": "J01",
            "route_id": "R3",
            "duration_min": 27,
            "pm25_ug_m3": 5
        }
    ])
      
    fastest, best = find_best_route(routes, "J01", 5)

    assert fastest["route_id"] == "R1"
    assert best["route_id"] == "R2"


def test_journey_not_found():
    routes = pd.DataFrame([
        {
            "journey_id": "J01",
            "route_id": "R1",
            "duration_min": 20,
            "pm25_ug_m3": 30
        }
    ])

    result = find_best_route(routes, "J99", 5)

    assert result is None

from pathlib import Path
from src.exercise import load_data

def test_load_real_csv_files():
    project_root = Path(__file__).resolve().parents[1]

    routes_path = project_root / "src" / "routes.csv"
    feedback_path = project_root / "src" / "feedback.csv"

    routes, feedback = load_data(
        routes_path,
        feedback_path
    )

    assert not routes.empty
    assert not feedback.empty

    assert "journey_id" in routes.columns
    assert "route_id" in routes.columns
    assert "duration_min" in routes.columns
    assert "pm25_ug_m3" in routes.columns

    assert "after_journey_id" in feedback.columns
def test_find_best_route_with_real_data():
    project_root = Path(__file__).resolve().parents[1]

    routes_path = project_root / "src" / "routes.csv"
    routes, _ = load_data(routes_path, project_root / "src" / "feedback.csv")

    fastest, best = find_best_route(routes, "J01", 8)

    assert fastest["route_id"] == "J01_A"
    assert best["route_id"] == "J01_C"



def test_remember_preference():
        project_root = Path(__file__).resolve().parents[1]
        
        routes_path = project_root / "src" / "routes.csv"
        routes, _ = load_data(routes_path, project_root / "src" / "feedback.csv")
        routes = pd.DataFrame([
        {"journey_id": "J02", "route_id": "J02_A", "duration_min": 12, "pm25_ug_m3": 25},
        {"journey_id": "J02", "route_id": "J02_B", "duration_min": 17, "pm25_ug_m3": 14},
    ])

        # Without remembering the preference: choose the fastest route
        _, without_memory = find_best_route(routes, "J02", 0)
        assert without_memory["route_id"] == "J02_A"

        # With remembering the preference: choose the cleaner route
        _, with_memory = find_best_route(routes, "J02", 5)
        assert with_memory["route_id"] == "J02_B"