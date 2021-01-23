from django.contrib import admin
import blogttm.models as Post

# Register your models here.


admin.site.register(Post.PostSubject)
# @admin.register(Post.PostSubject)
# class PostSubject(admin.ModelAdmin):
#     pass

# admin.site.register(Post.DjangoBlog)
@admin.register(Post.DjangoContents)
class Django(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

@admin.register(Post.Git)
class Git(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

@admin.register(Post.DataAnalysis)
class DataAnalysis(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

@admin.register(Post.CaseStudy)
class CaseStudy(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

@admin.register(Post.Cloud)
class Cloud(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

