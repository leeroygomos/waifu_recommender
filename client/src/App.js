import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';

// Components
import Layout from './components/Layout/Layout';
import Home from './components/Home/Home';
import Anime from './components/Anime/Anime';
import Characters from './components/Characters/Characters';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout/>}>
          <Route index element={<Home/>}/>
          <Route path='anime' element={<Anime/>}/>
          <Route path='characters' element={<Characters/>}/>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
