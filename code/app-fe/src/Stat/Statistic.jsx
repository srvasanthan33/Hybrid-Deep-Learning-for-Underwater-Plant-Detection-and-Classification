import React from 'react'
import Header from '../Helpers/Header'

import graph from '../assets/download (1).png'

function Statistic() {
  return (
    <div className="flex-1 p-10 ">
      <Header title="Stats"/>
      <div className="">
        <img src={graph}  alt="" className="max-w-full h-auto rounded-lg shadow-md mx-auto my-auto "/>
      </div>
    </div>
  )
}

export default Statistic