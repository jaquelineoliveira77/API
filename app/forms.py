from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class EscolhaCidade(FlaskForm):
    cidades = open("app\process\cidades.txt", 'r').readlines()
    choices = []
    for i in cidades:
        city = (i,i)
        choices.append(city)
    
    cidade = SelectField(u'cidade', choices=choices)
    submit = SubmitField('Sign In')

