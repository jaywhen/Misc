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

//对外可见
flask run --host=0.0.0.0
//修改默认端口
flask run --port=端口号
//硬重载（忽略缓存并刷新页面）
Ctrl+F5 || Shift+F5

```



> 过滤器：
>
> - 变量|过滤器
>
> - ```
>   {% filter upper %}
>   	some text
>   {% endfilter %}
>   # 将这段文字转换为大写
>   ```
>
> - 