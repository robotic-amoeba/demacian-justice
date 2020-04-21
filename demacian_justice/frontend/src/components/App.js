import React, { Component } from "react";
import { render } from "react-dom";

import Summoner from "./Summoner"

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      placeholder: "Loading"
    };
  }

  render() {
    return (
    <div><Summoner/></div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
