# 所有导出信息
from flask import Flask

app = Flask(__name__)
# 初始化配置
app.config.from_pyfile('app.conf')

from Gakigram import views, models



