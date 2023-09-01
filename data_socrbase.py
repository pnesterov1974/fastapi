from sqlalchemy import create_engine, text

from schema import SocrBase, FieldList

CONNECTION_STR = r"mssql+pymssql://sa:Exptsci123@192.168.1.78/kladr2"

####### 1-st LEVEL defs  Iter & GetRecordCount

def iter_socrbase_data():
    eng = create_engine(CONNECTION_STR)
    sql = """
    SELECT TOP(15)
       ROW_NUMBER() OVER(ORDER BY [Pid]) AS [IID],
       [Level],
       [ScName],
       [SocrName],
       [KodTST]
    FROM [dbo].[SocrBase];
    """
    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)


def iter_socrbase_data_paged(
    page_size: int, current_page: int, level: int | None = None
):
    eng = create_engine(CONNECTION_STR)

    filter_where_str = None
    if level:
        filter_where_str = f"WHERE [Level] = {level}"

    sql = f"""
    WITH [SocrBase] AS
	(
	SELECT ROW_NUMBER() OVER (ORDER BY [Pid]) AS [IID],
		   [Level],
		   [ScName],
		   [SocrName],
		   [KodTST]
	FROM [dbo].[SocrBase]
    @WHERE
	)
	SELECT [IID],
	       [Level],
		   [ScName],
		   [SocrName],
		   [KodTST]
	FROM [SocrBase]
	WHERE [IID] BETWEEN (({current_page} - 1) * {page_size}) AND ({current_page} * {page_size} - 1);
    """

    if filter_where_str:
        sql = sql.replace("@WHERE", filter_where_str)
    else:
        sql = sql.replace("@WHERE", "--")

    with open("socrbase.sql", mode="w", encoding="utf-8") as f:
        f.write(sql)

    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)


def get_socrbase_recordcount() -> int:
    eng = create_engine(CONNECTION_STR)
    sql = "SELECT COUNT(*) FROM [dbo].[SocrBase];"
    with eng.connect() as conn:
        return conn.execute(text(sql)).fetchone()[0]


### 2nd level = 1st level to list comprehensions of dicts

def get_socrbase_data() -> list[dict]:
    return [r for r in iter_socrbase_data()]


def get_socrbase_data_paged(
    page_size: int, current_page: int, level: int | None = None
) -> list[dict]:
    return [
        r for r in iter_socrbase_data_paged(
            page_size=page_size, current_page=current_page, level=level
        )
    ]


### 3d level = 2nd level to list comprehensions of pydantic objects

def get_pyd_socrbase_data() -> list[SocrBase]:
    return [SocrBase.parse_obj(obj) for obj in get_socrbase_data()]

def get_pyd_socrbase_data_paged(
    page_size: int, current_page: int, level: int | None = None
) -> list[SocrBase]:
    return [
        SocrBase.parse_obj(obj) for obj in get_socrbase_data_paged(
            page_size=page_size, current_page=current_page, level=level
        )
    ]

def get_socrbase_fieldnames() -> list[str]:
    l = ['[IID]', '[Level]', '[ScName]', '[SocrName]', '[KodTST]']
    return l

# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    #print(get_socrbase_recordcount())
    #for r in iter_socrbase_data_paged(page_size=20, current_page=1, level=2):
    #    print(r)
    #print('\n'.join([str(r) for r in get_socrbase_data()]))
    print('\n'.join([str(r) for r in get_pyd_socrbase_data()]))
    
