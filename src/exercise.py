import pandas as pd

def load_data(routes_path='routes.csv', feedback_path='feedback.csv'):
    routes = pd.read_csv(routes_path)
    feedback = pd.read_csv(feedback_path)
    return routes, feedback

def find_best_route(routes, journey_id, max_extra_minutes):
    j_data = routes[routes['journey_id'] == journey_id]
    
    if j_data.empty:
        return None

    fastest = j_data.loc[j_data['duration_min'].idxmin()]
    
    limit_duration = fastest['duration_min'] + max_extra_minutes
    
    eligible = j_data[j_data['duration_min'] <= limit_duration]
    
    best_route = eligible.sort_values(by=['pm25_ug_m3', 'duration_min']).iloc[0]
    
    return fastest, best_route

def main():
    print("--- RECLAIM EXERCISE EXECUTION (Refactored) ---")
    
    
    routes, feedback = load_data()
    max_extra = feedback.loc[0, 'max_extra_minutes']

    j01_fastest, j01_best = find_best_route(routes, 'J01', max_extra)
    print(f"J01 Before Feedback (Fastest): Route {j01_fastest['route_id']}, Duration: {j01_fastest['duration_min']} min, PM2.5: {j01_fastest['pm25_ug_m3']} ug/m3")
    print(f"J01 After Feedback: Route {j01_best['route_id']}, Duration: {j01_best['duration_min']} min, PM2.5: {j01_best['pm25_ug_m3']} ug/m3")

    _, j02_best = find_best_route(routes, 'J02', max_extra)
    print(f"J02 With Stored Preference: Route {j02_best['route_id']}, Duration: {j02_best['duration_min']} min, PM2.5: {j02_best['pm25_ug_m3']} ug/m3")

if __name__ == "__main__":
    main()