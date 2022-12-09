import './game.css'
import React from 'react'
import Iframe from 'react-iframe';

const Game = () => {
    return (
        <>
            <div className="game-screen">
                <Iframe className='porting' frameborder="0" src="https://aki78.pythonanywhere.com/game" width="1366" height="768"><a href="https://aki78.pythonanywhere.com/game">Group3 Metropolia by Aki78</a></Iframe>
            </div>
        </>
        
    )
}


export default Game;

        //<embed  src="../Publish/game.html" / >


