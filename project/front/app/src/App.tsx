import React from 'react';
import logo from './logo.svg';
import './App.css';
import Connection from './components/connection';
import SearchCustomerByLastName from './components/hiboutik/searchCustomerByLastName';

function App() {
  return (
    <div className="App">
      <header className="App-header">
          <h1>Dashboard</h1>
          <p>Coded by hetya</p>
      </header>
        <div className='app-page'>
            <SearchCustomerByLastName></SearchCustomerByLastName>
            <Connection/>
        </div>
    </div>
  );
}

export default App;
