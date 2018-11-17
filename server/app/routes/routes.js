var ObjectID = require('mongodb').ObjectID;
const bodyParser     = require('body-parser');

module.exports = function(app, db) {
    app.post('/query', bodyParser.json(), (req, res) => {
        const details = { '_id': new ObjectID(req.body.query) }
        db.collection('veritas').findOne(details, (err, item) => {
        if (err) {
            console.log(err);
            res.send({'error':'An error has occurred'});
        } 
        else {
            res.send(item);
        }
        });
    });
}