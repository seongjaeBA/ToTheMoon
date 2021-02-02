from django.contrib import admin
import blogttm.models as Post

# Register your models here.


admin.site.register(Post.PostSubject)
# @admin.register(Post.PostSubject)
# class PostSubject(admin.ModelAdmin):
#     pass

# admin.site.register(Post.DjangoBlog)
@admin.register(Post.DjangoContentsModels)
class Django(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

@admin.register(Post.GitModels)
class Git(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

@admin.register(Post.DataAnalysisModels)
class DataAnalysis(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

@admin.register(Post.CaseStudyModels)
class CaseStudy(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

@admin.register(Post.CloudModels)
class Cloud(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

