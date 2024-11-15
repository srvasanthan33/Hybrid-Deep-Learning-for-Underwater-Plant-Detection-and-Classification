from flask import Flask, request, jsonify, send_from_directory
from flask_jwt_extended import JWTManager, create_access_token
from flask_pymongo import PyMongo
from flask_cors import CORS
import bcrypt
import os
from dotenv import load_dotenv
from bson import ObjectId

BASE_URL = 'http://localhost:5000'
load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']

app.config['SECRET_KEY'] = 'phycofinder123'


mongo  = PyMongo(app)
jwt = JWTManager(app)

from routes.authenticate import auth_bp
from routes.profile import profile_bp
from routes.launch import launch_bp
from routes.home import home_bp

IMAGE_UPLOAD_FOLDER = 'uploads/images'
VIDEO_UPLOAD_FOLDER = 'uploads/videos'

    
@app.route('/')
def getReq():
    return "Hello",202

@app.route('/uploads/videos/<user_id>/<path:filename>')
def serve_video(user_id, filename):
    # Ensure that the user_id is a valid ObjectId (assuming it's MongoDB ObjectId)
    if not ObjectId.is_valid(user_id):
        return "Invalid user ID", 400
    
    # Construct the path for the video file
    user_video_folder = os.path.join(VIDEO_UPLOAD_FOLDER, user_id)
    
    # Serve the video file from the correct folder
    return send_from_directory(user_video_folder, filename)

@app.route('/uploads/images/<user_id>/<path:filename>')
def serve_image(user_id, filename):
    # Ensure that the user_id is a valid ObjectId (assuming it's MongoDB ObjectId)
    if not ObjectId.is_valid(user_id):
        return "Invalid user ID", 400
    
    # Construct the path for the image file
    user_image_folder = os.path.join(IMAGE_UPLOAD_FOLDER, user_id)
    
    # Serve the image file from the correct folder
    return send_from_directory(user_image_folder, filename)
@app.route('/df')
def getDf():
    return "Df"

if __name__ == '__main__':
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)

    
    
    app.register_blueprint(launch_bp)
    app.register_blueprint(home_bp)


    app.run(debug=True)
    
