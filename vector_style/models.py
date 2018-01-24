from django.db import models
from django.contrib.postgres.fields import JSONField
from leaflet_storage.models import DataLayer


class Styles(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False, verbose_name='Название стиля')
    style = JSONField(null=False, blank=False, verbose_name='Описание стиля')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()

    class Meta:
        managed = True
        verbose_name = 'Стили отображения слоёв'
        ordering = ['title']


class DatalayerStyles(models.Model):
    datalayer = models.ForeignKey(DataLayer, models.CASCADE, null=False, blank=False, verbose_name='Слой')
    styles = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.datalayer)

    def __unicode__(self):
        return self.__str__()

    class Meta:
        managed = True
        verbose_name = 'Настройка стилей слоёв'
        ordering = ['datalayer__description']