import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Card from './componenti/Card.jsx'
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Card title="Pitoneeee"
    desc="Un bel pitone sexy"
    imgUrl='/pics/pitone.jpg'/>
    <App />
  </StrictMode>,
)
