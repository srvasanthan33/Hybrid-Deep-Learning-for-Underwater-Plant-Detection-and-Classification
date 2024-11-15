import os

from app import mongo
from bson import ObjectId
from pymongo.errors import PyMongoError
import secrets
from flask import make_response,session,request,abort
IMAGE_UPLOAD_FOLDER = 'uploads/images'

IMAGE_RESULT_FOLDER = 'gcolab/results'

        
def handle_analysis(path,user_id,video_id):
    images = []
    if os.path.exists(path):
        user_folder = os.path.join(IMAGE_UPLOAD_FOLDER,str(user_id))
        os.makedirs(user_folder, exist_ok=True)

        if os.path.isdir(IMAGE_RESULT_FOLDER):
            for file_name in os.listdir(IMAGE_RESULT_FOLDER):
                file_path = os.path.join(IMAGE_RESULT_FOLDER, file_name)
                
                # Check if the item is a file (not a directory)
                if os.path.isfile(file_path):
                    user_file_path = os.path.join(user_folder, file_name)
                    
                    # Save the file to the user's folder
                    with open(file_path, 'rb') as src_file, open(user_file_path, 'wb') as dest_file:
                        dest_file.write(src_file.read())
                    
                    images.append(user_file_path)
            try:
                result = mongo.db.videos.update_one(
                    {'_id': ObjectId(video_id)},
                    {'$set': {'images': images}},
                    upsert=True
                )
                if result.modified_count > 0:
                    print(f"Video data updated successfully for video ID {video_id}.")
                elif result.upserted_id:
                    print(f"Video data inserted successfully with new ID {result.upserted_id}.")
                else:
                    print(f"No changes made to the video data for video ID {video_id}.")
            except PyMongoError as e:
                print(f"Error updating video data: {e}")
        else:
            print(f"Error: {IMAGE_RESULT_FOLDER} is not a valid directory.")
    else:
        print(f"Error: Provided path '{path}' does not exist.")

        # for file in IMAGE_RESULT_FOLDER:
            
        #     file_path = os.path.join(user_folder,file.filename)
        #     images.append(file_path)
        #     file.save(file_path)
            
        #     # store the images array into the video here using video_id

        #     #  video_data = {
        #     #     'user_id': user['_id'],
        #     #     'video_filename': filename,
        #     #     'path': file_path,
        #     #     'meta_data': {
        #     #         'mimetype': file.mimetype,
        #     #         'size': os.path.getsize(file_path)
        #     #     },
        #     #     'images': []
        #     # }

        
def serialize_objectid(obj):
    """Converts ObjectId to string for JSON serialization."""
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj
