import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../css/connection.css';
const Connection = () => {
    const [connectionLogin, setConnectionLogin] = useState('');
    const [connectionPassword, setConnectionPassword] = useState('');
    const [error, setError] = useState('');

    const handleLoginChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setConnectionLogin(event.target.value);
    }

    const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setConnectionPassword(event.target.value);
    }

    const handleLogin = () => {
        setError('')
        axios.post(process.env.REACT_APP_IP_BACK + '/user/auth/login', {
            "login" : connectionLogin,
            "password" : connectionPassword
        })
            .then(response => {
                console.log(response);
                localStorage.setItem('jwtAuthorization', response.data.access_token)
            })
            .catch(error => {
                console.log(error?.response?.data?.detail);
                setError(error?.response?.data?.detail);
            });
        setConnectionLogin('')
        setConnectionPassword('')
    }

    const handleSignup = () => {
        setError('')
        axios.post(process.env.REACT_APP_IP_BACK + '/user/auth/signup', {
            "login" : connectionLogin,
            "password" : connectionPassword
        })
            .then(response => {
                console.log(response);
                localStorage.setItem('jwtAuthorization', response.data.access_token)
            })
            .catch(error => {
                console.log(error.data);
                console.log(error?.response?.data?.detail);
                setError(error?.response?.data?.detail);
            });
        setConnectionLogin('')
        setConnectionPassword('')
    }

    return (
        <div className='connection-component'>
            <h3>Connection</h3>
            <input className='connection-input-and-button' type="text" placeholder="login" value={connectionLogin} onChange={handleLoginChange}/>
            <input className='connection-input-and-button' type="password" placeholder="password" value={connectionPassword} onChange={handlePasswordChange}/>
            {error ? <p className='app-error connection-error'>*{error}</p> : null}
            <button className='connection-input-and-button connection-input-button-login' onClick={handleLogin}>login</button>
            <button className='connection-input-and-button connection-input-button-signup' onClick={handleSignup}>signup</button>
        </div>
    );
}
export default Connection;