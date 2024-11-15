import React from 'react';

function Loading() {
  return (
    <div className="flex justify-center items-center min-h-screen">
      <div className="flex items-center space-x-2">
        <div className="w-8 h-8 border-4 border-t-4 border-gray-200 border-solid rounded-full animate-spin border-t-blue-500"></div>
        <p className="text-lg text-gray-600">Loading...</p>
      </div>
    </div>
  );
}

export default Loading;
