import logo from './logo.svg';
import { Component } from 'react';

import './App.css';
import { useEffect, useState } from 'react';
import staffCard from '../HR and Manager/staff-card/staff-card.component';
import Card from 'react-bootstrap/Card';
import {Container , Col, Button} from 'react-bootstrap';  

const App = () => {
  const [searchField, setSearchFIeld] = useState('');
  const [staff] = useState([]);





  // for getting the data website
  
  // useEffect(() => {
  //   fetch('link')
  //     .then((response) => response.json())
  //     .then((users) => setStaff(users));
  // }, []);


  return (
    <div className='=App'>

      <h1 className='app-title'>HR and Manager</h1>

        <div className = "container-fluid">
        



        </div>











    </div>



  );









};



export default App;
