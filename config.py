import os

##########################################
# this file contains all the configurations and variables used throughout the bot.
##########################################

PORT = int(os.environ.get('PORT', 5000))

# if using heroku: os.environ['TOKEN']
TOKEN = 'YOUR-TOKEN-GOES-HERE'

# ID of the group you want errors to be posted in, eg. -1001336914977
ERROR_GROUP = -1234

# IDs of users you want to allow certain actions, eg. 1039999701, 1039999702
VERIFIED_USERS = ( 1039999701,1039999702)