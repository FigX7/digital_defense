from django.db import models


class Website(models.Model):
    """ Model to represent a Website model """

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'
        db_table = 'website'

    name = models.CharField(max_length=256)
    url = models.CharField(max_length=512)

    def __str__(self):
        return '{}'.format(self.name)


class Page(models.Model):
    """ Model to represent a Page model """

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        db_table = 'page'

    path = models.CharField(max_length=256)
    website_id = models.ForeignKey(
        Website, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}'.format(self.name)


class Vulnerability(models.Model):
    """ Model to represent a Vulnerabilities model """

    class Meta:
        verbose_name = 'Vulnerability'
        verbose_name_plural = 'Vulnerabilities'
        db_table = 'vulnerability'

    data = models.CharField(max_length=256)
    page_id = models.ForeignKey(
        Page, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}'.format(self.name)
