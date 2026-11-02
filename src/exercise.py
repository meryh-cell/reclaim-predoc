import pandas as pd


routes = pd.read_csv('routes.csv')
feedback = pd.read_csv('feedback.csv')

print("---  EXERCISE EXECUTION ---")


j01 = routes[routes['journey_id'] == 'J01']
fastest_j01 = j01.loc[j01['duration_min'].idxmin()]
print(f"J01 Before Feedback (Fastest): Route {fastest_j01['route_id']}, Duration: {fastest_j01['duration_min']} min, PM2.5: {fastest_j01['pm25_ug_m3']} ug/m3")


max_extra = feedback.loc[0, 'max_extra_minutes']
limit_j01 = fastest_j01['duration_min'] + max_extra
eligible_j01 = j01[j01['duration_min'] <= limit_j01]
best_j01 = eligible_j01.sort_values(by=['pm25_ug_m3', 'duration_min']).iloc[0]
print(f"J01 After Feedback: Route {best_j01['route_id']}, Duration: {best_j01['duration_min']} min, PM2.5: {best_j01['pm25_ug_m3']} ug/m3")

j02 = routes[routes['journey_id'] == 'J02']
fastest_j02 = j02.loc[j02['duration_min'].idxmin()]
limit_j02 = fastest_j02['duration_min'] + max_extra
eligible_j02 = j02[j02['duration_min'] <= limit_j02]
best_j02 = eligible_j02.sort_values(by=['pm25_ug_m3', 'duration_min']).iloc[0]
print(f"J02 With Stored Preference: Route {best_j02['route_id']}, Duration: {best_j02['duration_min']} min, PM2.5: {best_j02['pm25_ug_m3']} ug/m3")
