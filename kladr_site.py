from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

kladr_site_router = APIRouter(prefix="/kladr/site")
templates = Jinja2Templates(directory="templates")

from data_socrbase import (
    get_pyd_socrbase_data,
    # get_pyd_socrbase_data_paged,
    # get_socrbase_recordcount,
    # get_socrbase_fieldnames,
)


@kladr_site_router.get("/", response_class=HTMLResponse)
def site_root(request: Request):
    return templates.TemplateResponse(
        "main.html", {"request": request}
        )


@kladr_site_router.get("/socrbase", response_class=HTMLResponse)
def socrbase(request: Request):
    # return get_pyd_socrbase_data()
    return templates.TemplateResponse("socrbase.html", {"request": request})


# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
