import './account_management.css'
import React from 'react'
import { useNavigate } from "react-router-dom";

const AccountManagement = ({username, callbackUsername ,  callbackSignedIn}) => {
    let navigate = useNavigate();
    
    function handleSignOutEvent() {
        callbackUsername("")        
        callbackSignedIn(false);

        localStorage.clear();

        const routeChange = () => {
            let path = "/airport-heist.github.io";
            navigate(path);
        }
        routeChange();

    }
    

    return (
        <>
            <h1>Profile</h1>
            <p>Username: {username}</p>

            <button onClick={handleSignOutEvent}>Sign out</button>
        </>

    )
}


export default AccountManagement;



