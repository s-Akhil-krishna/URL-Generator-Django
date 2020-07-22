from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL


class Command(BaseCommand):
    help = 'Refreshes all the shortcodes'

    #No of shortcodes to refresh
    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    #call refresh shortcodes
    def handle(self, *args, **options):
        number = options['items']
        return KirrURL.objects.refresh_codes(number)