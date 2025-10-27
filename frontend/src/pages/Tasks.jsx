import React, { useEffect, useState } from 'react'

function CommentList({ taskId }){
  const [comments, setComments] = useState([])
  const [body, setBody] = useState('')
  const [author, setAuthor] = useState('')

  const load = async () => {
    const res = await fetch(`/api/tasks/${taskId}/comments`)
    const data = await res.json()
    setComments(data)
  }

  useEffect(()=>{ load() }, [taskId])

  const add = async () => {
    if(!body.trim()) return
    await fetch(`/api/tasks/${taskId}/comments`, {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ body, author })
    })
    setBody(''); setAuthor('')
    load()
  }

  const del = async (cid) => {
    await fetch(`/api/comments/${cid}`, { method:'DELETE' })
    load()
  }

  return (
    <div style={{border:'1px solid #ddd', padding:12, borderRadius:8, marginTop:8}}>
      <h4>Comments</h4>
      <div style={{display:'flex', gap:8, marginBottom:8}}>
        <input placeholder="Comment..." value={body} onChange={e=>setBody(e.target.value)} style={{flex:1}}/>
        <input placeholder="Author (optional)" value={author} onChange={e=>setAuthor(e.target.value)} style={{width:180}}/>
        <button onClick={add}>Add</button>
      </div>
      <ul style={{paddingLeft:18}}>
        {comments.map(c => (
          <li key={c.id} style={{marginBottom:6}}>
            <b>{c.author || 'Anon'}:</b> {c.body}
            <button style={{marginLeft:8}} onClick={()=>del(c.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default function Tasks(){
  const [tasks, setTasks] = useState([])
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  const load = async () => {
    const res = await fetch('/api/tasks')
    const data = await res.json()
    setTasks(data)
  }

  useEffect(()=>{ load() }, [])

  const add = async () => {
    if(!title.trim()) return
    await fetch('/api/tasks', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({ title, description })
    })
    setTitle(''); setDescription('')
    load()
  }

  const del = async (id) => {
    await fetch(`/api/tasks/${id}`, { method:'DELETE' })
    load()
  }

  return (
    <div>
      <h3>Create Task</h3>
      <div style={{display:'flex', gap:8, marginBottom:16}}>
        <input placeholder="Title" value={title} onChange={e=>setTitle(e.target.value)} style={{flex:1}}/>
        <input placeholder="Description" value={description} onChange={e=>setDescription(e.target.value)} style={{flex:2}}/>
        <button onClick={add}>Add</button>
      </div>

      <h3>All Tasks</h3>
      {tasks.length === 0 && <p>No tasks yet.</p>}
      <div style={{display:'grid', gap:12}}>
        {tasks.map(t => (
          <div key={t.id} style={{border:'1px solid #ccc', padding:12, borderRadius:8}}>
            <div style={{display:'flex', justifyContent:'space-between'}}>
              <div>
                <div style={{fontWeight:'bold'}}>{t.title}</div>
                <div style={{opacity:0.8}}>{t.description}</div>
              </div>
              <button onClick={()=>del(t.id)}>Delete</button>
            </div>
            <CommentList taskId={t.id} />
          </div>
        ))}
      </div>
    </div>
  )
}
