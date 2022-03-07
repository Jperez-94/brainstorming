import cassiopeia as cass
from macros import json_key, commands, tiers, divisions

APIKEY = ""
REGION = ""

class ApiLol():

    def __init__(self):
        self._data_json = ""
        self.keyAPILol = cass.set_riot_api_key(APIKEY)

    def updateSummoner(self, message) -> bool:
        discord_member = message.author.name
        summoner = message.content[len(commands.AddMyLol) + 1:len(message.content)]
        # añadir check de que existe el summonerName, si existe guardar la info relevante. Si no, mensaje de error
        try:
            summoner_data = self._getSummoner(summoner)

            self._data_json[json_key.Members][discord_member][json_key.Summoner] = {}
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Name] = summoner_data.name
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Id] = summoner_data.id
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.AccountId] = summoner_data.account_id
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Puuid] = summoner_data.puuid

            return True
        except:
            return False
    
    def updateSummonerInfo(self, discord_member) -> bool:
        summoner = cass.Summoner(
            name = self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Name],
            region = REGION)
        try:
            summoner_entries = cass.get_league_entries(summoner)
            summoner_5x5_data = summoner_entries.fives()
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Tier] = str(summoner_5x5_data.tier)
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Division] = str(summoner_5x5_data.division)
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.LeaguePoints] = str(summoner_5x5_data.league_points)
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Wins] = str(summoner_5x5_data.wins)
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Losses] = str(summoner_5x5_data.losses)

            return True
        except:
            return False

    def rankMembers(self) -> list:
        _summoners_rank = []
        for member in self._data_json[json_key.Members]:
            if json_key.Summoner in self._data_json[json_key.Members][member].keys():
                self.updateSummonerInfo(member)
                _summoners_rank.append(self._data_json[json_key.Members][member][json_key.Summoner])
        
        summoners_rank = []
        for tier in self._order_rank(_summoners_rank):
            if len(tier) != 0:
                for summoner in tier:
                    summoners_rank.append([
                        summoner[json_key.Name],
                        summoner[json_key.Tier],
                        summoner[json_key.Division],
                        summoner[json_key.Wins],
                        summoner[json_key.Losses]]
                    )
        
        return summoners_rank

    def _order_rank(self, summoners_info) -> list:
        ordered_summs = []
        divisiones = ['I', 'II', 'III', 'IV']

        for tier in tiers.Tier_List:
            ordered_tier = []
            ordered_tier.append(self._order_by_tier(summoners_info, tier))
            for division in divisions.Division_List:
                ordered_summs.append(self._order_by_division(ordered_tier, division))
        
        return ordered_summs
        
    def _order_by_tier(self, summoners_info, tier) -> list:
        ordered_tier = []
        for summoner in summoners_info:
            if summoner[json_key.Tier] == tier:
                ordered_tier.append(summoner)
        
        return ordered_tier

    def _order_by_division(self, summoners_info, division) -> list:
        ordered_division = []
        for summoner in summoners_info[0]:
            if len(summoner) != 0:
                if summoner[json_key.Division] == division:
                    ordered_division.append(summoner)
        
        return ordered_division

    def _getSummoner(self, summoner) -> cass.Summoner:
        return cass.get_summoner(name= summoner, region= REGION)
