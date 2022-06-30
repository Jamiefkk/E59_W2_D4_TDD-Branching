# class FootballResults:

def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"
    elif final_score["away_score"] > final_score["home_score"]:
        return "Away win"
    else:
        return "Draw"

def get_results(results):
    final_results = []
    for result in results:
        final_results.append(get_result(result))
    
    return final_results

    # final_score
    # if final_score:
    #     return "Home win"
# "home_score": 0,
#     "away_score": 1
# def get_results(final_scores):
#     pass
#     # (You could try and use a list comprehension for this)