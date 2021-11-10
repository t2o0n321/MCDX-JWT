var container = document.getElementsByClassName('container')[0]
var u = document.getElementById('userName')
var p = document.getElementById('password')

function inputIsNull() {
    return (u.value == '' || p.value == '')
}

function checker() {
    removeFormerAlert()
    if (inputIsNull()) {
        var alertBar = document.createElement('div')
        alertBar.id = 'alert'
        alertBar.classList.add('alert')
        alertBar.classList.add('alert-danger')
        alertBar.innerText = 'Both user name and password is needed !'
        container.appendChild(alertBar)
        return false
    }
    return true
}

function removeFormerAlert() {
    try {
        container.removeChild(document.getElementById('alert'))
    } catch (e) {}
}