import React, { Component } from 'react';
import goodKarma from '../../public/good-karma.svg'
import badKarma from '../../public/bad-karma.svg'

class RatingBar extends Component {
    constructor(props) {
        super(props)
        this.rateFn = this.rateFn.bind(this);
    }

    rateFn (event) {
        this.props.handleRate(event, this.props.puuid)
    }

    render() {
        const upvotes = this.props.upvotes;
        const downvotes = this.props.downvotes;

        return (

            <div className='rating-bar'>
                <div className='score' id='upvotes'>{upvotes}</div>
                <button data-vote='upvote' onClick={this.rateFn} id='upbutton' >
                </button>
                <button data-vote='downvote' onClick={this.rateFn} id='downbutton'>
                </button>
                <div className='score' id='downvotes'>{downvotes}</div>
            </div>
        )
    }
}

export default RatingBar;
