const express = require('express')
const router = express.Router()
const verifyJwt = require('../middlewares/verifyJWT')
const tools = require('../middlewares/admintool')

function createRouter(dependencies) {
    var {} = dependencies
    router.route('/ctrl')
        .get(function(req, res) {
            var token = verifyJwt.verify(req.cookies.token)

            if (!token) {
                res.status(404).send(`You don't have permission to access this page`)
            } else {
                var privilege = token['privilege']
                var user = token['user']
                if (privilege === 0) {
                    res.status(404).send(`You don't have permission to access this page`)
                } else {
                    res.render('./admin/ctrlPanel', { toShow: user })
                }
            }
        })
        .post(function(req, res) {
            var token = verifyJwt.verify(req.cookies.token)

            if (!token) {
                res.location('/api/auth/login')
                res.redirect('/api/auth/login')
            } else {
                var privilege = token['privilege']
                var user = token['user']
                if (privilege === 0) {
                    res.status(404).send(`You don't have permission to access this page`)
                } else {
                    var domain = req.body.domain
                    try {
                        tools.nslookup(domain, (data) => {
                            res.render('./admin/ctrlPanel', { toShow: user, nsResult: data })
                        })
                    } catch (e) {
                        res.render('./admin/ctrlPanel', { toShow: user, nsResult: '' })
                    }
                }
            }
        })
    return router
}

module.exports = {
    createRouter: createRouter,
}