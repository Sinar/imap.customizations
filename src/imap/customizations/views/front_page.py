# -*- coding: utf-8 -*-

# from imap.customizations import _
from Products.Five.browser import BrowserView
from zope.interface import Interface
from plone import api

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IFrontPage(Interface):
    """ Marker Interface for IFrontPage"""


class FrontPage(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('front_page.pt')

    def latest_news(self):
        news = api.content.find(portal_type='News Item')
        return news

    def latest_activities(self):
        news = api.content.find(portal_type='Activity')
        return news

    def latest_resources(self):
        news = api.content.find(portal_type='Resource')
        return news

    def __call__(self):
        # Implement your own actions:
        return self.index()
