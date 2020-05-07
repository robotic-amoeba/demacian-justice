import React, { Component } from "react";
import { Redirect } from "react-router-dom";

class SearchBar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            inputValue: '',
            selectValue: 'EUW1',
            redirect: false
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSelectChange = this.handleSelectChange.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        this.setState({ redirect: true })
    };

    handleInputChange(event) {
        this.setState({ inputValue: event.target.value });
    };

    handleSelectChange(event) {
        this.setState({ selectValue: event.target.value });
    };

    render() {
        let containerName = 'summonerSearchBar'
        let path = `/profile?name=${this.state.inputValue}&server=${this.state.selectValue}`
        return this.state.redirect ? <Redirect to={path} /> : (
            <div className={containerName}>
                <form onSubmit={this.handleSubmit}>
                    <input id="inputSummoner" onChange={this.handleInputChange} type="text" placeholder="Summoner Name" name="name" />
                    <select id="server" onChange={this.handleSelectChange} name="server" defaultValue='EUW1'>
                        <option value="BR1">BR1</option>
                        <option value="EUN1">EUN1</option>
                        <option value="EUW1">EUW1</option>
                        <option value="LA1">LA1</option>
                        <option value="LA2">LA2</option>
                        <option value="NA1">NA1</option>
                        <option value="OCE">OCE/OC1</option>
                        <option value="RU1">RU1</option>
                        <option value="TR1">TR1</option>
                        <option value="JP1">JP1</option>
                        <option value="KR">KR</option>
                        <option value="PBE">PBE</option>
                    </select>
                    <button><img src="https://img.icons8.com/search" alt="search icon" height='23px' onClick={this.handleSubmit} /></button>
                </form>
            </div>
        )
    }

}

export default SearchBar;
