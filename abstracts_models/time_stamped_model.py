from django.db import models

class TimeStampedModel(models.Model):
    """
    Modèle abstrait fournissant des champs de timestamp
    pour la création et la dernière mise à jour.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True