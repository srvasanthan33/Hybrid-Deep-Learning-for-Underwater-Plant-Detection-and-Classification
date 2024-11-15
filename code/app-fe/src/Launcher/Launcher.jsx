import React from 'react'
import Header from '../Helpers/Header'
import VideoUploadComponent from './VideoUploadComponent'

function Launcher() {
  return (
    <div className="flex-1 p-10 launcher-container">
      <Header title="Launch"/>
      <VideoUploadComponent/>
    </div>
  )
}

export default Launcher