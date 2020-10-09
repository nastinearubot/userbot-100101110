import os

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 1354863))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "7faa797cba87851ac8533e137ed28186")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBuwLZ72GWtWzNJMVJPGEp-mXj3UCLIjg0XW1E4nGCkDy2ovjeDluLAAXzccNDiHKPYaF4kWXmzO3kPXDz70RM4zMxvpfmKQ-RUMINDEB-wRczZtMyKFdT-slhDsaP7n5hx9S8MT_XahGzNnAaRHk2J6jZoPgbpvcVKh7IVb0eOPLpHZM2hsM6Q7D6_9wXHLB_3lVnH5_1X0TV08IVm-7Ze2wXgc-dhx0HQgYmx-Up80j1Ld-vUpnk_y9bgq3azYPpFP4gXYNsZ260M4Bqa1z2bOVWjoziwMJ53ueNhi9Wjm4YiyqzxAU70p0zJ7882tEyuXeJ42jocZQfDmpSGsmDLRY=")
    DB_URI = os.environ.get("DATABASE_URL", "postgres://ofcnipdqfpiizo:13f750b0845153527640824a41d2ce49e92ef81ef47353048ab0515c71c898ca@ec2-54-235-181-120.compute-1.amazonaws.com:5432/d7c47pofadq5ld")
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/")
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", "fcc7fc16406aa3f650b5419f99c7e14320c5cb6c")
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", "itsrxns/userbot-100101110")
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1306336056").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", "38e2c02bbc2c01f7fe1e6b28c237721ef56a4f8c9ede910c53c56543aa56405ac9976ebf35dee586c6c80c605cf439efce3dfe76799ebf791a52b1ee99950369")
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "45d8e7e9-5906-4f88-8ea2-6281f0d96fb8")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "rxubotnuovo")
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", "1290861304:AAHm_Jc7VxlhUmnDvH7Ngv5pA9wWr3KrnJ0")
    # Get your own API key from https://www.remove.bg/ or
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", "upnaMnhbEpRijfuRgX9TxNM2")
    # define "spam" in PMs
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 5))
    # Send .get_id in any channel to fill this value.
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", -1001492152928))
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", "@guccirxnsbot")
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", "https://telegra.ph/file/e38af5d97c838f24bac26.jpg")
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 5))
    if AUTH_TOKEN_DATA != None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", -1001492152928)
    if PRIVATE_GROUP_ID != None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError("Private Group ID invalido. Il tuo ID deve iniziare con -100 e dopo il chat id.")

class Development(Var):
    LOGGER = True
    # Here for later purposes
