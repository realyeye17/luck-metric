import pybaseball

def get_batting_data(year):
    #Finds the following stats for hitters with 350 plate appearances
    batting_stats = pybaseball.batting_stats(year, qual = 350)
    stat_list = ['Name', 'AVG+', 'BB%+', 'K%+', 'BABIP+', 'ISO+', 
                                     'SLG+', 'OBP+', 'wOBA', 'wRC+', 'wRAA', 'xBA', 'xSLG', 
                                     'xwOBA', 'Contact%', 'LD+%', 'Hard%+', 'Soft%+', 'EV', 'Barrel%', 
                                     'maxEV', 'HR/FB%+', 'O-Swing%', 'Z-Contact%', 'Z-Swing%', 'SwStr%']
    
    stat_list_numbers = [stat for stat in stat_list if stat != 'Name']

    #condensed_stats makes a new DataFrame only including the stats listed above
    condensed_stats = batting_stats[stat_list]
    #Finds the means and standard deviation of each stat and returns them in a dictionary
    means = {stat: condensed_stats[stat].mean() for stat in stat_list_numbers}
    stdev = {stat: condensed_stats[stat].std() for stat in stat_list_numbers}

    return condensed_stats, means, stdev