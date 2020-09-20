from .models import Pill


ls = list(Pill.objects.all())
PILL_CHOICES = [v for v in i.values() for i in list(Pill.objects.all())]
