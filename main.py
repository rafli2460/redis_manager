#!/usr/bin/env python3

# Scola Redis Manager
# A system for managing redis server for scola LMS.
# __author__ = "Muhammad Rafli"
# __copyright__ = "Copyright 2022, PT. Inovasi Edukasi Bangsa"

from flask import Flask, jsonify
from redis import Redis
from waitress import serve
from dotenv import load_dotenv
import os

load_dotenv()
redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
app_host = os.getenv('APP_HOST')
app_port = os.getenv('APP_PORT')

app = Flask(__name__)

redis = Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.get("/")
def home(): 
    return {'info': 'Scola Redis Manager', 'version':'0.1-alpha4'}

@app.get("/list")
def get_list_keys():
       result = []
       for key in redis.scan_iter("*-settingdata"):
              result.append(key)
       return jsonify(results = result)

@app.route("/delete/<keys>", methods=['POST'])
def delete_keys(keys):
    delete_keys = redis.delete(keys)
    if methods == 'POST':
        redis.delete(keys)
        return { "status": True, "message": keys+" has been deleted."}
    else:
        return { "status": False, "message": keys+ "not found."}


if __name__ == '__main__':
    print("\033c", end="")
    print("Scola Redis manager")
    print("Listening at: "+app_host+" port "+app_port )
    serve(app, host=app_host, port=app_port)