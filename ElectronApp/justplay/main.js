const {app, BrowserWindow} = require('electron');

let mainWindow;

app.on('ready', () => {
  mainWindow = new BrowserWindow({
      height: 580,
      width: 800, 
      webPreferences: {
      	nodeIntegration: true
      }
  });

  mainWindow.loadURL('file://' + __dirname + '/index.html');
});
