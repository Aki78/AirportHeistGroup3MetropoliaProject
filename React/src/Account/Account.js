import './account.css';
import React from 'react';
import { useState, useRef } from 'react';
import { useNavigate } from "react-router-dom";
import ReCAPTCHA from "react-google-recaptcha";


const Account = ({ callbackUsername ,  callbackSignedIn} ) => {
    ///////////////Sign in///////////////
    const [accUsername, setAccUsername] = useState("");        //check username
    const [accPassword, setAccPassword] = useState("");        //check password

    let navigate = useNavigate();   //for navigating to home page

    function handleUsername(accUsername) {
        callbackUsername(accUsername);
    }

    function handleSignedIn(signedin) {
        callbackSignedIn(signedin);
    }

/*
    function checkCredentials(accUsername, accPassword, response) {
        console.log("Log check", accUsername);
        console.log("Log check from DB", response);
        
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
            alert("Wrong username or password. Please try again.");
            return false;
        }
    }*/

    async function retrieveInfo(accUsername, accPassword) {
        let answer;
        await fetch("http://127.0.0.1:5000/Account/retrieve?userin=" + accUsername + "&passin=" + accPassword)
            .then(response => response.json())
            .then(response => {
                console.log("Got", response)
                //const res = checkCredentials(accUsername, accPassword, response);
                answer = response.message;
            })
            .catch(err => console.error(err));   
        return answer;
    }

    async function handleSignInEvent() {
        //console.log(accUsername);
        //console.log(accPassword);

        let dbAllowance = await retrieveInfo(accUsername, accPassword);

        if (dbAllowance === "Allow" && accUsername !== "" && accPassword !== "") {
            handleUsername(accUsername);
            handleSignedIn(true);

            const userData = {
                "user": accUsername,
                "signedin": true
            }
            console.log("Adding to local storage", userData);
            localStorage.setItem("user", userData.user);
            localStorage.setItem("signed_in", userData.signedin);

            const routeChange = () => {
                let path = "/home";
                navigate(path);
            }
            routeChange();
        }
        else {
            alert("Incorrect username or password. Please try again");
            handleSignedIn(false);
        }
    }



    ///////////////Sign up///////////////
    const captchaRef = useRef(null);
    const [passwordConfirm, setPasswordConfirm] = useState("");
    var token;
    var humanConfirm = false;

    async function checkToken(token) {
        let answer;
        //console.log("2 --- ", token);
        await fetch("http://127.0.0.1:5000/Account/recaptcha?skey=6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe&token=" + token)
            .then(response => response.json())
            .then(response => {
                //console.log("Received from API", response);
                answer = response;
            })
            .catch(err => console.error(err));
        //console.log("Answer: ", answer);

        return answer.success;
    }

    function checkMatchSignUpInfo(accPassword, passwordConfirm) {
        if (accPassword === passwordConfirm) {
            return true;
        }
        else {
            return false;
        }
    }

    async function checkExistingAccount(accUsername) {
        let res;
        await fetch("http://127.0.0.1:5000/Account/checkExist=" + accUsername)
            .then(response => response.json())
            .then(response => {
                console.log("Got", response);
                //const res = checkCredentials(accUsername, accPassword, response);
                if (response.message === "Exist") {
                    console.log("User existed");
                    res = true;
                }
                else if (response.message === "Nonexist") {
                    console.log("No user with same username");
                    res = false;
                }
            })
            .catch(err => console.error(err)); 
        return res;
    }

    async function registerNewUser(accUsername, accPassword) {    
        await fetch("http://127.0.0.1:5000/Account/createAccount?username=" + accUsername + "&password=" + accPassword, {method: "POST"})
            .then(response => response.json())
            .then(response => {
                console.log("Got", response);
                //console.log(response.message);           
            })
            .catch(err => console.error(err)); 
        return "Account created";
    }

    function handleCaptchaButton() {
        token = captchaRef.current.getValue();
        //console.log("1 --- ", token);
    }


    async function handleSignUpEvent() {
        captchaRef.current.reset();
        //console.log(accUsername);
        //console.log(accPassword);
        //console.log(passwordConfirm);


        //Recaptcha token
        humanConfirm = await checkToken(token);
        //console.log("-------", humanConfirm);
        
        const matchInfo = checkMatchSignUpInfo(accPassword, passwordConfirm);

        if (matchInfo === true && humanConfirm === true) {
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
                console.log(res);

                const routeChange = () => {
                    let path = '/home';
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
                <div className="captcha">
                    <ReCAPTCHA
                        sitekey="6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"      //Development
                        //sitekey="6LcUh2AjAAAAAN_Rn3CfWhN9Vpl1H__2gjjwDHHS"    //Official
                        ref={captchaRef}
                        onChange={handleCaptchaButton}
                    />
                </div>
                <button onClick={handleSignUpEvent}>Sign up</button>
            </div>
        </>
    )
}


export default Account;



