import React from 'react'

import './navigation.css'

import Logo from '../img/title.png'

import { Link } from "react-router-dom";

const Navigation = () => {
    return (

        <nav class="nav_bar">
            <ul>
                <li><img src={Logo} alt="logo"></img></li>
                <li><Link to="airport-heist.github.io" >Home</Link></li>
                <li><Link to="LeaderBoard" >Leaderboard</Link></li>
                <li><a href="https://aki78.itch.io/group3-metropolia" target="blank" >Game</a></li>
                <li><Link to="Tutorial">Tutorial</Link></li> 
            </ul>
        </nav>

    )
}


export default Navigation;
