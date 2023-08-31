import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
from data_street import get_pyd_street_data, get_street_recordcount

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#переименовать проект
#разделить на rout-ы
#api vs site, kladr vs gar
#git
#new env

@app.get("/")
def hello():
    return {"hello": "hello from FastAPI"}


@app.get("/socrbase")
def socrbase() -> list:
    return get_pyd_socrbase_data()


# http://127.0.0.1:8000/socrbase_paged?page_size=20&current_page=1
@app.get("/socrbase_paged")
def socrbase_paged(
    page_size: int = 20, current_page: int = 1, level: int | None = None
) -> list:
    return get_pyd_socrbase_data_paged(
        page_size=page_size, current_page=current_page, level=level
    )


@app.get("/socrbase_recordcount")
def socrbase_recordcout() -> int:
    return get_socrbase_recordcount()


@app.get("/socrbase_fieldlist")
def socrbase_fieldlist() -> list[str]:
    return get_socrbase_fieldnames()


@app.get("/kladr")
def kladr() -> list:
    return get_pyd_kladr_data()


@app.get("/kladr_paged")
def kladr_paged(
    page_size: int = 20, current_page: int = 1, status: int | None = None
) -> list:
    return get_pyd_kladr_data_paged(
        page_size=page_size, current_page=current_page, status=status
    )


@app.get("/kladr_recordcount")
def kladr_recordcout() -> int:
    return get_kladr_recordcount()


@app.get("/street")
def kladr() -> list:
    return get_pyd_street_data()


@app.get("/street_recordcount")
def kladr_recordcout() -> int:
    return get_street_recordcount()


# uvicorn kladr:app --reload
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("kladr:app", reload=True)
