var fs = require('fs')
window.onload = function() {
    var btn = this.document.querySelector('#btn')
    var thedatas = this.document.querySelector('#thedatas')
    btn.onclick = function() {
        fs.readFile('thedatas.txt', (err, data)=>{
            thedatas.innerHTML = data
        })
    }

}