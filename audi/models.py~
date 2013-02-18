from django.db import models
from django.contrib import admin

# Create your models here.

class Audi(models.Model):
    title = models.CharField(max_length=60)
    audio_file = models.FileField(upload_to = u'audi_files/', max_length=200)
    created = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class Remark(models.Model):
	author = models.CharField(max_length=60)
	body = models.TextField(max_length=60)
	created = models.DateField(auto_now_add=True)
	audi = models.ForeignKey(Audi)
	def __unicode__(self):
		return self.body
	    
class RemarkInline(admin.StackedInline):
	model = Remark
	extra = 1

class AudiAdmin(admin.ModelAdmin):
	list_display = ('title','created')
	search_fields = ('title',)
	list_filter = ('created',)
	inlines = [RemarkInline]
	def __unicode__(self):
		return self.list_display

class RemarkAdmin(admin.ModelAdmin):
	list_display = ('audi','author','body','created')
	search_fields = ('author','body')
	list_filter = ('created','author')
	def __unicode__(self):
		return self.list_display

admin.site.register(Audi,AudiAdmin)
admin.site.register(Remark,RemarkAdmin)
