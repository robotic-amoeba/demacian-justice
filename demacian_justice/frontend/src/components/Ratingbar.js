import React from 'react';
import goodKarma from '../../public/good-karma.svg'
import badKarma from '../../public/bad-karma.svg'



const RatingBar = (props) => {
    const rateFn = (event)=>{props.handleRate(event, props.puuid)}
    return (

        <div className='rating-bar'>
            <button data-vote='upvote' onClick={rateFn}>
                <img data-vote='upvote' src={goodKarma} height='40px' alt='good karma icon' />
            </button>
            <div className='score'>54</div>
            <button data-vote='downvote' onClick={rateFn}>
                <img data-vote='downvote' src={badKarma} height='40px' alt='bad karma icon'/>
            </button>
        </div>
    )
}

export default RatingBar;