const express = require('express');
const cors = require('cors')
const app = express();
app.use(cors());
var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"
app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress +
':' + iPortaTcp));
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/paperino', (req, res) => {
    console.log("Mi hai chiesto di salutarti");
    res.sendFile("formSemplice.html", { root: './htdoc' });
    });

app.get('/gestisciDatiForm', (req, res) => {
    console.log(req.query.fname);
    res.send("<html>Buona serata "+req.query.fname+"</html>");
    });

app.get('/pippo', (req, res) => {
    console.log("Mi hai la pagina che invia file");
    res.sendFile("sendfile.html", { root: './htdoc' });
    });

app.post("/mansendfile",(req,res) => {
    p=req.query.password
    if (p=="paperino")
        res.send("<html>Troppo figo</html>");
    else
        res.send("<html>Muori</html>");
});
