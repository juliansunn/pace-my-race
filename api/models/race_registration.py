from django.db import models


class RaceRegistration(models.Model):
    user = models.ForeignKey("api.User", on_delete=models.CASCADE)
    race = models.ForeignKey("api.Race", on_delete=models.CASCADE)
    registration_time = models.DateTimeField(auto_now_add=True)
    # Add any other fields related to registration details, such as payment status, bib number, etc.
