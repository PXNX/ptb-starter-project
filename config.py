import os

##########################################
# this file contains all the configurations and variables used throughout the bot.
##########################################

PORT = int(os.environ.get('PORT', 5000))

# The token @botfather sent you goes here, for example 133769420:AndHereGoe4ssomEL0ngT3xtWoHo0o
# if using heroku: os.environ['TOKEN'] and you'll have to add your token to Heroku's config vars then
TOKEN = 'YOUR-TOKEN-GOES-HERE'

# ID of the group you want errors to be posted in, for example -1001336914977
ERROR_GROUP = -1234

# IDs of users you want to allow certain actions, for example 1039999701, 1039999702
VERIFIED_USERS = (1039999701, 1039999702)
