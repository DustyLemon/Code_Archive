import urllib.request
import json
import objects

def get_base_address(region):
    return 'https://{region}.api.pvp.net/api/lol/{region}/'.format(region=region)

def get_end_point(apikey,otherargs=False):
    if otherargs:
        return '&api_key={apikey}'.format(apikey=apikey)
    else:
        return '?api_key={apikey}'.format(apikey=apikey)

def get_error_message(code):
    if code == 400:
        return 'Bad request'
    elif code == 401:
        return 'Unauthorized'
    elif code == 404:
        return 'No summoner data found for any specified inputs'
    elif code == 429:
        return 'Rate limit exceeded'
    elif code == 500:
        return 'Internal server error'
    elif code == 503:
        return 'Service unavailable'
    return ''

def request_raw(url):
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        the_page = response.read()

        return str(the_page, 'UTF-8')
    except urllib.error.HTTPError as e:
        pass
        #print('-'*50)
        #print(e.code, get_error_message(e.code))
        #print('-'*50)

    return None

def request_json(url):
    try:
        json_data = request_raw(url)
        if json_data == None:
            return None
        
        data = json.loads(json_data)
        return data
    except ValueError:
        pass
        #print('-'*50)
        #print('Invalid json data')
        #print('-'*50)

def format_json(data):
    return json.dumps(data, indent=4)

def get_champions(region, apikey):
    data = request_json('https://global.api.pvp.net/api/lol/static-data/{region}/v1.2/champion'.format(region=region) + get_end_point(apikey))
    return data

def get_regions():
    data = request_json('http://status.leagueoflegends.com/shards')
    return data

def get_summoner_by_name(name, region, apikey):
    data = request_json(get_base_address(region) + 'v1.4/summoner/by-name/{name}'.format(name=name) + get_end_point(apikey))
    if data == None:
        return None
    return objects.summoner(name, region, data)

def get_league(summoner, apikey):
    data = request_json(get_base_address(summoner.get_region()) + 'v2.5/league/by-summoner/{summonerId}'.format(summonerId=summoner.get_id()) + get_end_point(apikey))
    if data == None:
        return None
    return objects.league(summoner, data)

def get_match_history(summoner, apikey):
    data = request_json(get_base_address(summoner.get_region()) + 'v2.2/matchhistory/{summonerId}'.format(summonerId=summoner.get_id()) + get_end_point(apikey))
    if data == None:
        return None
    return objects.matchhistory(summoner, data)

def get_game_data(summoner, apikey):
    data = request_json(get_base_address(summoner.get_region()) + 'v1.3/game/by-summoner/{summonerId}/recent'.format(summonerId=summoner.get_id()) + get_end_point(apikey))
    if data == None:
        return None
    return objects.gamelist(summoner, data)

def get_stats_ranked(summoner, apikey):
    data = request_json(get_base_address(summoner.get_region()) + 'v1.3/stats/by-summoner/{summonerId}/ranked'.format(summonerId=summoner.get_id()) + get_end_point(apikey))
    print(format_json(data))
    if data == None:
        return None
    return objects.stats(summoner, data)

def get_test(summoner, apikey):
    data = request_json(get_base_address(summoner.get_region()) + 'v2.2/match/{matchId}'.format(matchId=summoner.get_id()) + get_end_point(apikey))
    print(format_json(data))
    if data == None:
        return None
    return objects.stats(summoner, data)

#print(json.dumps(request_json('https://euw.api.pvp.net/api/lol/euw/v2.2/matchhistory/46839375?rankedQueues=RANKED_SOLO_5x5&api_key=fa3518a3-2076-40e9-adfd-2f19bf27a502'), indent=4))
