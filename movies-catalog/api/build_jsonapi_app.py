from fastapi import FastAPI
from fastapi_jsonapi import ApplicationBuilder

from api.generic_view import GenericView
from models import Movie
from schemas import (
    MovieCreateSchema,
    MovieSchema,
    MovieUpdateSchema,
)


def build_jsonapi_app(app: FastAPI) -> ApplicationBuilder:
    builder = ApplicationBuilder(
        app=app,
        prefix="/api",
        tags=["API"],
    )
    builder.add_resource(
        path="/movies",
        tags=["Movies"],
        resource_type="movie",
        view=GenericView,
        model=Movie,
        schema=MovieSchema,
        schema_in_post=MovieCreateSchema,
        schema_in_patch=MovieUpdateSchema,
    )
    return builder
