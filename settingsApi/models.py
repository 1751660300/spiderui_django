from django.db import models
import json


# Create your models here.
class settings(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, unique=True)
    desc = models.CharField(max_length=500, blank=True)

    def getJson(self):
        return {"id": self.id, "name": self.name, "desc": self.desc}


class setting_details(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    pid = models.IntegerField(blank=True)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=2000)
    desc = models.CharField(max_length=500, blank=True)
    sid = models.ForeignKey(settings, on_delete=models.CASCADE)

    def getJson(self):
        return {"id": self.id, "name": self.name, "desc": self.desc, "value": self.value, "sid": self.sid.id,
                "pid": self.pid}
