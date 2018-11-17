const routes = require('./routes');
module.exports = function(app, db) {
  routes(app, db);
  // future route groups here
};