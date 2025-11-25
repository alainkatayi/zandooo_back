from django.db import models


class SoftDeleteManager(models.Manager):
    def get_queryset(self):

        #filtre les object supprimé et renvoi seulement les disponibles
        return super().get_queryset().filter(deleted_at = None)