


def get_result(final_score):
    if final_score["home_score"] < final_score["away_score"]:
        return "away win"
    elif final_score["home_score"] > final_score["away_score"]:
        return "home win"
    else: 
        return "draw"
    


def get_results(score1, score2, score3):
    results_list = []
    score1 = get_result(score1)
    score2 = get_result(score2)
    score3 = get_result(score3)
    results_list.append(score1)
    results_list.append(score2)
    results_list.append(score3)
    return results_list
    

    
    
# (You could try and use a list comprehension for this)

    