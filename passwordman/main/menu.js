const {Menu, BrowserWindow} = require('electron')
var template = [
    {
        label: '文件(F)',
        submenu: [
            {label: '导入excel'},
            {label: '导入json'}
        ]
    },
    {
        label: '关于(A)',
        submenu: [
            {
                label: 'passwordman',
                accelerator: 'ctrl + n',
                click: ()=>{
                    var win = new BrowserWindow({
                        width: 300,
                        height: 200,
                        webPreferences: {nodeIntegration: true}
                    })
                    win.loadFile('./render/about.html')
                    win.on('closed', ()=>{
                        win = null
                    })
                }
            },
            {label: '关于作者'}
        ]
    }
]

var m = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(m)