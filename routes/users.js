const express = require('express');
const router = express.Router();
const verifyJWT = require('../middlewares/verifyJWT')

router.get('/', function(req, res, next) {
    res.send('respond with a resource');
});

router.get('/profile', function(req, res, next) {
    if (verifyJWT.verify(req.cookies.token)) {
        var userInfo = verifyJWT.verify(req.cookies.token)
        if (userInfo['privilege'] == 1)
            res.render('user_profile', { role: '特 A 級', userName: userInfo['user'], toShow: userInfo['user'], credit: userInfo['credit'] })
        else {
            res.render('user_profile', { role: 'F 級', userName: userInfo['user'], toShow: userInfo['user'], credit: userInfo['credit'] })
        }
    } else {
        res.status(404).send('please login fisrt')
    }
})

module.exports = router;