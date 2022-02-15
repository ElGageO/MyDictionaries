ws_winners_file = open('WorldSeriesWinners.txt', 'r')

winners_file_list = list(ws_winners_file)
ws_winners = []
for line in winners_file_list:
    team = line.rstrip()
    ws_winners.append(team)

win_counter = {}

for team in ws_winners:
    win_count = ws_winners.count(team)
    win_counter[team] = win_count

year_winner = {}
year = 1903

for num in range(0, len(ws_winners)):
    year_winner[year] = ws_winners[num]
    year += 1

user_selection = int(input('\nPlease enter a year: '))
while user_selection not in range(1903, 2009):
    user_selection = (int(input('\nThat is not a valid year. Please enter a year: ')))

print('\nThe', user_selection, 'World Series was won by the', year_winner[user_selection])
print('The', year_winner[user_selection], 'have won the World Series', win_counter[year_winner[user_selection]], 'time(s)\n')
