import './home.css'
import React from 'react'

import CompassInner from '../Images/compass-icon-13573_inner.png'
import CompassOuter from '../Images/compass-icon-13573_outer.png'
import Airplane from '../Images/airplane-icon-png-2515.png'


const Home = () => {
    return (
        <>
            {/*<img src={require('../img/hud.gif')} alt='background'></img>*/}

            <div class="compass">
                <div class="compass-inner">
                    <img src={CompassInner} alt="compass-inner-logo"></img>
                </div>
                <div class="compass-outer">
                    <img src={CompassOuter} alt="compass-outer-logo"></img>
                </div>
            </div>

            <div class="airplane">
                <img src={Airplane} alt="airplane-image"></img>
            </div>
        </>
        
    )
}


export default Home;



