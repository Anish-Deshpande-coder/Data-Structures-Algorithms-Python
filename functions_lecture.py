def calculate_match_points(goals_scored, goals_conceded):
    match = ""
    if goals_scored > goals_conceded:
        return 3
    elif goals_scored == goals_conceded:
        return 1
    else:
        return 0

def add_match_result(points, result):
    return points + result


def main():
    season_points = 0
    season_points = add_match_result(season_points, calculate_match_points(2,1))
    season_points = add_match_result(season_points, calculate_match_points(0,0))
    season_points = add_match_result(season_points, calculate_match_points(1,3))
    season_points = add_match_result(season_points, calculate_match_points(3,2))
    print(season_points)
main()