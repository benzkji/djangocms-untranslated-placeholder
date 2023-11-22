from django.views.generic import DetailView

from djangocms_untranslated_placeholder.tests.test_app.models import ModelWithPlaceholderField


class ModelWithPlaceholderDetailView(DetailView):
    model = ModelWithPlaceholderField
