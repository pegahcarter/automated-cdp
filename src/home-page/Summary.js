import React from 'react';
import { JsonToTable } from "react-json-to-table";
import cdp from './cdp.json';

const Summary = () => {
  return (
    <div>
      <pre>
        <JsonToTable json={cdp.summary} />
      </pre>
    </div>

  );
}

export default Summary;
