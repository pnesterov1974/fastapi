from pydantic import BaseModel


class SocrBase(BaseModel):
    IID: int
    Level: int
    ScName: str
    SocrName: str
    KodTST: int


class Kladr(BaseModel):
    IID: int
    Code: str
    Name: str
    Socr: str
    Index: str
    Gninmb: str
    Uno: str
    Ocatd: str
    Status: int


class Street(BaseModel):
    IID: int
    Code: str
    Name: str
    Socr: str
    Index: str
    Gninmb: str
    Uno: str
    Ocatd: str


class FieldList(BaseModel):
    FieldName: str


# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
