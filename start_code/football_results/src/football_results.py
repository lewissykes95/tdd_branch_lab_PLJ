
def get_result(final_score):
    if final_score["home_score"] < final_score["away_score"]:
        return "away win"
    elif final_score["home_score"] > final_score["away_score"]:
        return "home win"
    else: 
        return "draw"
    
    

# def get_results(final_scores):
#     pass
#     # (You could try and use a list comprehension for this)