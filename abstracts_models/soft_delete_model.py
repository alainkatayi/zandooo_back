from django.db import models
from django.utils import timezone
class SoftDeleteModel(models.Model):
    """
    Modèle abstrait fournissant une fonctionnalité de suppression douce (soft delete).
    Au lieu de supprimer physiquement les enregistrements de la base de données,
    ils sont marqués comme supprimés via le champ `is_deleted`.
    """
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """
        Surcharge de la méthode delete pour effectuer une suppression douce.
        """
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """
        Méthode pour restaurer un enregistrement supprimé.
        """
        self.deleted_at = None
        self.save()