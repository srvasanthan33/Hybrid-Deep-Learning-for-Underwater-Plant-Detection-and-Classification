import React from 'react'

function VideoComponent({ result }) {
  return (
    <div className="video-container mt-4">
      <div className="video">
        <video controls src={result.video_url} width="100%" className='rounded-lg'/>
      </div>

      <div className="images">
        <h3 className="text-xl font-semibold mt-4">Labelled Images:</h3>
        <div className="grid grid-cols-3 gap-4 mt-4">
          {result.image_urls && result.image_urls.map((imageUrl, index) => (
            <div key={index} className="image">
              <img
                src={imageUrl}
                alt={`Image ${index + 1}`}
                className="rounded-lg shadow-lg"
                style={{ width: '100%', height: 'auto' }}
              />
              <h4 className='text-xs'>{(imageUrl.split('\\'))[imageUrl.split('\\').length - 1]}</h4>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default VideoComponent;
