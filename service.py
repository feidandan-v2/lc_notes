from flask import Flask

# 创建 Flask 应用实例
app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    定义一个路由处理函数，当访问 '/' 路径时返回 "Hello, World!"。
    """
    return 'Hello, World!'

if __name__ == '__main__':
    # 设置监听的主机和端口
    host = 'localhost'
    port = 8002

    # 启动 Flask 应用
    app.run(host=host, port=port, debug=True)
