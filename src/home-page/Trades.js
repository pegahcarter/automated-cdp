import React from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';
import cdp from './cdp.json'

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
    Header: 'Side',
    accessor: 'side',
    width: 100
  },
  {
    Header: 'USD',
    accessor: 'usd'
  },
  {
    Header: 'Price',
    accessor: 'price'
  },
  {
    Header: 'ETH',
    accessor: 'eth'
  }
]

const Trades = () => {
  return (
    <div>
      <ReactTable
        columns={columns}
        data={cdp.trades}
        defaultPageSize={5}
      >
      </ReactTable>
    </div>
  );
}

export default Trades;
