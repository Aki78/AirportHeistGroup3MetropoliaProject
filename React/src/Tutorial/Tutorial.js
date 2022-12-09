import './tutorial.css'
import React from 'react'

const Tutorial = () => {
    return (
        <>
            <div className='container'>
                <main>
                    <h2>How To Play Aairport Heist</h2>
                </main>
                <section>
                    <h2>Glossary</h2>
                    <ul>
                        <li>
                            <p>Flight Limit:</p>
                            <p>You were able to commandeer a small plane at Helsinki Airport.</p>
                            <p>Due to the size of the plane's fuel tank flights are limited to 800km.
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
                    </ul>
                </section>
            </div>
        </>

    )
}


export default Tutorial;



