import apicaller
import staticdata

apikey = 'fa3518a3-2076-40e9-adfd-2f19bf27a502'

print('Loading champions')
staticdata.load_champions('euw', apikey)
print('Loaded {total} champions'.format(total=staticdata.get_champion_count()))

while True:
    name = input('Enter name: ')
    region = input('Enter region: ')

    summoner = apicaller.get_summoner_by_name(name, region, apikey)
    print(summoner.get_revision_date(formated=True))
    print(summoner.get_id())
    data = apicaller.get_league(summoner, apikey)
    if data != None:
        print(data.get_tier(), data.get_divison(), data.get_name(), str(data.get_league_points()) + 'lp')
    else:
        print('Unranked')
    print('')
    apicaller.get_stats_ranked(summoner, apikey)
    
    games = apicaller.get_game_data(summoner, apikey)
    for i in range(games.get_game_count()):
        game = games.get_game(i)
        print('Match Type:', game.get_sub_type(), 'Win:', game.get_win())
        print(game.get_time_started(formatted=True), 'for', game.get_length(formatted=True))
        print('    Champion |', game.get_champion())
        print('    K/D/A |', str(game.get_kills()) + '/' + str(game.get_deaths()) + '/' + str(game.get_assists()))
        print('    KDA |', round(game.get_kda(), 2))
        print('    Minions Killed |', game.get_farm())
        print('    Monsters Killed |', game.get_jungle_farm())
    print('')
