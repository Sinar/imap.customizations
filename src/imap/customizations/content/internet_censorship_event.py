#-*- coding: utf-8 -*-

from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from plone.app.z3cform.widget import SelectFieldWidget
from plone.namedfile.field import NamedBlobImage
import pandas as pd

# from imap.customizations import _

# Importing Citizenlab category list

df = pd.read_csv('https://raw.githubusercontent.com/citizenlab/test-lists/master/lists/00-LEGEND-new_category_codes.csv')
citizenlab_category_list = df.iloc[:,0].to_list()

class IInternetCensorshipEvent(model.Schema):
    """ Marker interface and Dexterity Python Schema for InternetCensorshipEvent
    """

    description = RichText(
         title=u'Description of internet censorship event',
         required=False
    )

    event_date = schema.Date(
        title='Date event occured',
        required=True,
    )
    
    lead_image = NamedBlobImage(
        title="Lead image",
        required=False,
    )

    directives.widget(category=SelectFieldWidget)
    category = schema.List(
        title=u'Category of websites/app blocked',
        description=u'Based on CitizenLab category',
        required=False,
        value_type=schema.Choice(
            values=citizenlab_category_list
        ),
        missing_value=u'',
    )

    blocked_websites = schema.List(
        title=u'Blocked website(s)',
        description=u'URLs of website(s) blocked',
        value_type=schema.URI(),
        required=False,
        missing_value=u'',
    )

    blocked_apps = schema.List(
        title=u'Blocked apps',
        description=u'URLs of app(s) blocked',
        value_type=schema.TextLine(),
        required=False,
        missing_value=u'',
    )
    
@implementer(IInternetCensorshipEvent)
class InternetCensorshipEvent(Container):
    """ Content-type class for IInternetCensorshipEvent
    """
