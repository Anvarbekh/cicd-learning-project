import os
from dotenv import load_dotenv
import sentry_sdk
from fastapi import FastAPI
import logging

# This line loads the variables from your .env file
load_dotenv()

# Now, get the DSN from the environment
SENTRY_DSN = os.getenv("SENTRY_DSN")

# Only initialize Sentry if the DSN is set
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0,
    )

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CI/CD learning on a feature branch!"}

@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0

# Your existing logging setup
logger = logging.getLogger(__name__)

# These logs will be automatically sent to Sentry
logger.info('This will be sent to Sentry')
logger.warning('User login failed')
logger.error('Something went wrong')