from django.core.management.base import BaseCommand, CommandError
from ...models import DeviceModel


class Command(BaseCommand):
    help = "Creates devices in DB."

    def handle(self, *args, **options):

        devices = ["device-1", "device-2", "device-5"]
        for device in devices:
            DeviceModel.objects.create(name=device)

        self.stdout.write(self.style.SUCCESS("Successfully created devices"))
