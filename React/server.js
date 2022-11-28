const express = require('express');
const cors = require('cors')
const app = express();

app.use(cors());

app.use('/Sign-in', (req, res) => {
  res.send({
    token: 'testing'
  });
});

app.listen(3000, () => console.log('API is running on http://localhost:3000/Sign-in'));