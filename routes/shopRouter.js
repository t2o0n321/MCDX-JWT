const express = require('express')
const router = express.Router()
const verifyJWT = require('../middlewares/verifyJWT')
const goodsdata = require('../utils/goodsdata')

router.get('/', function(req, res, next) {
    var userinfo = verifyJWT.verify(req.cookies.token)
    if (userinfo) {
        res.render('shop', { toShow: userinfo['user'] })
    } else {
        res.render('shop', { toShow: '登入' })
    }
})

router.get('/buy/:id', function(req, res, next) {
    var userinfo = verifyJWT.verify(req.cookies.token)
    if (userinfo) {
        res.render('buy', { toShow: userinfo['user'], toBuy: req.params.id })
    } else {
        res.status(404).send('please login first')
    }
})

router.get('/buy/:name/cash', function(req, res, next) {
    var userinfo = verifyJWT.verify(req.cookies.token)
    if (userinfo) {
        var usercredit = userinfo['credit']
        var price = goodsdata[req.params.name]['price']

        // not enough
        if (usercredit <= price) {
            res.render('buyalert')
        } else {
            var flag = '<div>N3v3R_PUt_c0nf1d3nT_!nfo_ins!de_jwt_token_and_pass_to_cookie</div>'
            res.send(flag)
        }

    } else {
        res.status(404).send('please login first')
    }
})

module.exports = router