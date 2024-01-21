const express = require('express');
const mysql = require('mysql');
const app = express();
const port = 3000;

// MySQL database connection
const connection = mysql.createConnection({
    host: '127.0.0.1',
    user: 'root',
    password: 'Cancer_0716', 
    database: 'gwc_email_collector'
});

connection.connect((err) => {
    if (err) throw err;
    console.log('Connected to MySQL Database!');
    
});

app.use(express.urlencoded({ extended: true }));

app.use(express.static('public'));

app.get('/', (req, res) => {
    res.send(`
    <html>
            <head>
                <title>BUGWC Attendance</title>
                <link rel="stylesheet" type="text/css" href="/css/style.css">
            </head>
            <body>
                <header>
                    
                </header>
                <img src="/css/frontend_elements/gwcbu_logo.png" alt="gwcLogo" class="top-left-image">
                <div class="form-container"> 
                    <form action="/submit-email" method="post" >
                        <div class="icon-container">
                            <img src="/css/frontend_elements/nameIcon.png" alt="nameIcon" class="icon">
                            <input type="name" id="name" name="name" placeholder="Name" required>
                        </div>
                        <div class="icon-container">
                            <img src="/css/frontend_elements/emailIcon.png" alt="emailIcon" class="icon">
                            <input type="email" id="email" name="email" placeholder="BU Email" required>
                        </div>
                        <button type="submit">Submit</button>
                    </form>
                </div>
                <footer id="main-footer">
                  
                </footer>
            </body>
    </html>
`);
});


app.post('/submit-email', (req, res) => {
    const email = req.body.email;
    const name = req.body.name;
    
    const query = 'INSERT INTO emailList (email) VALUES (?)';

    connection.query(query, [email], (err, result) => {
        if (err) {
            console.error('Error executing query:', err);
            return res.status(500).send('Error saving email');
        }
        res.send(`
        <html>
            <head>
                <title>Thank you for attending!</title>
                <link rel="stylesheet" type="text/css" href="/css/style.css">
            </head>
        
            <body>
                <p>Thank you for attending the event, ${name}!</p>
            </body>
        </html>
        `);
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

