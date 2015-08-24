#-*- coding:utf8 -*-
import devjournal
from unittest import TestCase


class TestPage(TestCase):
    @classmethod
    def setUpClass(cls):
        devjournal.app.config['TESTING'] = True
        devjournal.app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:////tmp/unittests_db'
        devjournal.db.create_all()

    @classmethod
    def tearDownClass(cls):
        import os
        os.remove(devjournal.app.config['SQLALCHEMY_DATABASE_URI'][len('sqlite:///'):])

    def setUp(self):
        self.app = devjournal.app.test_client()
        self.p = devjournal.models.Page()
        self.cat = devjournal.models.Category()
        self.cat.name = "testing"
        self.cat.save()
        self.p.md = '''# test\nthis is a paragraph'''
        self.p.name = 'test'
        self.p.categories.append(self.cat)
        self.p.save()

    def tearDown(self):
        devjournal.db.session.rollback()
        devjournal.db.session.delete(self.p)
        try:
            devjournal.db.session.delete(self.p2)
        except AttributeError:
            pass
        devjournal.db.session.delete(self.cat)
        devjournal.db.session.commit()

    def test_unique_tag_search(self):
        """Test wether we are correctly redirected, since there's only one result."""
        r = self.app.get('/search?q=tag:{0}'.format(self.cat.name))
        self.assertEqual(r.status_code, 302)

    def test_unique_name_search(self):
        """Test wether a name: search is correctly redirected to the only result."""
        r = self.app.get('/search?q=name:{0}'.format(self.p.name))
        self.assertEqual(r.status_code, 302, r.data)

    def test_multi_tag_search(self):
        """test wether we get correct results when there's two pages."""
        self.p2 = devjournal.models.Page()
        self.p2.md = '''# test 2\nThis is a paragraph, and it's okay.'''
        self.p2.name = "test2"
        self.p2.categories.append(self.cat)
        self.p2.save()

        r = self.app.get('/search?q=tag:{0}'.format(self.cat.name))
        self.assertEqual(r.status_code, 200)
        self.assertIn('<li><a href="/{0}">{1}</a></li>'.format(self.p.name,
                                                               self.p.name), r.data)
        self.assertIn('<li><a href="/{0}">{1}</a></li>'.format(self.p2.name,
                                                               self.p2.name), r.data)

# TODO: test multi_name_search(self):
# TODO: test multi_without_foreign_search(self): wether even with and other un-LIKE name, the name doesn't show up
