from typing import ClassVar

from fastapi import Depends
from fastapi_jsonapi.misc.sqla.generics.base import ViewBaseGeneric
from fastapi_jsonapi.views import Operation, OperationConfig
from pydantic import BaseModel, ConfigDict
from sqlalchemy.ext.asyncio import AsyncSession

from models import db_helper


class AllViewsDependencies(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )
    session: AsyncSession = Depends(db_helper.session_getter)


def extract_datalayer_kwargs(
    view: ViewBaseGeneric,
    dto: AllViewsDependencies,
):
    return {
        "session": dto.session,
    }


class GenericView(ViewBaseGeneric):
    operation_dependencies: ClassVar = {
        Operation.ALL: OperationConfig(
            dependencies=AllViewsDependencies,
            prepare_data_layer_kwargs=extract_datalayer_kwargs,
        ),
    }
