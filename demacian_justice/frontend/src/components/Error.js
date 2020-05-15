import React, { Component } from "react";
import amumuLogo from '../../public/amumu_icon.png';

class Error extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: this.props.error
        };
    };

    render() {
        let errorContainer = 'errorContainer';
        return (
            <div className={errorContainer}>
                <img src={amumuLogo} alt='error icon' height='500' width='698'></img>
                <p>{this.state.error.status + " " + this.state.error.statusText}</p>
            </div>
        );
    }
};

export default Error;