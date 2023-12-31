from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline, TranslationStackedInline, TranslationAdmin

from .models import TestModel, TestInlineModel, ModelWithPlaceholderField


class TestInlineModelInline(TranslationStackedInline, admin.StackedInline):
    model = TestInlineModel
    extra = 2


class TestInlineModelInline2(TranslationTabularInline, admin.TabularInline):
    model = TestInlineModel
    extra = 2


class TestModelAdmin(TranslationAdmin, admin.ModelAdmin):
    inlines = [TestInlineModelInline, TestInlineModelInline2, ]
    fieldsets = [
        ['', {'fields': ['field0', ]}],
        ['First Set', {'fields': ['field1', 'field2']}],
    ]


admin.site.register(TestModel, TestModelAdmin)



class ModelWithPlaceholderFieldAdmin(admin.ModelAdmin):
    pass


admin.site.register(ModelWithPlaceholderField, ModelWithPlaceholderFieldAdmin)


