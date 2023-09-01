from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

kladr_site_router = APIRouter(prefix='/kladr/site')

templates = Jinja2Templates(directory="templates")

from data_socrbase import (
    get_pyd_socrbase_data,
    #get_pyd_socrbase_data_paged,
    #get_socrbase_recordcount,
    #get_socrbase_fieldnames,
)


@kladr_site_router.get("/", response_class=HTMLResponse)
def site_root():
    return """
    <html>
        <head>
            <title>Kladr Fastapi Demo</title>
        </head>
        <body>
            <h1>Welcome to Kladr</h1>
        </body>
    </html>
"""


@kladr_site_router.get("/socrbase")
def socrbase(request: Request):
    #return get_pyd_socrbase_data()
    return templates.TemplateResponse("template.html",
                                      {"request": request}
                                    )


# -------------------------------------------------------------------------------------------------
if __name__ == "__main__": pass