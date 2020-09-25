const btn = this.document.querySelector('#btn')
const BrowserWindow = require('electron').remote.BrowserWindow

window.onload = function() {
    btn.onclick = ()=>{
        newWin = new BrowserWindow({
            width: 400,
            height: 600
        })

        newWin.loadFile('./render/coloros.html')
        newWin.on('closed', ()=>{
            newWin = null
        })

    }  
}

window.addEventListener('contextmenu', function(){
    alert('clicked')
  })