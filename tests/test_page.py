import devjournal
from unittest import TestCase
from sqlalchemy.exc import IntegrityError


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
        self.p.md = '''# test\nthis is a paragraph'''
        self.p.name = 'test'
        self.p.save()

    def tearDown(self):
        devjournal.db.session.rollback()
        devjournal.db.session.delete(self.p)
        devjournal.db.session.commit()

    def test_page_present(self):
        r = self.app.get('/{0}'.format(self.p.name))
        self.assertEqual(r.status_code, 200)
        self.assertIn('<title>test</title>', r.data)
        self.assertIn('<h1>test</h1>', r.data)

    def test_page_not_present(self):
        r = self.app.get('/jreoigeriughrei')
        self.assertEqual(r.status_code, 404)

    def test_duplicate_name(self):
        p = devjournal.models.Page()
        p.md = ''
        p.name = 'test'
        self.assertRaises(IntegrityError, p.save)

    def test_modify(self):
        r = self.app.post('/test/edit', data={'page_name': 'test2',
                                              'page_content': '# test_modified'},
                          headers={'Content-Type': 'application/json; charset=utf-8'})
        self.assertEqual(r.status_code, 200)
        p = devjournal.models.Page.query.findall(name='test2').first()
        self.assertEqual(p.id, self.p.id)
        self.assertEqual(p.md, '# test_modified')
