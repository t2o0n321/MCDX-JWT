const express = require('express');
const router = express.Router()
var userdata = require('../utils/userdata')
var conf = require('../utils/jwtconfig')
const jwt = require('jsonwebtoken')

function createRouter(dependencies) {
    const {} = dependencies
    router.get('/login', function(req, res, next) {
        res.render('login')
    })
    router.post('/login/v', function(req, res, next) {
        var user = req.body.userName
        var password = req.body.password
        var token = verifyUser(user, password)
        if (token.length != 0) {
            res.cookie('token', token, {
                httpOnly: true,
                maxAge: conf.settings['jwt_expire_in'],
                sameSite: 'strict'
            })
            res.location('/shop')
            res.redirect('/shop')
        } else {
            res.redirect('/api/auth/login')
        }
    })
    router.get('/logout', function(req, res, next) {
        res.clearCookie('token')
        res.location('/shop')
        res.redirect('/shop')
    })
    return router;
}

function verifyUser(user, password) {
    if (userdata.info[user] != undefined) {
        if (userdata.info[user]['password'] === password) {
            const token = jwt.sign(userdata.info[user], conf.settings['jwt_key'], { expiresIn: conf.settings['jwt_expire_in'] })
            return token
        }
    }
    return ''
}

module.exports = {
    createRouter: createRouter
}