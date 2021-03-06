import cassiopeia as cass
from macros import json_key, commands, tiers, divisions, admin, messages


class ApiLol():

    def __init__(self):
        self._data_json = ""
        self.keyAPILol = cass.set_riot_api_key(admin.APILOLKEY)
        self.Icons = list()

    def updateSummoner(self, message) -> bool:
        discord_member = message.author.name
        summoner = message.content[len(commands.AddMyLol) + 1:len(message.content)]
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
            region = admin.REGION)
        try:
            summoner_entries = cass.get_league_entries(summoner)
            summoner_5x5_data = summoner_entries.fives()
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Icon] = self._get_tier_icon(str(summoner_5x5_data.tier))
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Tier] = str(summoner_5x5_data.tier)
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Division] = str(summoner_5x5_data.division)
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.LeaguePoints] = str(summoner_5x5_data.league_points)
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Wins] = str(summoner_5x5_data.wins)
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Losses] = str(summoner_5x5_data.losses)

            return True
        except:
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Icon] = self._get_tier_icon(tiers._Unranked)
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Tier] = tiers._Unranked
            self._data_json[json_key.Members][discord_member][json_key.Summoner][json_key.Division] = ""
            
            return False

    def rankMembers(self) -> list:
        _summoners_rank = []
        _unranked = []
        for member in self._data_json[json_key.Members]:
            if json_key.Summoner in self._data_json[json_key.Members][member].keys():
                self.updateSummonerInfo(member)
                if self._data_json[json_key.Members][member][json_key.Summoner][json_key.Tier] == tiers._Unranked:
                    _unranked.append(self._data_json[json_key.Members][member][json_key.Summoner])
                else:
                    _summoners_rank.append(self._data_json[json_key.Members][member][json_key.Summoner])

        summoners_rank = []
        _order_summoners = self._order_rank(_summoners_rank)
        _order_summoners.append(_unranked)

        for tier in _order_summoners:
            if len(tier) != 0:
                for summoner in tier:
                    if summoner[json_key.Tier] != tiers._Unranked:
                        summoners_rank.append([
                            summoner[json_key.Icon],
                            summoner[json_key.Name],
                            summoner[json_key.Tier],
                            summoner[json_key.Division],
                            summoner[json_key.Wins],
                            summoner[json_key.Losses]]
                        )
                    else:
                        summoners_rank.append([
                            summoner[json_key.Icon],
                            summoner[json_key.Name],
                            summoner[json_key.Tier],
                            "",
                            "",
                            ""]
                        )

        return summoners_rank

    def get_summoner_stadistics(self, discord_member) -> str:
        if json_key.Summoner not in self._data_json[json_key.Members][discord_member].keys():
            return messages.summonerNotRegistered

        summoner = self._data_json[json_key.Members][discord_member][json_key.Summoner]
        if summoner[json_key.Tier] != tiers._Unranked:
            message = f"""
            Invocador: {summoner[json_key.Name]}
                Rank: {summoner[json_key.Tier]} {summoner[json_key.Division]} {self.Icons[summoner[json_key.Icon]]}

                                        {summoner[json_key.LeaguePoints]} LP


                                VICTORIAS: {summoner[json_key.Wins]}
                                DERROTAS: {summoner[json_key.Losses]}


            """
        else:
            message = f"""
            Invocador: {summoner[json_key.Name]}
                Rank: {summoner[json_key.Tier]}  {self.Icons[summoner[json_key.Icon]]}

                                        0 LP


                    VICTORIAS: 0 bananitas
                    DERROTAS: 0 bananitas


            """
        return message

    def _order_rank(self, summoners_info) -> list:
        ordered_summs = []
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

    def _get_tier_icon(self, rank_name) -> int:
        for i in range(len(self.Icons)):
            if self.Icons[i].name == rank_name:
                return i

    def _getSummoner(self, summoner) -> cass.Summoner:
        return cass.get_summoner(name= summoner, region= admin.REGION)
