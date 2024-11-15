
from venv import logger
from bson import ObjectId
from flask import Flask, request, Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.utils import secure_filename
from app import mongo, BASE_URL


home_bp = Blueprint('home',__name__)
from helpers.uploadHelper import serialize_objectid
@home_bp.route('/home',methods=['GET'])
@jwt_required()
def sendHome():
    try:
        current_user = get_jwt_identity()
        user = mongo.db.users.find_one({'email':current_user['email']})

        if not user:
            return jsonify({'message': 'User not found'}), 404
        
        if user.get('videos') and len(user['videos']) > 0:
            latest_video_id = user['videos'][-1]
            video = mongo.db.videos.find_one({'_id': ObjectId(latest_video_id)})
            if not video:
                return jsonify({'message': 'Video not found'}), 404
            serialized_video = {key: serialize_objectid(value) for key, value in video.items()}
            video_url = f"{BASE_URL}/{video['path']}"
            serialized_video['video_url'] = video_url
            if 'images' in video:
                image_urls = []
                for img_path in video['images']:
                    # Convert image paths to URLs
                    image_url = f"{BASE_URL}/{img_path}"

                    # Add the image URL to the list
                    image_urls.append(image_url)

                # Attach the image URLs to the serialized video data
                serialized_video['image_urls'] = image_urls
            return jsonify(serialized_video), 200
        else:
            return jsonify({'message': 'No videos found for this user'}), 404
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)}), 500
