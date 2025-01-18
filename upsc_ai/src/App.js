import './App.css';
import Nav from './Nav.js'
import { Routes, Route } from 'react-router-dom';
import Quiz from './Quiz.js';
import Header from './Header.js';
import { useLocation } from 'react-router-dom';


function App() {
  const location = useLocation();
  const isHomePage = location.pathname === "/";

  return (
    isHomePage?<div id = "container-fluid">
      <Header />
      <Routes>
      <Route path="/" element={<HomeContent />} />
      <Route path="/Modern-History" element={<Quiz />} />
     </Routes>
     <div id = "nav-container">
      <Nav />
      </div>
   </div>:<div id = "container-fluid">
      <Header />
      <div id = "nav-container">
      <Nav />
      </div>
      <Routes>
      <Route path="/" element={<HomeContent />} />
      <Route path="/Modern-History" element={<Quiz />} />
     </Routes>
   </div>
  );   
}

function HomeContent() {
  return (
    <div>
    <h1 id = "heading">UAI</h1>
    <p id = "description">Civil service preparation aided by AI</p>
    </div>
  );
}

export default App;
