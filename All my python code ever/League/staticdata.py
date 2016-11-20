import apicaller

champion_id = {}
id_champion = {}
champion_count = 0
regions = ['BR', 'EUNE', 'EUW', 'KR', 'LAS', 'LAN', 'NA', 'OCE', 'TR', 'RU']
regions_lower = [region.lower() for region in regions]
tiers = {'BRONZE':'Bronze', 'SILVER':'Silver', 'GOLD':'Gold', 'PLATINUM':'Platinum', 'DIAMOND':'Diamond', 'MASTER':'Master', 'CHALLENGER':'Challenger'}

def load_champions(region, apikey):
    global champion_count
    champions = apicaller.get_champions(region, apikey)

    for champion_name in champions['data']:
        champion = champions['data'][champion_name]
        
        champion_id[champion['name']] = champion['id']
        id_champion[champion['id']] = champion['name']
        
        champion_count += 1

def get_champion_from_id(championid):
    return id_champion[championid]

def get_id_from_champion(champion):
    return champion_id[champion]

def get_champion_count():
    return champion_count

def get_regions():
    return regions

def get_tiers():
    return tiers

def get_tier(tier):
    return tiers[tier]

def get_regions_lower():
    return regions_lower

def get_region_count():
    return len(regions)
