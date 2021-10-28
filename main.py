from flask import Flask,render_template,request,session
from utils import *
from inspect import isfunction
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'OH ITS A SECRET!'


@app.route('/',methods=['GET'])
def index():
    items = [
    (name, eval(api_prefix+name).comment)
    for name in api_list
    ]
    return render_template(
        'index.html',
        items = items
        )


@app.route('/api/<func>',methods=['GET','POST'])
def api(func):

    if func not in api_list:
        return render_template('404.html'), 404
    
    form_in = eval(api_prefix + func)()
    form_out = ResultForm()
 
    if form_in.validate_on_submit():
        form_out.result.data = form_in.run()

    return render_template(
        'form.html',
        name = func,
        form_in = form_in,
        form_out = form_out
        )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

