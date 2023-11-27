# -*- coding: utf-8 -*-

# from imap.customizations import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface
from plone import api
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


#from sinar.miscbehavior import _

from datetime import datetime as dt
from pandas import pandas as pd
 
class IImapResource(Interface):
    """ Marker Interface for IIMAPResource"""    

@implementer(IImapResource)
class ImapResource(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('imap_resource.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()

    # def partners(self):
    #     partners = self.context.implementing_partners()
    #     return partners
    

    def partners(self):
        results = []
        brains = api.content.find(context=self.context, portal_type='Organization')
        for brain in brains:
            partner = brain.getObject()
            results.append({
                'title': brain.Title,
                'description': brain.Description,
                'uuid': brain.UID,
                })
        return results

    def created_date(self):
        time = pd.to_datetime(self.context.created)

        if self.context.created:
            for t in time:         
                return t.dt.strftime("%a, %d %b %Y")
        else:  
            return

    def sdg_title(self):

        factory = getUtility(IVocabularyFactory,
                             'sinar.miscbehavior.SDGGoals')

        vocabulary = factory(self.context.SDG_goals)
        
        for term in vocabulary:
            if self.context.SDG_goals:
                return term.title
            else:
                return None

    def country_title(self):


        factory = getUtility(IVocabularyFactory,
                             'collective.vocabularies.iso.countries')

        vocabulary = factory(self.context.countries)
        for term in vocabulary:
            return term.title
