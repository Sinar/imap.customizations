# -*- coding: utf-8 -*-
from imap.customizations.testing import IMAP_CUSTOMIZATIONS_FUNCTIONAL_TESTING
from imap.customizations.testing import IMAP_CUSTOMIZATIONS_INTEGRATION_TESTING
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

    def test_front_page_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='front-page'
        )
        self.assertTrue(view.__name__ == 'front-page')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in front-page'
        # )

    def test_front_page_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='front-page'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = IMAP_CUSTOMIZATIONS_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
