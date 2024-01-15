const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse the incoming request body
app.use(express.urlencoded({ extended: true }));

// Route for the landing page
app.get('/', (req, res) => {
    res.send(`
        <form action="/submit-email" method="post">
            <label for="email">Enter your BU Email:</label>
            <input type="email" id="email" name="email" required>
            <button type="submit">Submit</button>
        </form>
    `);
});

// Route to handle form submission
app.post('/submit-email', (req, res) => {
    const email = req.body.email;
    // Here, you would typically add code to insert the email into a database
    console.log(email); // Just for demonstration purposes
    res.send('Email received: ' + email);
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
