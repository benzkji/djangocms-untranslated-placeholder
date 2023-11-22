from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from modeltranslation.admin import TranslationAdmin

from djangocms_untranslated_placeholder.tests.test_app.models import TestPluginModel, ModelWithPlaceholderField


class TestPlugin(TranslationAdmin, CMSPluginBase):
    model = TestPluginModel
    render_template = 'test_app/testplugin.html'

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context.update({
            'object_list': ModelWithPlaceholderField.objects.all()
        })
        print(context)
        return context


plugin_pool.register_plugin(TestPlugin)
