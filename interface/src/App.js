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
      actions: cdp.actions,
      trades: cdp.trades,
      summary: cdp.summary
    }
  }

  render() {
    const columns = [
      {
        Header: 'Trade ID',
        accessor: 'id',
        width: 100
      },
      {
        Header: 'Date',
        accessor: 'date'
      },
      {
        Header: 'Action',
        accessor: 'action',
        sortable: false,
        width: 125
      },
      {
        Header: 'ETH-USD',
        accessor: 'eth-usd',
        sortable: false,
        width: 100
      },
      {
        Header: 'Quantity',
        accessor: 'quantity',
        sortable: false,
      }
    ]
    return (
      // <Homepage />
      <ReactTable
        columns={columns}
        data={this.state.actions}
        defaultPageSize={5}
      >

      </ReactTable>
    )
  }

}

export default App;
