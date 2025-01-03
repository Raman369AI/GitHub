import './App.css';
import Nav from './Nav.js'
import { Routes, Route } from 'react-router-dom';
import Quiz from './Quiz.js';
import Header from './Header.js';

function App() {
  return (
    <div id = "container-fluid">
      <Header />

      <HomeContent />
      <div id = "nav-container">
      <Nav />
      </div>
      <Routes>
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
