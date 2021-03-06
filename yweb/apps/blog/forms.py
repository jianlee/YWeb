# coding: utf-8

from wtforms import BooleanField, StringField, \
    validators, DateTimeField, TextAreaField, IntegerField, \
    PasswordField, FileField, SelectField

from wtforms.validators import ValidationError

from yweb.forms import Form
from yweb.utils.translation import ugettext_lazy as _


class ArticleEditForm(Form):

    title = StringField( _('Title'), [
        validators.Length(min=2, max=256) ] )

    abstract = TextAreaField( _('Abstract'), [
        validators.Length(min=2, max=1024) ] )

    markup = SelectField(
        _('Markup Language'), coerce=int, default=1,
        choices=[(1, 'Markdown'),
                 (2, 'reStructuredText')] )

    body = TextAreaField( _('Body'), [
        validators.Length(min=6, max=1024*1024) ] )

    is_public = BooleanField( _('Is Public ?') )


class PostEditForm(Form):

    body = TextAreaField( _('Body'), [
        validators.Length(min=6, max=1024*1024) ] )

