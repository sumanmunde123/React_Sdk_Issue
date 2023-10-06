
import './App.css'
import { FrappeProvider } from 'frappe-react-sdk'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './Home'

function App() {


  return (
	<div className="App">
	  <FrappeProvider socketPort={import.meta.env.VITE_SOCKET_PORT ?? ''} url="http://localhost:8001" >
	<BrowserRouter basename={import.meta.env.VITE_BASE_PATH}>
	<Routes>
		<Route path='/' element={<Home />} />
	</Routes>
	</BrowserRouter>
	  </FrappeProvider>
	</div>
  )
}

export default App
