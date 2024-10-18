import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+pymysql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}'
        f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

