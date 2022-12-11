import './tutorial.css'
import React from 'react'

const Tutorial = () => {
    return (
        <>
            <div className='container'>
                <main>
                    <h2 id='how'>How To Play Aairport Heist</h2>
                    <div className='steps'>
                        <ol>
                            <li>
                                Go to our website: <a href='https://aki78.pythonanywhere.com/home'>https://aki78.pythonanywhere.com/home</a>
                            </li>
                            <li>
                                Then click on the game from the top of the page.
                            </li>
                            <li>
                                Wit for it to load...
                            </li>
                            <li>
                                Click on the start button.
                            </li>
                            <li>
                                You are given the chance to heist, or to travel. Choose wisely.
                            </li>
                            <li>
                                Now you can see the map, your location and the interpole's location.
                            </li>
                            <li>
                                The airports that you can select are in black. Choose your path. 
                            </li>
                            <li>Would you win? Or would the interpole get to you?</li>
                        </ol>
                    </div>
                </main>
                <div className='brd'>
                    <section>
                        <h1>Glossary</h1>
                        <ol>
                            <li>
                                <p>Flight Limit:</p>
                                <p>You were able to commandeer a small plane at Helsinki Airport.
                                    Due to the size of the plane's fuel tank flights are limited to 800km.
                                    Airports with-in 800km travel range are showenv on a map.
                                </p>
                            </li>
                            <li>
                                <p>Evading Capture:</p>
                                <p>
                                    Interpol moves from airport to airport at random. You can see in which city interpol is
                                    and must avoid flying to the same airport. The game is over if interpol lands in the same airport as you.
                                </p>
                            </li>
                            <li>
                                <p>Ticket:</p>
                                <p>
                                    You start the game with 5000€. Each flight cost money based on how long the flight is.
                                </p>
                            </li>
                            <li>
                                <p>Points:</p>
                                <p>Money is equal to points, so when the player reaches portugal their score is
                                    equal to how much money they have left.</p>
                            </li>
                            <li>
                                <p>Stealing:</p>
                                <p>
                                    In order to get more money
                                    and points, you can choose to steal. Stealing is done after arriving at an airport.</p>
                            </li>
                        </ol>
                    </section>
                </div>
            </div>
        </>

    )
}


export default Tutorial;



