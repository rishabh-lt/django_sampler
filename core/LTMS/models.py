# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

####################
# check how enums work in django
###################

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Browser(models.Model):
    browser_id = models.CharField(primary_key=True, max_length=35)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    type_ind = models.CharField(max_length=7, blank=True, null=True)
    status_ind = models.CharField(max_length=8, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name+"-"+self.type_ind

    class Meta:
        managed = False
        db_table = 'browser'


class BrowserVersion(models.Model):
    browser_version_id = models.CharField(primary_key=True, max_length=35)
    browser = models.ForeignKey(Browser, models.DO_NOTHING)
    version_no = models.CharField(max_length=50)
    code = models.CharField(max_length=255)
    architecture = models.CharField(max_length=2)
    build = models.CharField(max_length=35, blank=True, null=True)
    beta_ind = models.IntegerField(blank=True, null=True,default=0,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ])
    latest_ind = models.IntegerField(blank=True, null=True,default=0,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ])
    popular_ind = models.IntegerField(blank=True, null=True,default=0,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ])
    status_ind = models.CharField(max_length=8, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.code

    class Meta:
        managed = False
        db_table = 'browser_version'


class Os(models.Model):
    os_id = models.CharField(primary_key=True, max_length=35)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    os_type = models.CharField(max_length=7)
    status_ind = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self) -> str:
        return self.name+"-"+self.os_type


    class Meta:
        managed = False
        db_table = 'os'


class OsBrowser(models.Model):
    os_browser_id = models.BigAutoField(primary_key=True)
    os_version = models.ForeignKey('OsVersion', models.DO_NOTHING)
    browser_version = models.ForeignKey(BrowserVersion, models.DO_NOTHING)
    use_in_realtime = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ])
    use_in_screenshot = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ])
    use_in_responsive = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ])
    status_ind = models.CharField(max_length=8, blank=True, null=True)
    allow_for_freemium = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ])

    def __str__(self) -> str:
        return str(self.os_version) +"-"+ str(self.browser_version)

    class Meta:
        managed = False
        db_table = 'os_browser'


class OsVersion(models.Model):
    os_version_id = models.CharField(primary_key=True, max_length=35)
    os = models.ForeignKey(Os, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    code = models.CharField(max_length=80, blank=True, null=True)
    architecture = models.CharField(max_length=2)
    status_ind = models.CharField(max_length=8, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


    class Meta:
        managed = False
        db_table = 'os_version'
