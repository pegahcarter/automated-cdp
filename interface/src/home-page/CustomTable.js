import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
  },
  paper: {
    marginTop: theme.spacing(3),
    width: '100%',
    overflowX: 'auto',
    marginBottom: theme.spacing(2),
  },
  table: {
    minWidth: 650,
  },
}));

const CustomTable = (data) => {
  const classes = useStyles();
  var keys = Object.keys(data)
  var tableData = []

  for (var i=0; i=data.length; i++) {
    var row = []
    keys.forEach(function(key, i) {
      row.push(data[i][key])
    });
    tableData.push(row);
  }

  return (
    <div className={classes.root}>
      <Paper className={classes.paper}>
        <Table className={classes.table} size="small">
          <TableHead>
            <TableRow>
              {keys.map(key => (
                <TableCell>{key}</TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {tableData.map(row => (
              <TableRow key={row.id}>
              <TableCell component="th" scope="row">
                row.id
              </TableCell>
              {row.map(value => (
                <TableCell>{row[value]}</TableCell>
              ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </Paper>
    </div>
  );
}

export default CustomTable;
