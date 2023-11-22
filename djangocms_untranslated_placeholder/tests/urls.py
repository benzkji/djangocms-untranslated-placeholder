"""URLs to run the tests."""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import re_path, path
from django.views import static

from djangocms_untranslated_placeholder.tests.test_app.views import ModelWithPlaceholderDetailView

admin.autodiscover()

urlpatterns = [
]

urlpatterns += i18n_patterns(
    path(
        "detail/<int:pk>/",
        ModelWithPlaceholderDetailView.as_view(),
        name="detailview",
    ),
    re_path('^admin/', admin.site.urls),
    re_path(r'^', include('cms.urls')),
)


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    ]
