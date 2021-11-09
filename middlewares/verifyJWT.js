const jwt = require('jsonwebtoken')
const conf = require('../utils/jwtconfig')

function VerifyJwt(jwt_token) {
    if (!jwt_token) {
        return false
    }
    return jwt.verify(jwt_token, conf['settings']['jwt_key'])
}

module.exports = {
    verify: VerifyJwt
}