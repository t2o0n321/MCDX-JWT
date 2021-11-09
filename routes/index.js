const express = require('express');
const router = express.Router();
const authRouter = require('../routes/authRouter').createRouter({})
const adminRouter = require('../routes/adminRouter').createRouter({})

router.use('/api/auth', authRouter)
router.use('/admin', adminRouter)

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index');
});

module.exports = router;