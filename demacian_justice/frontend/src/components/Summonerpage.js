import React, {Component} from "react";
import Summoner from "./Summoner";

class SummonerPage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <div>
        <Summoner location={this.props.location}/>
      </div>
    )
  }
}

export default SummonerPage;
