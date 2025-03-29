from fastapi import FastAPI
from fastapi_jsonapi import ApplicationBuilder

from api.generic_view import GenericView
from models import (
    AgeRating,
    Genre,
    Movie,
)
from schemas import (
    AgeRatingCreateSchema,
    AgeRatingSchema,
    AgeRatingUpdateSchema,
    GenreCreateSchema,
    GenreSchema,
    GenreUpdateSchema,
    MovieCreateSchema,
    MovieSchema,
    MovieUpdateSchema,
)


def build_jsonapi_app(
    app: FastAPI,
) -> ApplicationBuilder:
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
    builder.add_resource(
        path="/age-ratings",
        tags=["Age Ratings"],
        resource_type="age-rating",
        view=GenericView,
        model=AgeRating,
        schema=AgeRatingSchema,
        schema_in_post=AgeRatingCreateSchema,
        schema_in_patch=AgeRatingUpdateSchema,
        model_id_field_name="name",
    )
    builder.add_resource(
        path="/genres",
        tags=["Genre"],
        resource_type="genre",
        view=GenericView,
        model=Genre,
        schema=GenreSchema,
        schema_in_post=GenreCreateSchema,
        schema_in_patch=GenreUpdateSchema,
    )
    return builder
