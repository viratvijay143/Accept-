# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23455230"))
    API_HASH = getenv("API_HASH", "1740e4541ec18b9cdd3e5ff6f3687d46")
    BOT_TOKEN = getenv("BOT_TOKEN", "7103983582:AAHlKHHsJ4heJomxDB6CL65Am6TO7o-JLrs")
    FSUB = getenv("", "")
    CHID = int(getenv("CHID", "-1002114435811"))
    SUDO = list(map(int, getenv("SUDO", "6332321765").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://vijaysahu:Ajay#321@vijaysahu.nysbqg1.mongodb.net/?retryWrites=true&w=majority&appName=vijaysahu")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
