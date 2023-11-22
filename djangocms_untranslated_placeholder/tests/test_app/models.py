from cms.models import CMSPlugin, PlaceholderField, PlaceholderRelationField
from cms.utils.placeholder import get_placeholder_from_slot
from django.db import models
from django.utils.functional import cached_property


class TestPluginModel(CMSPlugin):
    field1 = models.CharField(max_length=64, default='', blank=False)
    field_date = models.DateField(default=None, null=True, )
    field_datetime = models.DateTimeField(default=None, null=True, )
    field_time = models.TimeField(default=None, null=True, )

    def __str__(self):
        return self.field1


class TestModel(models.Model):
    field0 = models.CharField(max_length=64, default='', blank=True)
    field1 = models.CharField(max_length=64, default='', blank=False)
    field2 = models.CharField(max_length=64, default='', blank=True)

    def __str__(self):
        return self.field1


class TestInlineModel(models.Model):
    testmodel = models.ForeignKey(TestModel, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=64, default='', blank=False)
    field2 = models.CharField(max_length=64, default='', blank=True)

    def __str__(self):
        return self.field1


class ModelWithPlaceholderField(models.Model):
    text = models.CharField(max_length=64, default='', blank=True)
    placeholders = PlaceholderRelationField()

    def __str__(self):
        return self.text

    @cached_property
    def my_placeholder(self):
        return get_placeholder_from_slot(self.placeholders, "content1")
