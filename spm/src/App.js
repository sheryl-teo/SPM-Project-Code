import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import staffCard from './components/HR and Manager/staff-card/staff-card.component';


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

      

        


    </div>

  );









};



export default App;
