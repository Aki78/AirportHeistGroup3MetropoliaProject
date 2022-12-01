import './credits.css'
import React from 'react'

const Credits = () => {
    return (
        <>
            <main>
                <h2 id='motto'>PREPARE FOR TROUBLE AND MAKE IT DOUBLE</h2>
                <section>
                    <div class="backend">
                        <h4>The brains behind the backend part:</h4>
                        <ul>
                            <li>Francesco Natanni</li>
                            <li>Eiaki V. Morooka</li>
                        </ul>
                    </div>

                    <div class="database">
                        <h4>The person who made the database work:</h4>
                        <ul>
                            <li>Jenni Hallikas</li>
                        </ul>
                    </div>

                    <div class="frontend">
                        <h4>People who built the frontend:</h4>
                        <ul>
                            <li>Khai Cao</li>
                            <li>Kiana Aghajani</li>
                        </ul>
                    </div>
                </section>
                <div id='line'></div>
                <h2 id='how'>How to talk to us?</h2>
                <article>
                    <div class='back'>
                        <h4>I'll start with the people who made the logic work:</h4>
                        <div class="frank">
                            <p>Frank</p>
                            <p>His e-mail:</p>
                            <a href="mailto: francesn@metropolia.fi">francesn@metropolia.fi</a>
                            <p>his github link for the nerds:</p>
                            <a href='https://github.com/murphyslemon'>https://github.com/murphyslemon</a>
                            <br></br> <br></br>
                        </div>
                        <div class="aki">
                            <p>Aki</p>
                            <p>Everything about him is confidential, sorry babe.</p>
                            <p>But I found his e-mail for you!</p>
                            <a href='mailto: eiakim@metropolia.fi'>eiakim@metropolia.fi</a>
                            <br></br> <br></br>
                        </div>
                    </div>
                    <div class="data">
                        <br></br> <br></br>
                        <h4>For the database ;</h4>
                        <div class="jenni">
                            <p>Jenni <br></br><br></br>had to do everything by herself, so I took this opportunity to shout-out to her.</p>
                            <p>You should too!</p>
                            <p>Have her e-mal if you have (database related) questions.</p>
                            <a href='mailto: jenni.hallikas@metropolia.fi'>jenni.hallikas@metropolia.fi</a>
                            <br></br> <br></br>
                        </div>
                    </div>
                    <div class="front">
                        <br></br> <br></br>
                        <h4>And finally we have the cool ppl!</h4>
                        <div class="khai">
                            <p>Khai <br></br> <br></br> would be the only person who will text you back <br></br>so I got all his accounts ready!</p>
                            <p>Find him on facebook and Insta with: MKRadius</p>
                            <p>For snap try: M_k_Radiuss12</p>
                            <p>Pinterest and tumbler are personal, so NO.</p>
                            <p>His discord is: Lmao#7890</p>
                            <p>And the rest is NOYB, bestie!</p>
                        </div>
                        <div class="kia">
                            <p>Kiana?</p>
                            <p>She said thank you, next.</p>
                        </div>
                    </div>
                </article>

            </main>
        </>

    )
}


export default Credits;



