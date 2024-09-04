from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Blogs,Comments,Portfolio,Project

# Register your models here.
@admin.register(Blogs)
class BlogsAdminModel(admin.ModelAdmin):
    list_display=('id','title','description','created_at','updated_at')



@admin.register(Comments)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ('id','comment_by','blogs','comment')



@admin.register(Portfolio)
class PortFolioAdminModel(admin.ModelAdmin):
    list_display=('id','image')


@admin.register(Project)
class ProjectAdminModel(admin.ModelAdmin):
    list_display = ('id','project_name','project_url','tech_used')