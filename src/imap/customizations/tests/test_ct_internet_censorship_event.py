# -*- coding: utf-8 -*-
from imap.customizations.content.internet_censorship_event import IInternetCensorshipEvent  # NOQA E501
from imap.customizations.testing import IMAP_CUSTOMIZATIONS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class InternetCensorshipEventIntegrationTest(unittest.TestCase):

    layer = IMAP_CUSTOMIZATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_internet_censorship_event_schema(self):
        fti = queryUtility(IDexterityFTI, name='Internet censorship event')
        schema = fti.lookupSchema()
        self.assertEqual(IInternetCensorshipEvent, schema)

    def test_ct_internet_censorship_event_fti(self):
        fti = queryUtility(IDexterityFTI, name='Internet censorship event')
        self.assertTrue(fti)

    def test_ct_internet_censorship_event_factory(self):
        fti = queryUtility(IDexterityFTI, name='Internet censorship event')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IInternetCensorshipEvent.providedBy(obj),
            u'IInternetCensorshipEvent not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_internet_censorship_event_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Internet censorship event',
            id='internet_censorship_event',
        )

        self.assertTrue(
            IInternetCensorshipEvent.providedBy(obj),
            u'IInternetCensorshipEvent not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('internet_censorship_event', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('internet_censorship_event', parent.objectIds())

    def test_ct_internet_censorship_event_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Internet censorship event')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_internet_censorship_event_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Internet censorship event')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'internet_censorship_event_id',
            title='Internet censorship event container',
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
