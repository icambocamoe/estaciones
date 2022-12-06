import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Estaciones from './Estaciones';
import Regression from './Regression';
import Login from './Login';
import Home from './Home';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/Estaciones" element={<Estaciones />} />
      <Route path="/" element={<Login />} />      
      <Route path="/Regression" element={<Regression />} />      
      <Route path="/App" element={<App />} />
      <Route path="/Home" element={<Home />} />
    </Routes>
  </BrowserRouter>
 
);
 /*<React.StrictMode>
    <App />
</React.StrictMode>*/

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
