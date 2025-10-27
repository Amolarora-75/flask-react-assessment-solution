import React from 'react'
import Tasks from './pages/Tasks'

export default function App(){
  return (
    <div style={{maxWidth:900, margin:'40px auto', padding:'0 16px'}}>
      <h1>Tasks & Comments</h1>
      <p>Simple UI to demo Task CRUD and Comment CRUD.</p>
      <Tasks />
    </div>
  )
}
