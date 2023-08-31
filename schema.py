from pydantic import BaseModel


class SocrBase(BaseModel):
    IID: int
    LEVEL: int
    SCNAME: str
    SOCRNAME: str
    KOD_T_ST: str

class Kladr(BaseModel):
    IID: int
    CODE: str
    NAME: str
    SOCR: str
    INDEX: str
    GNINMB: str
    UNO: str
    OCATD: str
    STATUS: int

class Street(BaseModel):
    IID: int
    CODE: str
    NAME: str
    SOCR: str
    INDEX: str
    GNINMB: str
    UNO: str
    OCATD: str
    
class FieldList(BaseModel):
    FieldName: str

# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pass
