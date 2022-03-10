
class admin():
    REGION = ""
    APILOLKEY = ""
    ADMIN = ''
    DEFAULT_CHANNEL = ''
    BOT_FILE = "bot.py"
    JSON_FILE = "server_config.json"

class json_key():
    Members = "Members"
    TextChannels = "TextChannels"
    VoiceChannels = "VoiceChannels"
    Name = "name"
    Id = "id"
    Summoner = "summoner"
    AccountId = "accountid"
    Puuid = "puuid"
    Icon = 'icon'
    Tier = "tier"
    Division = "division"
    LeaguePoints = "league_points"
    Wins = "wins"
    Losses = "losses"

class commands():
    NewMember = "!newmember"
    Close = "!close"
    AddMyLol = "!addmylol"
    Rank = "!rank"
    MyLol = "!mylol"
    Commands = "!commands"

    Command_List = [
        NewMember,
        AddMyLol,
        Rank,
        MyLol,
        Close,
        Commands
    ]

    Restrict_List =[
        Close,
        Commands
    ]

class tiers():
    _Challenger = "Challenger"
    _GrandMaster = "GrandMaster"
    _Master = "Master"
    _Diamond = "Diamond"
    _Platinum = "Platinum"
    _Gold = "Gold"
    _Silver = "Silver"
    _Bronze = "Bronze"
    _Iron = "Iron"
    _Unranked = "Unranked"

    Tier_List = [
        _Challenger,
        _GrandMaster,
        _Master,
        _Diamond,
        _Platinum,
        _Gold,
        _Silver,
        _Bronze,
        _Iron,
        _Unranked
    ]

class divisions():
    _I = "I"
    _II = "II"
    _III = "III"
    _IV = "IV"

    Division_List = [
        _I,
        _II,
        _III,
        _IV
    ]

class messages():
    on_ready = 'Hola holita, ya estamos por aquí!'
    notKnowMember = 'Hola bananita, todavia no nos conocemos. Escribe !newmember para registrarte monete!'
    close = 'Se acabó la diversion!'
    default = 'Hola holita bananita!\n\n Comandos:\n    ->!addmylol nombreInvocador\n   ->!mylol\n  ->!rank'
    restricFeature = 'Bananita! Parece que no sabes que botón tienes que pulsar'
    alreadyRegistered = '{}, ya tenías casa en esta jungla! Ya puedes usar las funcionalidades de League of Legends, lo primero es registrar tu nombre de invocador. Escribe !addmylol [nombreInvocador]'
    welcomeNewMember = 'Bienvenido a la jungla {}! Si quieres acceder a las funcionalidades de League of Leagends, añade tu nombre de invocador escribiendo !addmylol [nombreInvocador]'
    badCommandFormat = 'Te falta un espacio despues del comando bananita!'
    checkSummonerDefault = 'Uuuuh bananita! Veamos si eres un intrépido invocador...\n'
    summonerFound = '\nInteresante bananita, estás en {} {}'
    summonerNotRanked = '\nOh oh bananita! Parece que aun no tienes clasificación'
    summonerNotFound = 'Algo ha salido mal bananita! Revisa que has escrito bien tu nombre de invocador'
    introRank = "Veamos como va el ranking bananita:\n"
    rankMessage = "            {} {} está en {} {}\n"
    rankUnable = 'Vaya bananita! No hay ningún invocador registrado o con rango conseguido'
    summonerNotRegistered = "Vaya bananita! No te tengo guardado como un intrépido invocador. Para acceder a comandos de League of Legends escribe !addmylol [Nombre de invocador]"
    allCommands = """
    ############################################################
    Listado de comandos completo
    ############################################################
    !newmember
    !addmylol
    !mylol
    !rank
    !commands
    !close
    """
