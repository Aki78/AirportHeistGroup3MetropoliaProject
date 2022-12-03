import './account.css'
import React from 'react';
import { useState } from 'react';
import { useNavigate } from "react-router-dom";


const Account = ({ callbackUsername ,  callbackSignedIn} ) => {
    ///////////////Sign in///////////////
    const [accUsername, setAccUsername] = useState("");        //check username
    const [accPassword, setAccPassword] = useState("");        //check password

    let navigate = useNavigate();   //for navigating to home page

    function handleUsername(accUsername) {
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
        await fetch("http://127.0.0.1:5000/Account/retrieve=" + accUsername)
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
            handleUsername(accUsername);
            handleSignedIn(true);
            const routeChange = () => {
                let path = "/airport-heist.github.io";
                navigate(path);
            }
            routeChange();

        }
        else {
            handleSignedIn(false);
        }

    }


    ///////////////Sign up///////////////
    const [passwordConfirm, setPasswordConfirm] = useState("");

    function checkMatchSignUpInfo(accPassword, passwordConfirm) {
        if (accPassword === passwordConfirm) {
            return true;
        }
        else {
            return false
        }
    }

    async function checkExistingAccount(accUsername) {
        let res;
        await fetch("http://127.0.0.1:5000/Account/checkExist=" + accUsername)
            .then(response => response.json())
            .then(response => {
                console.log("Got from DB ", response)
                //const res = checkCredentials(accUsername, accPassword, response);
                if (response.message === "Exist") {
                    console.log("User existed")
                    res = true;
                }
                else if (response.message === "Nonexist") {
                    console.log("No user with same username")
                    res = false;
                }
            })
            .catch(err => console.error(err)); 
        if (res === true) {
            return true;
        }
        else {
            return false;
        }
    }

    async function registerNewUser(accUsername, accPassword) {    
        await fetch("http://127.0.0.1:5000/Account/createAccount?username=" + accUsername + "&password=" + accPassword, {method: "POST"})
            .then(response => response.json())
            .then(response => {
                console.log("Got from DB ", response) 
                console.log(response.message)               
            })
            .catch(err => console.error(err)); 
        return "Account created"
    }


    async function handleSignUpEvent() {
        console.log(accUsername);
        console.log(accPassword);
        console.log(passwordConfirm);
        
        const matchInfo = checkMatchSignUpInfo(accPassword, passwordConfirm);

        if (matchInfo) {
            handleUsername(accUsername);
            handleSignedIn(true);

            const exist = await checkExistingAccount(accUsername);
            if (exist) {
                alert("The username is taken. Please choose another one.");
                handleSignedIn(false);
            }
            else {
                console.log("About to create new acc");
                const res = registerNewUser(accUsername, accPassword);
                console.log(res)
                const routeChange = () => {
                    let path = '/airport-heist.github.io';
                    navigate(path);
                }
                routeChange();
            }
        }
        else {
            alert("Wrong password check. Please confirm again.");
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



            <h4>Don't have an account?</h4>
            <h2>Sign up</h2>

            <div className="sign-up-form">
                <div className="username">
                    <input 
                        placeholder='Username'
                        onChange={e => setAccUsername(e.target.value)}
                    />
                </div>
                
                <div className="password">
                    <input
                        type="password"
                        placeholder='Password'
                        onChange={e => setAccPassword(e.target.value)}
                    />
                </div>

                <div className="password-confirm">
                    <input
                        type="password"
                        placeholder='Confirm password'
                        onChange={e => setPasswordConfirm(e.target.value)}
                    />
                </div>

                <button onClick={handleSignUpEvent}>Sign up</button>
            </div>

        </>

    )
}


export default Account;



