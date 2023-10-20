# -*- coding: utf-8 -*-
from imap.customizations.testing import IMAP_CUSTOMIZATIONS_FUNCTIONAL_TESTING
from imap.customizations.testing import IMAP_CUSTOMIZATIONS_INTEGRATION_TESTING
from imap.customizations.views.i_m_a_p_resource import IIMAPResource
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = IMAP_CUSTOMIZATIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_imap_resource_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='imap-resource'
        )
        self.assertTrue(IIMAPResource.providedBy(view))

    def test_imap_resource_not_matching_interface(self):
        view_found = True
        try:
            view = getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='imap-resource'
            )
        except ComponentLookupError:
            view_found = False
        else:
            view_found = IIMAPResource.providedBy(view)
        self.assertFalse(view_found)


class ViewsFunctionalTest(unittest.TestCase):

    layer = IMAP_CUSTOMIZATIONS_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
