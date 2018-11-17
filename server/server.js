const express        = require('express');
const MongoClient    = require('mongodb').MongoClient
const db             = require('./config/db');
const cors           = require('cors');
const app            = express();

const port = 8001;

app.use(cors());

MongoClient.connect(db.url, { useNewUrlParser: true }, (err, database) => {
    if (err) return console.log(err)
                        
    d2 = database.db("veritasalpha");
    require('./app/routes')(app, d2);
    app.listen(port, () => {
      console.log('We are live on ' + port);
    });               
  });