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
    r="<html>Buona serata "+req.query.fname;
    if (req.query.fsesso =="1")
        r+="<br>Sei un Uomo"
    else if (req.query.fsesso =="2")
        r+="<br>Sei una Donna"
    else
        r+="<br>Non hai specificato il tuo sesso"
    r+="<br>Sei nato nel comune: "+req.query.fcomune+"</html>"
    res.send(r)
    });

app.post('/gestisciDatiForm', (req, res) => {
    console.log(req.body.fname);
    r="<html>Buona serata "+req.query.fname;
    if (req.body.fsesso =="1")
        r+="<br>Sei un Uomo"
    else if (req.body.fsesso =="2")
        r+="<br>Sei una Donna"
    else
        r+="<br>Non hai specificato il tuo sesso"
    r+="<br>Sei nato nel comune: "+req.body.fcomune+"</html>"
    res.send(r)
    });

app.get('/sendfile', (req, res) => {
    console.log("Mi hai chiesto la pagina per inviare file");
    res.sendFile("sendfile.html", { root: './htdoc' });
    });

app.post("/mansendfile",(req,res) => {
    p=req.body.password
    if (p=="paperino")
        res.send("<html>Troppo figo</html>");
    else
        res.send("<html>Muori</html>");
});
