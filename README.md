# QS-dataviewer
Dataviewer for quicSim-docker output

## Build

We used NodeJS for this project. After cloning, the modules can be installed with `npm`

```npm install```

## Run

To run the server, use `npm start`: this starts the server on port `8080`.

The server allows `metric.json` files to be uploaded (Max. one) to show the data in tables. Data files can be found here: https://github.com/moonfalir/quic-cc-testresults

The row of buttons can be used to Show/Hide columns. It is also possible to click the column on each table to show the test results with the median value for that column.

Rows can also be filtered and shown again with the `Show all rows` button.
