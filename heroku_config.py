import os

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 1516656))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "d9e0d8d4268862852c7ca848de66ccc7")
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BJWap1sBux_6lv3sq5aqcl54L2quFJs79p-1XnC2qncRUsojk_8zE3UAeP1qEuv2Eiwn9PA1IGWenOQSL9_cZDQmNVZYt6nYqaJrfCz9O_VRndXiBs6vnw5L2SFVy5WiR8O2JRu7hrfBTwXBb6BACk5WHo_nb-TK4A4Xqva7kHg-9wpyxhWpcDIFJ8aGqU7TAnJsO1959-deKdXAJTN_fIJ0T8Dc5En0_swaSN-hRRxgylXSGKB2CmfUR0EycaazpgzQ_bdmAHHrfUECY90zgVWjGXnDyT3to7S5QQF1mUeg0V0xXxujYeJig3GQh6fMQeJcTgCQovP-Q2Po22ZJRCli7Xq3rVI=)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1306336056").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    # Get your own API key from https://www.remove.bg/ or
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    # define "spam" in PMs
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    # Send .get_id in any channel to fill this value.
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -100))
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    if AUTH_TOKEN_DATA != None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
    if PRIVATE_GROUP_ID != None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError("Private Group ID invalido. Il tuo ID deve iniziare con -100 e dopo il chat id.")

class Development(Var):
    LOGGER = True
    # Here for later purposes
