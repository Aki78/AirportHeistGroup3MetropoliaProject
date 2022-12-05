import './leadbrd.css'
import React, { useState, useEffect } from 'react'

const LeaderBoard = () => {
    const [userInfo, setUserInfo] = useState(Array.from(Array(10).keys()));
    const request = "http://127.0.0.1:5000/top_ten";

    useEffect(() => {
        async function get_topten_info() {
            fetch(request)
                .then(response => response.json())
                .then(response => {
                    console.log("Got from DB ", response);
                    setUserInfo(response);
                })
                .catch(err => console.error(err));
            return "Data retrieved";
        }
        get_topten_info();
    }, [request]);
    
    //console.log(userInfo[0]);

    
    //const my_list = userInfo.map();

    const makeList = () => (userInfo.map(userInfo => {

        return  (
            <li className='fade-in-list' style={{ opacity: "0", animationDelay: `${0.05 * userInfo.length}s` }}>
                <a id="ldb_username">{userInfo[0]}</a>
                <a id="ldb_score">{userInfo[1]}</a>
            </li>
        )
    }))

    return (
        <>
            <div className="main">
                <div className="section">
                    <div className="leadbrd">
                        <div className="top">
                            <h1>Top 10 Players</h1>
                        </div>
                        <div className="ppl">
                            <ol>
                                {makeList()}
                            </ol>
                        </div>

                        <h1 className="you">You</h1>
                        <li className="one"></li>
                    </div>
                </div>
            </div>
        </>

    )
}


export default LeaderBoard;





