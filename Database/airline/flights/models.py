from django.db import models
class Airport(models.Model):
    code = models.CharField(max_length =3)
    city = models.CharField(max_length =64)


    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    ### This will be changed to Forgien Key 
    origin =  models.ForeignKey(Airport, on_delete = models.CASCADE, related_name = "departures")
    destination = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name = "arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"