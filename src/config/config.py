# imports
from decouple import config
from motor.motor_asyncio import AsyncIOMotorClient
from models.admin import AdminInConfig
from models.token import TokenSettings


#import configs

def load_config() -> dict:
    try:
        return {

            "LOG_DEBUG": config("LOG_DEBUG", cast=bool),

            "DATABASE": {
                "default": {
                    "ENGINE": config("DB_ENGINE", cast=str),
                    "NAME": config("DB_NAME", cast=str),
                    "USER": config("DB_USERNAME", cast=str),
                    "PASSWORD": config("DB_PASSWORD", cast=str),
                    "HOST": config("DB_HOST", cast=str),
                    "PORT": config("DB_PORT", cast=int),
                }
            },

            "ADMIN": {
                "USERNAME": config("ADMIN_USERNAME", cast=str),
                "HASHED_PASSWORD": config("ADMIN_HASHED_PASSWORD", cast=str)
            },

            "TOKEN": {
                "SECRET_KEY": config("TOKEN_SECRET_KEY", cast=str),
                "ALGORITHM": config("TOKEN_ALGORITHM", cast=str),
                "ACCESS_EXPIRES_MINUTES": config("TOKEN_ACCESS_EXPIRE_MINUTES", cast=int)
            }
        }

    except BaseException as e:
        print(e)


def init_db_client(CONF: dict) -> AsyncIOMotorClient:
    DB_CLIENT = AsyncIOMotorClient(
        host=CONF.get("DATABASE", dict())["default"]["HOST"],
        port=CONF.get("DATABASE", dict())["default"]["PORT"],
        username=CONF.get("DATABASE", dict())["default"]["USER"],
        password=CONF.get("DATABASE", dict())["default"]["PASSWORD"],
    )

    return DB_CLIENT[CONF.get("DATABASE", dict())["default"]["NAME"]]


def close_db_client(DB_CLIENT: AsyncIOMotorClient):
    DB_CLIENT.close()


def init_admin_user(CONF: dict) -> AdminInConfig:
    ADMIN_USER = CONF.get("ADMIN", dict())["USERNAME"]
    ADMIN_HASHED_PW = CONF.get("ADMIN", dict())["HASHED_PASSWORD"]

    return AdminInConfig(
        username=ADMIN_USER, hashed_password=ADMIN_HASHED_PW)


def init_token_settings(CONF: dict) -> TokenSettings:
    return TokenSettings(TOKEN_SECRET_KEY=CONF.get("TOKEN", dict())["SECRET_KEY"], ALGORITHM=CONF.get("TOKEN", dict())["ALGORITHM"], ACCESS_TOKEN_EXPIRE_MINUTES=CONF.get(
        "TOKEN", dict())["ACCESS_EXPIRES_MINUTES"])


CONF = load_config()
DB = init_db_client(CONF)
ADMIN_CONFIG = init_admin_user(CONF)
TOKEN_SETTINGS = init_token_settings(CONF)
