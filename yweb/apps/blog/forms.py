# coding: utf-8

from yweb.forms import Form
from wtforms import BooleanField, StringField, \
    validators, DateTimeField, TextAreaField, IntegerField, \
    PasswordField, FileField, SelectField

from wtforms.validators import ValidationError


class ImindEditForm(Form):

    title = StringField( _('Title'), [
        validators.Length(min=2, max=256) ] )

    abstract = TextAreaField( _('Abstract'), [
        validators.Length(min=2, max=1024) ] )

    body = TextAreaField( _('Body'), [
        validators.Length(min=6, max=1024*1024) ] )

    ispublic = BooleanField( _('Is Public ?') )
