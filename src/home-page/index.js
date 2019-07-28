import React from 'react';

import Summary from './Summary'
import Actions from './Actions'
import Trades from './Trades'

const Homepage = ({ loggedIn }) => {
  return (
    <div style={{ padding: '5%' }}>
      <Summary />
      <Actions />
      <Trades />
    </div>
  )
}

export default Homepage;
