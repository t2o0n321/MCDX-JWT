const { exec } = require('child_process')

function nslookup(domain, fn){
    exec('nslookup ' + domain).stdout.on('data', function(data){
        fn(data)
    })
}

module.exports = {
    nslookup: nslookup,   
}
