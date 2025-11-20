from environs import Env


env = Env()
env.read_env()


DB_USERNAME = env("DB_USERNAME")
DB_PASSWORD = env("DB_PASSWORD")
DB_IP = env("DB_IP")
DB_PORT = env("DB_PORT")
DB_NAME = env("DB_NAME")

TG_BOT_TOKEN = env("TG_BOT_TOKEN")

OPENAI_API_KEY = env("OPENAI_API_KEY")
MODEL_NAME = env("MODEL_NAME")
MAX_TOKENS = int(env("MAX_TOKENS"))
