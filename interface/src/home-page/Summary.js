import React from 'react';

import { JsonToTable } from "react-json-to-table";

import data from './cdp.json';

const Summary = () => {
  return (
    <div>
      Summary
      <pre>
        <JsonToTable json={data['summary']} />
      </pre>
    </div>

  );
}

export default Summary;
