import './credits.css'
import React from 'react'

const Credits = () => {
    return (
        <>
            <main>
                <h2 id='motto'>PREPARE FOR TROUBLE AND MAKE IT DOUBLE</h2>
                <section>
                    <div className="backend">
                        <h4>The brains behind the backend part:</h4>
                        <ul>
                            <li>Francesco Natanni</li>
                            <li>Eiaki V. Morooka</li>
                        </ul>
                    </div>

                    <div className="database">
                        <h4>The person who made the database work:</h4>
                        <ul>
                            <li>Jenni Hallikas</li>
                        </ul>
                    </div>

                    <div className="frontend">
                        <h4>People who built the frontend:</h4>
                        <ul>
                            <li>Khai Cao</li>
                            <li>Kiana Aghajani</li>
                        </ul>
                    </div>
                </section>
                <div id='line'></div>
                <h2 id='how'>Contact Information</h2>
                <article>
                    <div className='back'>
                        <h4>I'll start with the people who made the logic work:</h4>
                        <div className="frank">
                            <p>Frank</p>
                            <p>His e-mail:</p>
                            <a href="mailto: francesn@metropolia.fi">francesn@metropolia.fi</a>
                            <p>His github link:</p>
                            <a href='https://github.com/murphyslemon'>https://github.com/murphyslemon</a>
                            <br></br> <br></br>
                        </div>
                        <div className="aki">
                            <p>Aki</p>
                            <p>His e-mail address is:</p>
                            <a href='mailto: eiakim@metropolia.fi'>eiakim@metropolia.fi</a>
                            <br></br> <br></br>
                        </div>
                    </div>
                    <div className="data">
                        <br></br> <br></br>
                        <p>For the database;</p>
                        <div className="jenni">
                            <p>Jenni <br></br> <br></br> had to do everything by herself, so I took this opportunity to shout-out to her.</p>
                            <p>You should too!</p>
                            <p>Have her e-mal if you have (database related) questions.</p>
                            <a href='mailto: jenni.hallikas@metropolia.fi'>jenni.hallikas@metropolia.fi</a>
                            <br></br> <br></br>
                        </div>
                    </div>
                    <div className="front">
                        <br></br> <br></br>
                        <h4>And finally we have the cool ppl!</h4>
                        <div className="khai">
                            <p>Khai</p>
                            <p>would be the only person who texts you back <br></br> <br></br> so I got all his accounts ready!</p>
                            <p>Find him on Facebook and Insta with: Radius</p>
                            <p>For Snap try: M_iuss12</p>
                            <p>His discord is lol#7890</p>
                            <p>Pinterest and Tumbler are personal, so NO.</p>
                        </div>
                        <div className="kia">
                            <p>hmmm Kiana?</p>
                            <p>She said thank you, next.</p>
                        </div>
                    </div>
                </article>
            </main>
        </>

    )
}


export default Credits;



