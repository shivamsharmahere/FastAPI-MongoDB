import os

class Settings:
    # We read the MONGO_URL from the environment, just like before.
    MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://<username>:<your_password>@cluster0.n1i16pc.mongodb.net/")
    MONGO_DB_NAME = "TEST_APP"
    # We can add other settings here later, like Secret Keys for JWT.
    PROJECT_NAME = "Modular User API  CRUD"

settings = Settings()

