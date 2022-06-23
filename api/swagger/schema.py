from rest_framework import permissions
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os


class SchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super(SchemaGenerator, self).get_schema(request, public)
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Management Server API",
        default_version='v1',
        contact=openapi.Contact(email="itadmin@enertiv.com"),
    ),
    public=True,
    urlconf="api.urls",
    generator_class=SchemaGenerator,
)
