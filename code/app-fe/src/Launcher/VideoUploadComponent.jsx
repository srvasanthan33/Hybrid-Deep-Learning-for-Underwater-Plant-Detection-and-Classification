import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Correct way to use useNavigate for routing
import axios from 'axios';
import { toast } from 'react-toastify'; // Import react-toastify
import Loading from '../Helpers/Loading'; // Import Loading component

function VideoUploadComponent() {
  const [videoFile, setVideoFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false); // State for loading
  const navigate = useNavigate(); // Initialize navigate for redirection

  const handleFileChange = (e) => {
    setVideoFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!videoFile) {
      toast.error('Please select a video to upload!');
      return;
    }

    const formData = new FormData();
    formData.append('video', videoFile);

    setIsLoading(true); // Start loading

    try {
      const token = localStorage.getItem('token');
      if (!token) {
        toast.error('You need to be logged in!');
        setIsLoading(false); // Stop loading
        return;
      }

      const response = await axios.post('http://localhost:5000/video/upload', formData, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.data.message === 'Video uploaded successfully') {
        toast.success('Video uploaded successfully');
        navigate('/'); // Redirect to home page after upload using useNavigate
      } else {
        toast.error('Failed to upload video');
      }
    } catch (error) {
      toast.error('Error uploading video. Please try again.');
      console.error(error);
    }

    setIsLoading(false); // Stop loading after request completes
  };

  return (
    <div className="video-upload-component p-6 bg-dark-green text-lime-200 rounded-lg shadow-lg max-w-md mx-auto mt-10">
      <h2 className="text-2xl font-bold text-center mb-4">Upload Your Video</h2>
      
      <input 
        type="file" 
        name="video-file" 
        accept="video/*" 
        onChange={handleFileChange} 
        className="block w-full mb-4 text-white bg-dark-green border-2 border-lime-200 rounded-lg p-2"
      />
      
      <button 
        className="w-full bg-lime-500 text-neutral-900 font-bold py-2 rounded-lg hover:bg-lime-600 transition-all duration-300"
        onClick={handleUpload}
        disabled={isLoading} // Disable the button while loading
      >
        {isLoading ? 'Uploading...' : 'Analyze'}
      </button>

      {isLoading && <Loading />} {/* Show loading spinner when uploading */}
    </div>
  );
}

export default VideoUploadComponent;
