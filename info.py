import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 6))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if re.search('^.\d+$', ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if re.search('^\d+$', user) else user for user in environ['AUTH_USERS'].split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
**Halooo! I'm @NinjaNaveen's Config Searcher Bot**

Here you can find all of my Configs for Openbullet in inline mode.
I made it easier for you to find the config you need❣️**

☑️For Requesting Configs and For Reporting Dead Configs in this Bot, Kindly DM @NinjaNaveenBot**
"""

ADMINHELP_MSG = """
/channel
/helpadmin
/total
/logger
/delete
"""

INFO_MSG = """
**Hey there!
I'm made to make it easier for you to find the config you need❣️

Admins:-
@NinjaNaveen
@YourDaddy9999
@Luciferr_xD

Credits for Configs:-
@YourDaddy9999
@Luciferr_xD
@Lucif3rHun
@Python_xD
@Tonami_YT
@sylas_T_H_P
@Guptaajiii

☑️For Requesting Configs and For Reporting Dead Configs in this Bot, Kindly DM @NinjaGiveaways_Bot**
"""

HELP_MSG = """
**🌀 How to Use Me?


🔰Type my Username @NinjaNaveenConfigsBot and you can type the desired config you need.

Example:-** 
     @NinjaNaveenConfigsBot Heroku - Will give Heroku Config


**🔰You can either Type the Name of the Site or you can Use Keywords

Example:- **
     @NinjaNaveenConfigsBot Indian - Will show list of Indian sites configs
     @NinjaNaveenConfigsBot Streaming - Will show list of Streaming sites configs
     @NinjaNaveenConfigsBot Proxyless - Will show list of Proxyless configs


**☑️ For Requesting Configs and For Reporting Dead Configs in this Bot, Kindly DM @NinjaNaveenBot**
"""

SHARE_BUTTON_TEXT = "Yo, Checkout {username}. There you can find all of @NinjaNaveen's Configs for Openbullet in inline mode."
