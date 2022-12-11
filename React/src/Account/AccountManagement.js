import './account_management.css'
import React from 'react'
import { useState } from 'react';
import { useNavigate } from "react-router-dom";

const AccountManagement = ({ username , callbackUsername ,  callbackSignedIn }) => {
    //////////////////////////////Sign out//////////////////////////////
    let navigate = useNavigate();
    
    function handleSignOutEvent() {
        callbackUsername("");
        callbackSignedIn(false);

        localStorage.clear();

        const routeChange = () => {
            let path = "/Home";
            navigate(path);
        }
        routeChange();

    }


    //////////////////////////////Change password//////////////////////////////
    const [oldPass, setOldPass]     = useState("");
    const [newPass, setNewPass]     = useState("");
    const [confPass, setConfPass]   = useState("");

    async function changePassword() {
        await fetch("https://aki78.pythonanywhere.com/Account/changePass?username=" + username + "&newpass=" + newPass, {method: "POST"})
            .then(response => response.json())
            .then(response => {
                console.log("Message", response);
            })
            .catch(err => console.error(err));
    }

    async function checkOldPassword() {
        let answer;
        await fetch("https://aki78.pythonanywhere.com/Account/checkOldPass?username=" + username + "&oldpass=" + oldPass)
            .then(response => response.json())
            .then(response => {
                console.log("Got", response);
                answer = response;
            })
            .catch(err => console.error(err));
        if (answer.message === "Exist") {
            return true;
        }
        else if (answer.message === "Nonexist") {
            return false;
        }
    }

    async function handleChangePasswordEvent() {
        if (oldPass === newPass) {
            alert("New password can't be the same as old password");
        }
        else if (newPass !== confPass) {
            alert("Wrong confirm password. Please check again.");
        }
        else if (oldPass !== newPass && newPass === confPass) {
            let localUser = localStorage.getItem("user");
            
            if (localUser === username) {
                const oldPassMatch = await checkOldPassword();

                if (oldPassMatch === true) {
                    await changePassword();
                    console.log("Password changed");
                    
                    const routeChange = () => {
                        let path = "/Home";
                        navigate(path);
                    }
                    routeChange();
                }
                else {
                    alert("Old password incorrect. Please try again");
                }
            }
            else {
                alert("Something went wrong. Please sign out and sign in again.\nIf the error still occurs please contact the developers");
            }
        }  
    }
    

    //////////////////////////////Delete account//////////////////////////////
    const [delUsername, setDelUsername]     = useState("");
    const [delPassword, setDelPassword]     = useState("");
    const [delCFPassword, setDelCFPassword] = useState("");

    async function deleteAccount() {
        await fetch("https://aki78.pythonanywhere.com/Account/deleteAccount?username=" + delUsername + "&password=" + delPassword, {method: "POST"})
            .then(response => response.json())
            .then(response => {
                console.log("Message", response);
            })
            .catch(err => console.error(err));
    }

    async function passCheck() {
        let res;
        await fetch("https://aki78.pythonanywhere.com/Account/retrieve?userin=" + delUsername + "&passin=" + delPassword)
            .then(response => response.json())
            .then(response => {
                console.log("Got", response);
                //const res = checkCredentials(accUsername, accPassword, response);
                if (response.message === "Allow") {
                    //console.log("User existed");
                    res = true;
                }
                else if (response.message === "Block") {
                    //console.log("No user with same username");
                    res = false;
                }
            })
            .catch(err => console.error(err)); 
        return res;
    }

    async function handleDeleteAccountEvent() {
        let userConfirmDelete = window.confirm("Are you sure you want to delete your account?");
        if (userConfirmDelete) {
            if (delUsername === username && username === localStorage.getItem("user")) {
                if (delPassword === delCFPassword) {
                    const delPassCheck = await passCheck();
                    if (delPassCheck) {
                        deleteAccount();

                        callbackUsername("");
                        callbackSignedIn(false);

                        localStorage.clear();

                        const routeChange = () => {
                            let path = "/Home";
                            navigate(path);
                        }
                        routeChange();
                    }
                    else {
                        alert("Wrong password. Please try again.");
                    }
                }
                else {
                    alert("Wrong confirm password. Please check again.");
                }
            }
            else {
                alert("Wrong username. Please try again.")
            }
        }
        
        
    }

    return (
        <>
            <h1>Profile</h1>
            <p>Username: <strong>{username}</strong></p>

            <div className="sign-out">
                <button onClick={handleSignOutEvent}>Sign out</button>
            </div>

            <div className="line"></div>

            <h4>Change password</h4>
            <div className="change-password">
                <div className="cpw-old-password">
                    <input
                        type="password"
                        placeholder='Old password'
                        onChange={e => setOldPass(e.target.value)}
                    />
                </div>

                <div className="cpw-new-password">
                    <input
                        type="password"
                        placeholder='New password'
                        onChange={e => setNewPass(e.target.value)}
                    />
                </div>

                <div className="cpw-cfn-password">
                    <input
                        type="password"
                        placeholder='Confirm password'
                        onChange={e => setConfPass(e.target.value)}
                    />
                </div>

                <button onClick={handleChangePasswordEvent}>Change password</button>
            </div>

            <div className="line"></div>

            <h4>Delete account</h4>

            <div className="delete-account">
                <div className="del-username">
                    <input
                        placeholder='Username'
                        onChange={e => setDelUsername(e.target.value)}
                    />
                </div>

                <div className="del-password">
                    <input
                        type="password"
                        placeholder='Password'
                        onChange={e => setDelPassword(e.target.value)}
                    />
                </div>

                <div className="del-cf-password">
                    <input
                        type="password"
                        placeholder='Confirm password'
                        onChange={e => setDelCFPassword(e.target.value)}
                    />
                </div>

                <button onClick={handleDeleteAccountEvent}>Delete account</button>
            </div>
        </>

    )
}


export default AccountManagement;



