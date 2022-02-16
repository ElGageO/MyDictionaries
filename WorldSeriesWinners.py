ws_winners_file = open('WorldSeriesWinners.txt', 'r')

ws_winners = []
for line in ws_winners_file:
    team = line.rstrip()
    ws_winners.append(team)

win_counter = {}
win_years = {}

for team in ws_winners:
    win_count = ws_winners.count(team)
    win_counter[team] = win_count

year = 1903

for team in ws_winners:
    win_years[year] = team
    year += 1
    if year == 1904 or year == 1994:
        win_years[year] = 'No World Series played'
        year += 1

user_selection = int(input('\nPlease enter a year: '))
if user_selection not in range(1903, 2009):
    user_selection = int(input('\nThat is not a valid year. Please enter a year: '))
print('\n', user_selection, ' World Series winner: ', win_years[user_selection], sep = '')
if user_selection != 1904 and user_selection != 1994:
    print('World Series wins for ', win_years[user_selection], ': ', win_counter[win_years[user_selection]], '\n', sep = '')
