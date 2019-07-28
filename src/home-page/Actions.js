import React from 'react'
import ReactTable from 'react-table';
import 'react-table/react-table.css';
import cdp from '../assets/cdp.json'


const Actions = () => {
  return (
    <div style={{ paddingTop: '5%' }}>
      <ReactTable
        data={cdp.actions}
        defaultPageSize={5}
        columns={[{
          Header: 'Action ID',
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
        }]}
      />
    </div>
  );
}

export default Actions;
