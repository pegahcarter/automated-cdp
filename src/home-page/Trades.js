import React from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css';
import cdp from '../assets/cdp.json'


const Trades = () => {
  return (
    <div style={{ paddingTop: '5%' }}>
      <ReactTable
        data={cdp.trades}
        defaultPageSize={5}
        columns={[{
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
        }]}
      />
    </div>
  );
}

export default Trades;
