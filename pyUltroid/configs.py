# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (18783720
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=6, cast=int)
    )
    API_HASH = (c27199edf9f0510ff3d90c2c3dfa3963
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("1AZWarzMBu4Adishd1GjPJA8kUNXcQG0P4E9BNZ0MfNoIIMVkLD1M0WTFxdoq3d4aMPGqanrwRejzDABfWwjCZRbtH5_tr8tEtfkYbxun4rYHlxkomjrVvnSQneGkcVDw1qQ_OgJlBbFxU_v8zKzwHMSmiYI3VKvQjVeWb80WnxlrvG4M1t36lnoPFTdssb-wtpnJ6_B6kwZtXkiGtGGOOMhUpFMUHqeA-78t8MQUPc07ugH2oP8Yq6IYPNJzVACa6Okcu-CA0mQ0OG-E5pTDrlAnqfLWF9LD4QDlXbEjrTOXsPhckyiuA363OBWuUYLM5xPRoJgTunx4uY0q55WspiQKcB2rKks=", default=None)
    REDIS_URI = (http://redis-15676.c273.us-east-1-2.ec2.cloud.redislabs.com:15676
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (SWiR9Wem4BVUKKq5lpvuNAi4xA1atItU
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=None)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
