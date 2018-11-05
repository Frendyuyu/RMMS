from flask import Flask, render_template, request, g, session
import config

app = Flask(__name__)
app.config.from_object(config)


# 将 GET,POST 加入到请求方式中
@app.route("demo12", methods=["get", "post"])
def demo12():
    # 获取通过url中传入的参数如：http://127.0.0.1:5000/demo12?mane=qwe
    # 中"?"后的name=qwe
    # 打印结果如：ImmutableMultiDict([('mane', 'qwe')])
    if request.args:
        print(request.args)
    # 获取从form表单中提交的数据
    # 打印结果如：ImmutableMultiDict([('asd', 'asd')])
    if request.form:
        print(request.form)
    # 获取请求数据
    # 打印结果如：b'qweqwe'
    if request.data:
        print(request.data)
    # 获取json类型的数据
    # 打印结果如：{'name': 'nihao'}
    if request.json:
        print(request.json)
    # 获取传入文件pic,并打印该文件名,并保存为12.png
    # 打印结果如下：第一行为data的打印结果，返回值为"保存成功"
    # ImmutableMultiDict([('pic', <FileStorage: '2018-08-07 16-54-02屏幕截图.png' ('image/png')>)])
    # <FileStorage: '2018-08-07 16-54-02屏幕截图.png' ('image/png')>
    if request.files:
        pic = request.files.get('pic')
        print(pic)
        pic.save('./12.png')
        return '保存成功'
    return "查看控制台"
