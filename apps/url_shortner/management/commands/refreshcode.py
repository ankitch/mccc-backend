from django.core.management.base import BaseCommand

from apps.url_shortner.models import ShortenedUrl


class Command(BaseCommand):
    help = 'Refreshes all the Shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return ShortenedUrl.objects.refresh_shortcode(items=options['items'])
