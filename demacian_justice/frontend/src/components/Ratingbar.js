import React from 'react';
import goodKarma from '../../public/good-karma.svg'
import badKarma from '../../public/bad-karma.svg'



const RatingBar = (props) => {
    const rateFn = (event)=>{props.handleRate(event, props.puuid)}
    const upvotes = props.upvotes;
    const downvotes = props.downvotes;

    return (

        <div className='rating-bar'>
            <div className='score' id='upvotes'>{upvotes}</div>
            <button data-vote='upvote' onClick={rateFn} id='upbutton' >
            </button>
            <button data-vote='downvote' onClick={rateFn} id='downbutton'>
            </button>
            <div className='score' id='downvotes'>{downvotes}</div>
        </div>
    )
}

export default RatingBar;
