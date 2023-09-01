from fastapi import APIRouter

kladr_api_router = APIRouter(prefix='/kladr/api')

from data_socrbase import (
    get_pyd_socrbase_data,
    get_pyd_socrbase_data_paged,
    get_socrbase_recordcount,
    get_socrbase_fieldnames,
)
from data_kladr import (
    get_pyd_kladr_data,
    get_kladr_recordcount,
    get_pyd_kladr_data_paged,
)

@kladr_api_router.get("/")
def hello():
    return {"hello": "hello from FastAPI"}


@kladr_api_router.get("/socrbase")
def socrbase() -> list:
    return get_pyd_socrbase_data()


# http://127.0.0.1:8000/socrbase_paged?page_size=20&current_page=1
@kladr_api_router.get("/socrbase_paged")
def socrbase_paged(
    page_size: int = 20, current_page: int = 1, level: int | None = None
) -> list:
    return get_pyd_socrbase_data_paged(
        page_size=page_size, current_page=current_page, level=level
    )


@kladr_api_router.get("/socrbase_recordcount")
def socrbase_recordcout() -> int:
    return get_socrbase_recordcount()


@kladr_api_router.get("/socrbase_fieldlist")
def socrbase_fieldlist() -> list[str]:
    return get_socrbase_fieldnames()


@kladr_api_router.get("/kladr")
def kladr() -> list:
    return get_pyd_kladr_data()


@kladr_api_router.get("/kladr_paged")
def kladr_paged(
    page_size: int = 20, current_page: int = 1, status: int | None = None
) -> list:
    return get_pyd_kladr_data_paged(
        page_size=page_size, current_page=current_page, status=status
    )


@kladr_api_router.get("/kladr_recordcount")
def kladr_recordcout() -> int:
    return get_kladr_recordcount()


# -------------------------------------------------------------------------------------------------
if __name__ == "__main__": pass