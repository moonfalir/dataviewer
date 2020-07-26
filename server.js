const express = require('express');
const bodyParser= require('body-parser')
const multer = require('multer');
const app = express();
const upload = multer({
    dest: 'public/'
})
const fs = require('fs')

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.urlencoded({extended: true}))


// index page 
app.get('/', function(req, res) {
    res.sendFile(__dirname + '/public/index.html')
});

app.post('/upload', upload.single('metricsFile'),  function(req, res, next) {
    const file = req.file
    if (!file) {
        const error = new Error('Please upload a file')
        error.httpStatusCode = 400
        return next(error)
    }
    let tempFile = fs.readFileSync(__dirname + "/" + file.path)
    fs.writeFileSync(__dirname + '/public/metrics.json', tempFile)
    fs.unlink(__dirname + "/" + file.path, (err) => {
        if (err) {
            const error = new Error('Please upload a file')
            error.httpStatusCode = 400
            return next(error)
        }
        res.redirect('/')
    })
})

app.listen(8080);
console.log('8080 is the magic port');