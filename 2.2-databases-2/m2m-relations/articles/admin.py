from django.contrib import admin

from django.core.exceptions import ValidationError

from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image', ]
    list_filter = ['title', 'text', 'published_at', 'image', ]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tags_name', ]
    list_filter = ['tags_name', ]

class ScopeInline(admin.TabularInline):
    model = Scope
    extra =3
    

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            count += 1
           
            if form.cleaned_data['is_main'] and count == 1:
               return form.cleaned_data['is_main']
            elif  count == 0: 
                raise ValidationError('Статья без разделов')
            else: 
                raise ValidationError('Статья имеет лишь один главный раздел')

        return super().clean()   
    

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['is_main']
    inlines = [Scope,]


