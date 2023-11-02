from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="backend API",
        default_version="v1",
        description="Esta API-REST es un ejercicio para una evaluación.",
    ),
    public=False,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("users/", include("users.urls")),
    path("", include("core.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            "",
            RedirectView.as_view(pattern_name="schema-swagger-ui"),
            name="go-to-docs",
        )
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
