import './account_management.css'
import React from 'react'
import { Link } from "react-router-dom";

const AccountManagement = ({username}) => {
    
    

    return (
        <>
            <h1>Profile</h1>
            <p>Username: {username}</p>
        </>

    )
}


export default AccountManagement;



