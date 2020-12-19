# imports
from motor.motor_asyncio import AsyncIOMotorClient
import yaml
from models.admin import AdminInConfig

# read config file


def load_config() -> dict:
    try:
        with open('config/config.yml') as (yaml_file):
            conf = yaml.load(yaml_file.read(), Loader=yaml.SafeLoader)
        return conf
    except OSError as e:
        print(e)


CONF = load_config()

# database configs
DB_CLIENT = AsyncIOMotorClient(
    host=CONF.get("databases", dict())["default"]["HOST"],
    port=CONF.get("databases", dict())["default"]["PORT"],
    username=CONF.get("databases", dict())["default"]["USER"],
    password=CONF.get("databases", dict())["default"]["PASSWORD"],
)

DB = DB_CLIENT[CONF.get("databases", dict())["default"]["NAME"]]


def close_db_client():
    DB_CLIENT.close()


# admin-user configs
ADMIN = CONF.get("api_auth", dict())["admin"]
ADMIN_USER = CONF.get("api_auth", dict())["admin"]["USER"]
ADMIN_HASHED_PW = CONF.get("api_auth", dict())["admin"]["HASHED_PASSWORD"]

ADMIN_CONFIG = AdminInConfig(
    username=ADMIN_USER, hashed_password=ADMIN_HASHED_PW)

# token configs
TOKEN_SECRET_KEY = CONF.get("api_auth", dict())["token"]["SECRET_KEY"]
ALGORITHM = CONF.get("api_auth", dict())["token"]["ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = CONF.get("api_auth", dict())[
    "token"]["ACCESS_TOKEN_EXPIRE_MINUTES"]
