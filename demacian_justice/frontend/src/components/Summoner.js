import React, { Component } from "react";
import Error from './Error';
import RatingBar from './Ratingbar';
import queryString from 'query-string';
const axios = require('axios');


class Summoner extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: {},
            error: {},
            loaded: false,
            queryParams: queryString.parse(this.props.location.search)
        };
    }

    componentDidMount() {
        let { name, server } = this.state.queryParams;
        axios.get(`/karma/get_summoner?name=${name}&server=${server}`)
            .then(response => {
                this.setState(() => {
                    return {
                        data: response.data,
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
        let voteSentiment = event.target.dataset.vote
        axios.post('/karma/vote', {
            vote: voteSentiment,
            summoner_uuid: puuid
        })
        .then((response)=>{
            console.log(response)
        })
        .catch(error => {
            if (error.response && error.response.status > 400) {
                    return { error: error.response };
            }
            console.log(error)
        });
    }

    render() {
        if (this.state.error.status) {
            return <Error error={this.state.error} />
        }

        let divName = 'summoner-table';
        let imageName = 'circular-icon';
        let attrsName = 'summoner-attributes-container';
        let icon = `http://ddragon.leagueoflegends.com/cdn/10.8.1/img/profileicon/${this.state.data.profileIconId}.png`;
        return (
            <div>
                <div className={divName}>
                    <img className={imageName} src={icon} alt='summoner icon' height='200' width='200'></img>
                    <div className={attrsName}>
                        <ul>
                            <li>Name: {this.state.data.name}</li>
                            <li>Level: {this.state.data.summonerLevel}</li>
                        </ul>
                    </div>
                </div>
                <RatingBar puuid={this.state.data.puuid} handleRate={this.handleRate}/>
            </div>
        );
    }
}

export default Summoner;
