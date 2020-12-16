from django.db import models

class YieldPerKwp(models.Model):
    state = models.CharField("State", max_length=50)
    yield_kWp = models.IntegerField("Yield in kWh/kWp/a")

    def __str__(self):
        return self.state + ": " + str(self.yield_kWp)

