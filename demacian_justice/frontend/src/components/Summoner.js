import React, { Component } from "react";
import queryString from 'query-string'
const axios = require('axios');

class Summoner extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: {},
            loaded: false,
            queryParams: queryString.parse(this.props.location.search)
        };
    }

    componentDidMount() {
        let { name, server } = this.state.queryParams;
        axios.get(`/karma/get_summoner?name=${name}&server=${server}`)
            .then(response => {
                if (response.status > 400) {
                    return this.setState(() => {
                        return { placeholder: "Something went wrong!" };
                    });
                }
                return response.data;
            })
            .then(data => {
                this.setState(() => {
                    return {
                        data,
                        loaded: true
                    };
                });
            })
            .catch(e => {
                console.log(e)
            });

    }

    render() {
        let divName = 'summoner-table'
        let imageName = 'circular-icon'
        let attrsName = 'summoner-attributes-container'
        let icon = `http://ddragon.leagueoflegends.com/cdn/10.8.1/img/profileicon/${this.state.data.profileIconId}.png`
        return (
            <div className={divName}>
                <img className={imageName} src={icon} alt='summoner icon' height='200' width='200'></img>
                <div className={attrsName}>
                    <ul>
                        <li>Name: {this.state.data.name}</li>
                        <li>Level: {this.state.data.summonerLevel}</li>
                    </ul>
                </div>
            </div>
        );
    }
}

export default Summoner;