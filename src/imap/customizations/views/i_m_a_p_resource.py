# -*- coding: utf-8 -*-

# from imap.customizations import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IIMAPResource(Interface):
    """ Marker Interface for IIMAPResource"""


@implementer(IIMAPResource)
class IMAPResource(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('imap_resource.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
