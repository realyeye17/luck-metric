import pandas as pd

def z_score(value, mean, stdev):
    #Returns a z-score for any metric inputted
    return ((value-mean)/stdev)


def scaled_z_score(value, mean, stdev):
    #Scales metric to 100
    return 100 + (z_score(value, mean, stdev)*25)

def inverse_scaled_z_score(value, mean, stdev):
    #Scales metric to 100 (backwards for stats where lower is better)
    return 100 - (z_score(value, mean, stdev)*25)

def z_score_stats(data, means, stdevs):
    #Inverse stats list shows which stats are "better" when they are lower
    inverse_stats = ['K%+', 'SwStr%', 'O-Swing%', 'Soft%+']
    z_scores = pd.DataFrame()
    z_scores['Name'] = data['Name']

    stat_list = data.columns.drop('Name')

    for stat in stat_list:
        if stat in inverse_stats:
            z_scores[stat] = inverse_scaled_z_score(data[stat], means[stat], stdevs[stat])
        else:
            z_scores[stat] = scaled_z_score(data[stat], means[stat], stdevs[stat])

    return z_scores

def generate_skill_scores(batting_data):
    score = 0
    skill_weights = {'xwOBA': 0.22, 'xSLG': 0.18, 'Barrel%': 0.12, 'EV': 0.08,
    'xBA': 0.18, 'LD+%': 0.07, 'Hard%+': 0.07,
    'O-Swing%': 0.04, 'Z-Swing%': 0.04}

    #Weighting Methodology:
    #Power: 60% weight
    #xWOBA 22%, xSLG 18%, Barrel% 12%, EV 8%
    #Contact/Batted Ball Skills: 32%
    #xBA 18%, LD+% 7%, Hard%+ 7% -> Hard contact% could also be considered a power metric
    #Discipline Skills: 8% weight
    #O-Swing/Chase% 4%, Z-Swing%+ 4%

    for stat in skill_weights:
        score += batting_data[stat] * skill_weights[stat] 
    return score


def generate_outcome_scores(batting_data):
    score = 0
    batting_weights = {'wRC+': 0.22, 'ISO+': 0.18, 'SLG+': 0.12, 'wOBA': 0.08,
    'AVG+': 0.18, 'BABIP+': 0.07, 'OBP+': 0.08,
    'BB%+': 0.04, 'K%+': 0.03}

    #Weighting Methodology
    #Run Production: 60% weight
    #wRC+ 22%, ISO+ 18%, SLG+ 12%, wOBA 8%
    #Average/On Base: 33% weight
    #AVG+ 18%, BABIP+ 7%, OBP+ 8%
    #Plate Discipline: BB% 4%, K% 3%

    for stat in batting_weights:
        score += batting_data[stat] * batting_weights[stat]

    return score
    