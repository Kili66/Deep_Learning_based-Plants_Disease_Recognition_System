//import { ImageUpload } from "./home";

import React, { Component } from 'react';
import './App.css';
import Main from "./Main";
import Apple from "./Apple";
import Patato from "./Patato";
import Tomato from "./Tomato";
import Corn from "./Corn";
import Grape from "./Grape";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Navbar from './Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';




function App() {
  return (
    <div className="App" >
      <header className="App-header">

      <Router>
      <Routes>

//      <Route exact path="/" element={<Main/>} />
        <Route path="/Apple" element={<Apple/>} />
        <Route path="/Patato" element={<Patato/>} />
        <Route path="/Tomato" element={<Tomato/>} />
        <Route  path="/Corn" element={<Corn/>}/>
        <Route path="/Grape" element={<Grape/>} />
      </Routes>

      </Router>

      </header>
    </div>
  );
}

export default App;
