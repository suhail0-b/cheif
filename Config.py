import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6152616619:AAGLyZAC0gCHXBhSVy7NQw224Ad6LtPezLA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKABu0Eeof2nCL_7AJzb7drxU64mqo3RCSdeXx1EEE82e4f2Xf1LyqdFFYpxGl95AjIuBl-6cGJmmBTttYfhhDGWTfg5Gr2uyacuTpWTUzT-Y3585olIE7Omu4F7m2MOjinqKkCqwAyjdwFRx3-PLvS6aKaEZH0FemSQrw2BJYJC69GDTwxp-V71Owvxipig0Gu7jsruZ4GzHAgkMIFGJHn_pkp1TIg2XxfSMGpit0SsOD-XOWBYRCeydl2RbzH51dKJ8eYz_L69durE_ayHodCj150QUOuH9ep9GVRqbsf1TlYsINqgkIkbYEDi-L-4oljRlQKTkMlj1yQoNH97fzruUNQ=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "CHEIFxMUSICxBOT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5468701502")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
