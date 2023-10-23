# -*- coding: utf-8 -*-

# from imap.customizations import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IWhereWeWorkPage(Interface):
    """ Marker Interface for IWhereWeWorkMain"""


@implementer(IWhereWeWorkPage)
class WhereWeWorkPage(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('where_we_work_main.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
