import React from 'react'
import ReactTable from 'react-table';
import 'react-table/react-table.css';
import cdp from './cdp.json'

const columns = [
  {
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
  }
]

const Actions = () => {
  return (
    <div>
      <ReactTable
        columns={columns}
        data={cdp.actions}
        defaultPageSize={5}
      >
      </ReactTable>
    </div>
  );
}

export default Actions;
