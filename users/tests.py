from django.core.management import call_command
from django.test import TestCase


class CommandsTestCase(TestCase):

    def test_mycommand(self):
        """ Тестирование создания суперпользователя """

        args = []
        opts = {}
        call_command('create_super_user', *args, **opts)
