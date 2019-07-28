import React from 'react';

import Summary from './Summary'
import Actions from './Actions'
import Trades from './Trades'

const Homepage = ({ loggedIn }) => {
  return (
    <div>
      <Summary />
      <Actions />
      <Trades />
    </div>
  )
}

export default Homepage;
