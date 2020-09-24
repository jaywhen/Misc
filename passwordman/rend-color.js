const btn = this.document.querySelector('#btn')
const BrowserWindow = require('electron').remote.BrowserView

window.onload = function() {
    btn.onclick = ()=>{
        newWin = new BrowserWindow({
            width: 700,
            height: 600
        })

    }
}