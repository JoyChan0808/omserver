from django.db import models

class ServerFunCateg(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    server_categ_name = models.CharField(max_length=60)
    class Meta:
        db_table = u'server_fun_categ'


class ServerList(models.Model):
    server_name = models.CharField(max_length=39,primary_key=True)
    server_wip = models.CharField(max_length=45)
    server_lip = models.CharField(max_length=36)
    server_op = models.CharField(max_length=30)
    server_app_id = models.IntegerField()
    class Meta:
        db_table = u'server_list'


class ModuleList(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    module_name = models.CharField(max_length=60)
    module_caption = models.CharField(max_length=255)
    module_extend = models.CharField(max_length=2000)
    class Meta:
        db_table = u'module_list'

class ServerAppCateg(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') 
    server_categ_id = models.IntegerField()
    app_categ_name = models.CharField(max_length=90)
    class Meta:
        db_table = u'server_app_categ'
