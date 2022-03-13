# Dummy Discord Bot + API League of Legends

This bot has been develop to set a base to create any kind of discord bot. The main file of the project allows to create the number of bots the user deserve and with different functionalities by executing each one at independant threads.

In this case, the bot has been created to make requests to the API of League of Legends and create an easy way to check how the registered members are doing into the game.

## User guide

First step is to download this folder and make sure having installed:

- Python 3
- Cassiopeia (https://github.com/meraki-analytics/cassiopeia)
- Discord (https://github.com/Rapptz/discord.py)
  
It is also needed an API Discord key and an API League of Legends key:

- Link to get Discord key (https://discord.com/developers/applications)
- Link to get LOL key (https://developer.riotgames.com/)

### Configuration

Open the file macros.py. At class admin, fill empty fields:

- REGION: Server where the members play to League of Legends
- APILOLKEY: Generated key from League of Legends developer page
- ADMIN: Discord name of the user will be clasified as administrator in the discord bot
- DEFAULT_CHANNEL: Discord text channel the bot will use as default

Then, open .env file:

- DISCORD_TOKEN: Add token generated at Discord developer page

Before launching the bot, it is needed to add the images of the folder apiLol/ranked-icons as icons into the discord server manually.

The tool is ready to be executed. Launch file main.py

All information collected by the bot will be saved at server_config.json