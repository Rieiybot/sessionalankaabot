import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 13526001))

    API_HASH = os.environ.get("API_HASH", "dcdcbf9265d374c0e4fcfe87ae744e61")
