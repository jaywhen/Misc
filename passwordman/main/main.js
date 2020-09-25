// Modules to control application life and create native browser window
const {app, BrowserWindow} = require('electron')
const path = require('path')

function createWindow () {
  const mainWindow = new BrowserWindow({
    width: 700,
    height: 500,
    webPreferences: {
      //preload: path.join(__dirname, 'preload.js')
      nodeIntegration: true
    }
    
  })
  mainWindow.loadFile('./render/color.html')
  // Open the DevTools.
  mainWindow.webContents.openDevTools()

}

app.whenReady().then(() => {
  createWindow()
  require('./menu.js')
  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})
