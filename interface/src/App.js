import React, { Component } from 'react';
import './App.css';
import ReactTable from 'react-table';
import 'react-table/react-table.css';
import Homepage from './home-page';
import cdp from './home-page/cdp.json';

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      loggedIn: true,
      actions: cdp.actions,
      trades: cdp.trades,
      summary: cdp.summary
    }
  }

  render() {
    return (
      <Homepage />
    )
  }

}

export default App;
