// Add Restify to your project
const restify = require('restify')

// Create new server object
let server = restify.createServer()

/*
 * Here is a definition for an endpoint at /names accessabile when using HTTP
 * GET. The first argument is the path you want the GET endpoint to be available
 * at. The second argument is a callback function that recieves a req object
 * representing the clients request to this endpoint. The req object will
 * include things like the clients IP, params & headers sent and time. The
 * callback function also recieves a res object which represents the response
 * that will be sent back to the client. In the callback you can program the
 * response to have the headers, response body etc etc that you require your
 * endpoint to respond.
 */

server.get('/names', function(req, res) {
  res.json({
    names: [
      'joanne',
      'jim',
      'john',
      'jess'
    ]
  })
})

/*
 *
 * Request:
 * curl http://localhost:8080/names
 *
 * Response:
 * {"names":["joanne","jim","john","jess"]}
 *
 */

// Let your server listen on the port passed in (8080). You can add a callback
// as a second argument that runs when your server starts
server.listen(8080)

