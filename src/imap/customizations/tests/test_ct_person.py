# -*- coding: utf-8 -*-
from imap.customizations.content.person import IPerson  # NOQA E501
from imap.customizations.testing import IMAP_CUSTOMIZATIONS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class PersonIntegrationTest(unittest.TestCase):

    layer = IMAP_CUSTOMIZATIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_person_schema(self):
        fti = queryUtility(IDexterityFTI, name='Person')
        schema = fti.lookupSchema()
        self.assertEqual(IPerson, schema)

    def test_ct_person_fti(self):
        fti = queryUtility(IDexterityFTI, name='Person')
        self.assertTrue(fti)

    def test_ct_person_factory(self):
        fti = queryUtility(IDexterityFTI, name='Person')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPerson.providedBy(obj),
            u'IPerson not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_person_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Person',
            id='person',
        )

        self.assertTrue(
            IPerson.providedBy(obj),
            u'IPerson not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('person', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('person', parent.objectIds())

    def test_ct_person_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Person')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_person_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Person')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'person_id',
            title='Person container',
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
