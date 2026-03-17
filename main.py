from fetch import get_batting_data
import score

from visualize import make_scatter_plot, make_luck_graph

year = input("Enter season year: ")
batting_data, means, stdevs = get_batting_data(year)


z_scores = score.z_score_stats(batting_data, means, stdevs)

#Adds Skill+, Outcome+ and Luck stats to the DataFrame
z_scores['Skill+'] = z_scores.apply(score.generate_skill_scores, axis=1)
z_scores['Outcome+'] = z_scores.apply(score.generate_outcome_scores, axis=1)
z_scores['Luck'] = z_scores['Outcome+'] - z_scores['Skill+']
luck_sorted = z_scores[['Name', 'Luck']].sort_values('Luck', ascending=True)


make_scatter_plot(z_scores)
make_luck_graph(luck_sorted)