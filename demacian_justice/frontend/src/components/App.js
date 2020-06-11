import React, { Component } from "react";
import { render } from "react-dom";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import SummonerPage from "./SummonerPage"
import SearchBar from "./Searchbar"

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      placeholder: "Loading"
    };
  }

  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route
              exact path="/profile"
              component={SummonerPage}
            />
            <Route
              path="/"
              component={SearchBar}
            />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
