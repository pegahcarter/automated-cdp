import React, { Component } from 'react';

import Homepage from './home-page'

class App extends Component {

  state = {
    loggedIn: true
  };

  constructor(props) {
    super(props);
  }

  render() {
    let { loggedIn } = this.state;
    return (
      <Homepage />
    )
  }

}

export default App;
