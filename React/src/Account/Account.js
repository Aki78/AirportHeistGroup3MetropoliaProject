import './account.css'
import React, { useRef } from 'react';
import { useState } from 'react';
import { useNavigate } from "react-router-dom";


import Home from '../Home/Home';

const Account = ({ callbackUsername ,  callbackSignedIn} ) => {
    
    //const nametest = document.getElementsByTagName("input[type='text']")[0].value;
    const [accUsername, setAccUsername] = useState("");        //check username
    const [accPassword, setAccPassword] = useState("");        //check password

    let navigate = useNavigate();   //for navigating to home page

    function handleUSername(accUsername) {
        callbackUsername(accUsername)
    }

    function handleSignedIn(signedin) {
        callbackSignedIn(signedin)
    }

    function checkCredentials(accUsername, accPassword, response) {
        console.log("Log check", accUsername)   
        console.log("Log check from DB", response)     
        
        let checkUser = response.username;
        //let checkPass = info[1];    
        console.log("After fetch", checkUser);
        if (checkUser === accUsername) { // && checkPass === passwordInputRef) {
            console.log("Credentials match");
            console.log("Redirecting user");
            return true;
        }
        else {
            console.log("Incorrect credentials");
            return false;
        }
    }

    async function retrieveInfo(accUsername) {
        await fetch('http://127.0.0.1:5000/Account/' + accUsername)
            .then(response => response.json())
            .then(response => {
                console.log("Got from DB ", response)
                const res = checkCredentials(accUsername, accPassword, response);
                return res;
            })
            .catch(err => console.error(err));    
    }


    function handleSignInEvent() {
        console.log(accUsername);
        console.log(accPassword);

        if (retrieveInfo(accUsername)) {
            handleUSername(accUsername);
            handleSignedIn(true);
            const routeChange = () => {
                let path = '/airport-heist.github.io';
                navigate(path);
            }
            routeChange();

        }
        else {
            handleSignedIn(false);
        }


    }




    return (
        <>
            <h1>Sign in</h1>
            <div className="sign-in-form">
                <div className="username">
                    <input 
                        id="username"
                        type="text"
                        placeholder='Username'
                        onChange={e => setAccUsername(e.target.value)}
                    />
                </div>
                
                <div className="password">
                    <input
                        id="password"
                        type="password"
                        placeholder='Password'
                        onChange={e => setAccPassword(e.target.value)}
                    />
                </div>
                <button onClick={handleSignInEvent}>Sign in</button>
                <br/>
            </div>

            <div className="line"></div>


{/*
            <h4>Or</h4>
            <h3>Sign up</h3>

            <div class="sign-up-form">
                <div class="username">
                    <input 
                        placeholder='Username'
                        onChange={e => setUsername(e.target.value)}
                    />
                </div>
                
                <div class="password">
                    <input
                        type="password"
                        placeholder='Password'
                        onChange={e => setPassword(e.target.value)}
                    />
                </div>

                <div class="password-confirm">
                    <input
                        type="password"
                        placeholder='Confirm password'
                        onChange={e => setPasswordconfirm(e.target.value)}
                    />
                </div>

                <button onClick={() => setText("Signed up")}>
                    <Link to="../airport-heist.github.io">Sign up</Link>
                </button>
            </div>
*/}
        </>

    )
}


export default Account;



