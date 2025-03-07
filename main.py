from fastapi import FastAPI
from datetime import datetime
import json


from libs.tinyllama import fetch_historical_event

app = FastAPI()

@app.get("/events/today")
def get_today_events():
    now = datetime.now()

    info = fetch_historical_event(f"{now.day}/{now.month}")

    return info

@app.get("/events")
def get_events_from_date(date: str):
    info = fetch_historical_event(date)

    return info