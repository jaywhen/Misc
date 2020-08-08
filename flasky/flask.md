```
py -3 -m venv venv
//激活
venv\Scripts\activate
//安装
pip install Flask
//powershell
$env:FLASK_APP = "hello.py"
flask run

//cmd
set FLASK_APP=hello.py
flask run

//linux
export FLASK_APP=hello.py
flask run

//VSCODE
ctrl+shift+p
python选择解析器
&&
terminal也要进入虚拟环境
```

