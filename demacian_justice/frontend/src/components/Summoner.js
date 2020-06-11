import React, { Component } from "react";
import Error from './Error';
import RatingBar from './Ratingbar';
import queryString from 'query-string';
const axios = require('axios');


class Summoner extends Component {
    constructor(props) {
        super(props);
        this.state = {
            summoner: {},
            error: {},
            loaded: false,
            queryParams: queryString.parse(this.props.location.search)
        };
        this.handleRate = this.handleRate.bind(this);
    }

    componentDidMount() {
        let { name, server } = this.state.queryParams;
        axios.get(`/karma/get_summoner?name=${name}&server=${server}`)
            .then(response => {
                this.setState(() => {
                    return {
                        summoner: response.data,
                        loaded: true
                    };
                });
            })
            .catch(error => {
                if (error.response && error.response.status > 400) {
                    return this.setState(() => {
                        return { error: error.response };
                    });
                }
                console.log(error)
            });

    }

    handleRate (event, puuid) {
        let voteSentiment = event.target.dataset.vote;
        let state = this.state
        axios.post('/karma/vote', {
            vote: voteSentiment,
            summoner_uuid: puuid
        })
        .then((response)=>{
            this.setState(
                {summoner: Object.assign(state.summoner, response.data)}
            )
        })
        .catch(error => {
            if (error.response && error.response.status > 400) {
                    return { error: error.response };
            }
            console.log(error);
        });
    }

    karmaColor(){
        let karma = this.state.summoner.karma;
        let karmaClass;
        if (karma > 75) {
            karmaClass = "good-karma";
        } else if (karma < 25) {
            karmaClass = "bad-karma";
        } else {
            karmaClass = "neutral-karma";
        }
        return karmaClass;
    }

    render() {
        if (this.state.error.status) {
            return <Error error={this.state.error} />
        }

        let divName = 'summoner-table';
        let imageName = 'circular-icon';
        let attrsName = 'summoner-attributes-container';
        let icon = `http://ddragon.leagueoflegends.com/cdn/10.8.1/img/profileicon/${this.state.summoner.profileIconId}.png`;

        let karmaClass = this.karmaColor();


        return (
            <div>
                <div className={divName} id='good-score'>
                    <img className={imageName} src={icon} alt='summoner icon' height='200' width='200'></img>
                    <div className={attrsName}>
                        <ul>
                            <li>Name: {this.state.summoner.name}</li>
                            <li>Level: {this.state.summoner.summonerLevel}</li>
                            <li id="karma" className={karmaClass}>{this.state.summoner.karma}</li>
                        </ul>
                    </div>
                </div>
                <RatingBar puuid={this.state.summoner.puuid} handleRate={this.handleRate}
                           upvotes={this.state.summoner.upvotes}  downvotes={this.state.summoner.downvotes}/>
            </div>
        );
    }
}


export default Summoner;
