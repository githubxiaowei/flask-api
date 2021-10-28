import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ResultForm(FlaskForm):
    result = TextAreaField('', 
        validators=[],
        render_kw = {
            "placeholder": "Show results here",
            "rows": 10,
            "readonly": "true"
        }
    )


class API_demo(FlaskForm):
    comment = 'API样例，输出等于输入'
    input_data = StringField('input', validators=[DataRequired()])
    submit = SubmitField('提交')
    
    def run(self,):
        return self.input_data.data


class API_sql_template(FlaskForm):
    comment = '返回输入sql的模板'
    input_data = TextAreaField('input', 
        validators=[DataRequired()],
        render_kw = {
            "placeholder": "输入SQL语句",
            "rows": 5,
        }
    )
    submit = SubmitField('提交')
    
    def run(self,):
        s = self.input_data.data
        s = s.strip().lower()
        s = re.sub(r'[\s]+', ' ', s)
        s = re.sub(r'values[\s]*\((.*)\)', 'values()', s)
        s = re.sub(r'[\s]+', ' ', s)
        s = re.sub(r'=[\s]*.*?\s+', '= ', s+' ')
        return s 
