import React from 'react';

import data from './cdp.json';

const Summary = () => {
  return (
    <div>
      <pre>
        {JSON.stringify(data.summary, null, 2)}
      </pre>
    </div>

  );
}

export default Summary;
