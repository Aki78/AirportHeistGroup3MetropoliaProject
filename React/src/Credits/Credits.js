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
                            <p>Frank's</p>
                            <p>His e-mail:</p>
                            <a href="mailto: francesn@metropolia.fi">francesn@metropolia.fi</a>
                            <p>The github link for the nerds:</p>
                            <a href='https://github.com/murphyslemon'>https://github.com/murphyslemon</a>
                        </div>
                        <div class="Aki">
                            <p>Aki's</p>
                            <p>Everything about him is confidential, sorry babe</p>
                            <p>But look, I found his <p>e-mail</p> for you!</p>
                            <a href='mailto: eiakim@metropolia.fi'>eiakim@metropolia.fi</a>
                        </div>
                    </div>
                    <div class="data">
                        <p>For the database;</p>
                        <p>Jenni had to do everything by herself, so I take this opportunity to shout-out to her. You should too!</p>
                        <div class="jenni">
                            <p>Have her e-mal if you had database related questions.</p>
                            <a href='mailto: jenni.hallikas@metropolia.fi'>jenni.hallikas@metropolia.fi</a>
                        </div>
                    </div>
                    <div class="front">
                        <h4>And finally we have the gen-z!</h4>
                        <div class="Khai"></div>
                        <p>Khai is the only person who will text you back so I got all his account for you!</p>
                        <p>Find him on facebook with: MKRadius</p>
                        <p>Insta is the same, but for snap try: M_k_Radiuss12</p>
                        <p>Pinterest and tumbler are personal, so NO.</p>
                        <p>His discord is Lmao#7890</p>
                        <p>The rest is NOYB, bestie!</p>
                        <div class="kia"></div>
                        <p>hmmm Kiana?</p>
                        <p>She said thank you, next.</p>
                    </div>
                </article>

            </main>
        </>

    )
}


export default Credits;



