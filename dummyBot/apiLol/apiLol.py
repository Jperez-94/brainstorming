import json
import cassiopeia as cass

APIKEY = ""
REGION = ""

class ApiLol():

    def __init__(self):
        self._json_filepath = f'{__file__[0:__file__.find("apiLol.py")]}..\server_config.json'
        self._data_json = ""
        self.keyAPILol = cass.set_riot_api_key(APIKEY)
        self.parser_json()
    
    def parser_json(self):
        with open(self._json_filepath) as file:
            self._data_json = json.load(file)

        file.close()

    def update_json(self):
        with open(self._json_filepath, 'w') as file:
            json.dump(self._data_json, file, indent= 4)

        file.close()
        self.parser_json()

    def updateSummoner(self, message) -> bool:
        discord_member = message.author.name
        summoner = message.content[len('!addmylol') + 1:len(message.content)]
        # añadir check de que existe el summonerName, si existe guardar la info relevante. Si no, mensaje de error
        try:
            summoner_data = self._getSummoner(summoner)
            self._data_json['Members'][discord_member]['summoner'] = {}
            self._data_json['Members'][discord_member]['summoner']['name'] = summoner_data.name
            self._data_json['Members'][discord_member]['summoner']['id'] = summoner_data.id
            self._data_json['Members'][discord_member]['summoner']['accountid'] = summoner_data.account_id
            self._data_json['Members'][discord_member]['summoner']['puuid'] = summoner_data.puuid
            self.update_json()
            return True
        except:
            return False
    
    def updateSummonerInfo(self, discord_member) -> bool:
        print(discord_member)
        summoner = cass.Summoner(
            id= self._data_json['Members'][discord_member]['summoner']['id'],
            account_id= self._data_json['Members'][discord_member]['summoner']['accountid'],
            name= self._data_json['Members'][discord_member]['summoner']['name'],
            region=REGION)
        try:
            summoner_entries = cass.get_league_entries(summoner)
            summoner_5x5_data = summoner_entries.fives()
            self._data_json['Members'][discord_member]['summoner']['tier'] = str(summoner_5x5_data.tier)
            self._data_json['Members'][discord_member]['summoner']['division'] = str(summoner_5x5_data.division)
            self._data_json['Members'][discord_member]['summoner']['league_points'] = str(summoner_5x5_data.league_points)
            self._data_json['Members'][discord_member]['summoner']['wins'] = str(summoner_5x5_data.wins)
            self._data_json['Members'][discord_member]['summoner']['losses'] = str(summoner_5x5_data.losses)
            self.update_json()
            return True
        except:
            return False

    def rankMembers(self) -> list:
        _summoners_rank = []
        self.parser_json()
        for member in self._data_json['Members']:
            if "summoner" in self._data_json['Members'][member].keys():
                # self.updateSummonerInfo(member)
                _summoners_rank.append(self._data_json['Members'][member]['summoner'])
        
        summoners_rank = []
        for tier in self._order_rank(_summoners_rank):
            if len(tier) != 0:
                for summoner in tier:
                    summoners_rank.append([summoner['name'], summoner['tier'], summoner['division']])
        
        return summoners_rank

    def _order_rank(self, summoners_info) -> list:
        ordered_summs = []
        ligas = ['Challenger', 'GrandMaster', 'Master', 'Diamond', 'Platinum', 'Gold', 'Silver', 'Bronze', 'Iron']
        divisiones = ['I', 'II', 'III', 'IV']

        for tier in ligas:
            ordered_tier = []
            ordered_tier.append(self._order_by_tier(summoners_info, tier))
            for division in divisiones:
                ordered_summs.append(self._order_by_division(ordered_tier, division))
        
        return ordered_summs
        
    def _order_by_tier(self, summoners_info, tier) -> list:
        ordered_tier = []
        for summoner in summoners_info:
            if summoner['tier'] == tier:
                ordered_tier.append(summoner)
        
        return ordered_tier

    def _order_by_division(self, summoners_info, division) -> list:
        ordered_division = []
        for summoner in summoners_info[0]:
            if len(summoner) != 0:
                if summoner['division'] == division:
                    ordered_division.append(summoner)
        
        return ordered_division

    def _getSummoner(self, summoner) -> cass.Summoner:
        return cass.get_summoner(name= summoner, region= REGION)
