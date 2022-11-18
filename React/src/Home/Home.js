import './home.css'
import React from 'react'
import background from '../img/main_background.png'

const Home = () => {
    return (
        <>
        <img src={background} alt='background'></img>
        <div id='body-content'></div>
        <p> This is home. </p>
        </>
        
    )
}


export default Home;



