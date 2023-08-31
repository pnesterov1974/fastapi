from sqlalchemy import create_engine, text

from schema import Kladr

CONNECTION_STR = r"mssql+pymssql://sa:Exptsci123@192.168.1.80/kladr"

####### 1-st LEVEL defs  Iter & GetRecordCount


def iter_kladr_data():
    eng = create_engine(CONNECTION_STR)
    sql = """
    SELECT TOP(15)
           ROW_NUMBER() OVER(ORDER BY [Code]) AS [IID],
           [Code] AS [CODE],
           [Name] AS [NAME],
           [Socr] AS [SOCR],
           [Index] AS [INDEX],
           [Gninmb] AS [GNINMB],
           [Uno] AS [UNO],
           [Ocatd] AS [OCATD],
           [Status] AS [STATUS]
    FROM [dbo].[Kladr]
    """
    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)


def iter_kladr_data_paged(page_size: int, current_page: int, status: int | None = None):
    eng = create_engine(CONNECTION_STR)

    filter_where_str = None
    if status:
        filter_where_str = f"WHERE [Status] = {status}"

    sql = f"""
    WITH [Kladr] AS
	(
	SELECT ROW_NUMBER() OVER(ORDER BY [Code]) AS [IID],
           [Code],
           [Name],
           [Socr],
           [Index],
           [Gninmb],
           [Uno],
           [Ocatd],
           [Status]
	FROM [dbo].[Kladr]
    @WHERE
	)
	SELECT [IID] AS [IID],
	       [Code] AS [CODE],
           [Name] AS [NAME],
           [Socr] AS [SOCR],
           [Index] AS [INDEX],
           [Gninmb] AS [GNINMB],
           [Uno] AS [UNO],
           [Ocatd] AS [OCATD],
           [Status] AS [Status]
	FROM [Kladr]
	WHERE [IID] BETWEEN (({current_page} - 1) * {page_size}) AND ({current_page} * {page_size} - 1);
    """

    if filter_where_str:
        sql = sql.replace("@WHERE", filter_where_str)
    else:
        sql = sql.replace("@WHERE", "--")

    with open("kladr.sql", mode="w", encoding="utf-8") as f:
        f.write(sql)

    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)


def get_kladr_recordcount() -> int:
    eng = create_engine(CONNECTION_STR)
    sql = "SELECT COUNT(*) FROM [dbo].[Kladr];"
    with eng.connect() as conn:
        return conn.execute(text(sql)).fetchone()[0]


### 2nd level = 1st level to list comprehensions of dicts


def get_kladr_data() -> list[dict]:
    return [r for r in iter_kladr_data()]


def get_kladr_data_paged(
    page_size: int, current_page: int, status: int | None = None
) -> list[dict]:
    return [
        r
        for r in iter_kladr_data_paged(
            page_size=page_size, current_page=current_page, status=status
        )
    ]


### 3d level = 2nd level to list comprehensions of pydantic objects


def get_pyd_kladr_data() -> list[Kladr]:
    return [Kladr.parse_obj(obj) for obj in get_kladr_data()]


def get_pyd_kladr_data_paged(
    page_size: int, current_page: int, status: int | None = None
) -> list[Kladr]:
    return [
        Kladr.parse_obj(obj)
        for obj in get_kladr_data_paged(
            page_size=page_size, current_page=current_page, status=status
        )
    ]


# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # print(get_kladr_data())
    print("\n".join([str(r) for r in get_pyd_kladr_data()]))
    print(get_kladr_recordcount())
