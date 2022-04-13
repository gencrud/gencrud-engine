from django.urls import reverse

from catalog.models.catalog_image import CatalogImage
from gen.abstract.models import AbstractMPTTPageSeoModel
from gen.catalog.strings import URL_PREFIX_CATALOG, BASE_CATALOG_VERBOSE_NAME


class BaseCatalogModel(AbstractMPTTPageSeoModel):
    class Meta:
        abstract = True
        verbose_name = BASE_CATALOG_VERBOSE_NAME
        verbose_name_plural = BASE_CATALOG_VERBOSE_NAME

    def get_images(self):
        return CatalogImage.objects.filter(catalog_id=self.pk, catalog__is_show=True)

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse(URL_PREFIX_CATALOG, kwargs=kwargs)