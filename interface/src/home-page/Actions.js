import React from 'react';
import ReactDOM from 'react-dom';

import CustomTable from './CustomTable';

import data from './cdp.json';


const Actions = () => {
  return (
    <div>
      Actions
      <CustomTable data={data.actions} />
    </div>
  );
}

export default Actions;
