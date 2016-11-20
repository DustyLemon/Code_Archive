import datetime
import json
import staticdata

class summoner():

    def __init__(self, name, region, data):
        self.name = name
        self.region = region
        self.data = data

    def __str__(self):
        return json.dumps(self.data, indent=4)

    def get_data(self):
        return self.data

    def get_name(self):
        return self.name

    def get_region(self):
        return self.region

    def get_name_in_game(self):
        return self.data[self.name]['name']

    def get_profile_icon_id(self):
        return self.data[self.name]['profileIconId']

    def get_id(self):
        return self.data[self.name]['id']

    def get_revision_date(self, formated=False):  
        revisiondate = self.data[self.name]['revisionDate']
        if formated:
            return datetime.datetime.fromtimestamp(revisiondate / 1000).strftime('%d-%m-%Y %H:%M:%S')
        return revisiondate

    def get_summoner_level(self):
        return self.data[self.name]['summonerLevel']

class league():

    def __init__(self, summoner, data):
        self.summoner = summoner
        self.data = data

    def get_data(self):
        return self.data

    def get_tier(self):
        if self.summoner.get_summoner_level() < 30:
            return 'Unranked'
        
        return staticdata.get_tier(self.data[str(self.summoner.get_id())][0]['tier'])

    def get_divison(self):
        if self.summoner.get_summoner_level() < 30:
            return ''

        for entry in self.data[str(self.summoner.get_id())][0]['entries']:
            if self.summoner.get_name_in_game() == entry['playerOrTeamName']:
                return entry['division']
        
        return ''

    def get_name(self):
        if self.summoner.get_summoner_level() < 30:
            return ''
        
        return self.data[str(self.summoner.get_id())][0]['name']

    def get_league_points(self):
        if self.summoner.get_summoner_level() < 30:
            return -1

        for entry in self.data[str(self.summoner.get_id())][0]['entries']:
            if self.summoner.get_name_in_game() == entry['playerOrTeamName']:
                return entry['leaguePoints']
        
        return -1
    
    def __str__(self):
        return json.dumps(self.data, indent=4)

class gamelist():

    def __init__(self, summoner, data):
        self.summoner = summoner
        self.data = data

    def get_data(self):
        return self.data

    def get_game_count(self):
        return len(self.data['games'])

    def get_game(self, index):
        return game(self.summoner, self.data['games'][index])
    
    def __str__(self):
        return json.dumps(self.data, indent=4)

class game():

    def __init__(self, summoner, data):
        self.summoner = summoner
        self.data = data

    def get_champion(self):
        return staticdata.get_champion_from_id(self.data['championId'])

    def get_kills(self):
        try:
            return self.data['stats']['championsKilled']
        except KeyError:
            return 0

    def get_deaths(self):
        try:
            return self.data['stats']['numDeaths']
        except KeyError:
            return 0

    def get_assists(self):
        try:
            return self.data['stats']['assists']
        except KeyError:
            return 0

    def get_kda(self):
        if self.get_deaths() == 0:
            return self.get_kills() + self.get_assists()
        return (self.get_kills() + self.get_assists()) / self.get_deaths()

    def get_length(self, formatted=False):  
        timePlayed = self.data['stats']['timePlayed']
        if formatted:
            return datetime.datetime.fromtimestamp(timePlayed).strftime('%H:%M:%S')
        return timePlayed

    def get_time_started(self, formatted=False):  
        timePlayed = self.data['createDate']
        if formatted:
            return datetime.datetime.fromtimestamp(timePlayed/1000).strftime('%d-%m-%Y %H:%M:%S')
        return timePlayed

    def get_sub_type(self):
        return self.data['subType']

    def get_win(self):
        return self.data['stats']['win']

    def get_farm(self):
        return self.data['stats']['minionsKilled']

    def get_jungle_farm(self):
        if 'neutralMinionsKilled' in self.data['stats']:
            return self.data['stats']['neutralMinionsKilled']
        else:
            return 0


    def __str__(self):
        return json.dumps(self.data, indent=4)

class matchhistory():

    def __init__(self, summoner, data):
        self.summoner = summoner
        self.data = data

class match():

    def __init__(self):
        pass
        
