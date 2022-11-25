import './leadbrd.css'
import React from 'react'

const LeaderBoard = () => {

    const my_list = Array.from(Array(10).keys());

    const makeList = () => (my_list.map(e => {
        return <li className='fade-in-list' style={{ opacity: "0", animationDelay: `${0.05 * e}s` }}></li>
    }))

    return (
        <>
            <div class="main">
                <div class="section">
                    <div class="leadbrd">
                        <div class="top">
                            <h1>Top 10 Players</h1>
                        </div>
                        <div class="ppl">
                            <ol>
                                {makeList()}
                            </ol>
                        </div>

                        <h1>You</h1>
                        <li></li>
                    </div>
                </div>
            </div>
        </>

    )
}


export default LeaderBoard;





