from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import DateRangeField, ArrayField
from django.db import models


class DocumentTag(models.Model):
    id = models.SlugField(primary_key=True)

    def __str__(self):
        return self.id

    def title(self) -> str:
        return self.id.split('.')[-1]


class Document(models.Model):

    document = models.FileField(upload_to='documents/%Y/%m/%d')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    reference_period = DateRangeField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.day.strftime('%Y-%m-%d'))


class DocumentShare(models.Model):
    base_user_ids = ArrayField(
        models.IntegerField(),
        default=list,
    )
    base_group_ids = ArrayField(
        models.IntegerField(),
        default=list,
    )
    user_ids = ArrayField(
        models.IntegerField(),
        default=list,
    )
    group_ids = ArrayField(
        models.IntegerField(),
        default=list,
    )
    permissions = ArrayField(
        models.CharField(),
        default=list,
    )
    superuser = models.BooleanField(default=True)
    granted_permissions = models.CharField()
