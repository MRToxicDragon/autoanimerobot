from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("19134212"))
API_HASH = getenv("0d85b66bf650d9d64ec178e51fa6b2c9")
BOT_TOKEN = getenv("5756094413:AAH5xI_BxmAduPJtbkdam1Q9Ku743XtreHs")

MONGO_DB_URI = getenv("mongodb+srv://1:1@cluster0.1tetwnx.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("-1001247900358"))
UPLOADS_ID = int(getenv("-1001640403011"))

STATUS_ID = int(getenv("https://t.me/ARKJ360_anime_db/3"))
SCHEDULE_ID = int(getenv("https://t.me/ARKJ360_anime_db/5"))

CHANNEL_TITLE = getenv("ARKJ360")
INDEX_USERNAME = getenv("https://t.me/ARKJ360_anime_index")
UPLOADS_USERNAME = getenv("https://t.me/ARKJ360_anime_db")
