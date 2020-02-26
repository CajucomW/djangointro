from django.test import TestCase

class NavigationLinksTestCase(TestCase):

    def test_does_about_link_work(self):
        response = self.client.get('/')
        self.assertContains(response, 'wence.')
        self.assertContains(response, '/')

    def test_does_tech_link_work(self):
        response = self.client.get('/tech')
        self.assertContains(response, '...in training')
        self.assertContains(response, '/tech')

    def test_does_repo_link_work(self):
        response = self.client.get('/repos')
        self.assertContains(response, 'GitHub Repositories')
        self.assertContains(response, '/repos')

    def test_do_repos_appear(self):
        response = self.client.get('/repos')
        self.assertContains(response, 'CajucomW/basicstate')

    def test_does_pta_link_work(self):
        response = self.client.get('/pta')
        self.assertContains(response, 'Cajucom, PTA')
        self.assertContains(response, '/pta')

    def test_does_jiujitsu_link_work(self):
        response = self.client.get('/jiujitsu')
        self.assertContains(response, 'formiga')
        self.assertContains(response, '/jiujitsu')