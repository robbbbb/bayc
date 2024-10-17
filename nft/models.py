from django.db import models


# Create your models here.
class TransferEvent(models.Model):
    token_id = models.IntegerField()
    from_address = models.CharField(max_length=255)
    to_address = models.CharField(max_length=255)
    transaction_hash = models.CharField(max_length=255)
    block_number = models.IntegerField()

    def __str__(self):
        return self.token_id
