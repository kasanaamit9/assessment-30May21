import os
import sys
import json
import logging
from flask import Flask, request, jsonify, Response
import getpass
# import jwt
from configparser import ConfigParser

Announcement = Flask(__name__)
config = ConfigParser()
config.read("C:/Users/akasana/Downloads/New folder/announcement.ini")

filepath = config.get("filepath", "path")
filename = filepath + "/announcement.log"
logging.basicConfig(filename= filename, level = logging.INFO, format = '%(asctime)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@Announcement.route("/announcement/list_all", methods = ["GET"])
def list_all_announcements():
    if request.headers.get("Authorization","").find("Basic") == -1:
        logger.info("Authorization failed!")
        return Response("Authorization failed! 'username'/'password' NOT found!"), 401
    user = config.get("auth", "username")
    pswd = config.get("auth", "password")
    request_user = request.authorization.username
    request_pswd = request.authorization.password
    # print(f"User: {user}, Pswd: {pswd}")
    if user != request_user or pswd != request_pswd:
        logger.info("Authorization failed!")
        return Response("Authorization failed! 'username'/'password' is incorrect!"), 401
    logger.info("Listing all announcements from file")
    with open(filepath+"/announcement.json", "r") as f:
        announcement_json = eval(f.read())
    logger.info("Completed")
    return jsonify({"Announcements":announcement_json})

@Announcement.route("/announcement/add", methods = ["PUT"])
def create():
    if request.headers.get("Authorization","").find("Basic") == -1:
        logger.info("Authorization failed!")
        return Response("Authorization failed! 'username'/'password' NOT found!"), 401
    user = config.get("auth", "username")
    pswd = config.get("auth", "password")
    request_user = request.authorization.username
    request_pswd = request.authorization.password
    # print(f"User: {user}, Pswd: {pswd}")
    if user != request_user or pswd != request_pswd:
        logger.info("Authorization failed!")
        return Response("Authorization failed! 'username'/'password' is incorrect!"), 401
    logger.info("Adding new announcement to announcements")
    request_json = request.get_json()
    with open(filepath+"/announcement.json", "r") as f:
        announcement_json = eval(f.read())
    announcement_json.append(request_json)
    with open(filepath+"/announcement.json", "w") as f:
        f.write(json.dumps(announcement_json, indent=4))
    logger.info("Completed")
    return Response("Announcement has been added successfully")

if __name__ == "__main__":
    # Reading host and port from environment variables. If not set, it will pick up below default values
    host = os.environ.get("HOST", "0.0.0.0") 
    port = os.environ.get("PORT", 5000)
    if port is None or host is None:
        logger.error("Envronment variables for host or port is not set! Please check.")
        sys.exit()
    Announcement.run(debug = True, host = host, port = port)