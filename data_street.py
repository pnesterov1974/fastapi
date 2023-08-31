from sqlalchemy import create_engine, text

from schema import Street

CONNECTION_STR = r"mssql+pymssql://sa:Exptsci123@192.168.1.80/kladr"


def iter_street_data():
    eng = create_engine(CONNECTION_STR)
    sql = """
    SELECT TOP (15)
      ROW_NUMBER() OVER(ORDER BY [Code]) AS [IID], 
      [Code] AS [CODE],
      [Name] AS [NAME],
      [Socr] AS [SOCR],
      [Index] AS [INDEX],
      [Gninmb] AS [GINMB],
      [Uno] AS [UNO],
      [Ocatd] AS [OCATD]
  FROM [dbo].[Street]
    """
    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)


def get_street_recordcount():
    eng = create_engine(CONNECTION_STR);
    sql = 'SELECT COUNT(*) FROM [dbo].[Street];'
    with eng.connect() as conn:
        return conn.execute(text(sql)).fetchone()[0]


def get_street_data():
    return [r for r in iter_street_data()]


def get_pyd_street_data() -> list[Street]:
    return [Street.parse_obj(obj) for obj in get_street_data()]


# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # print(get_kladr_data())
    print("\n".join([str(r) for r in get_pyd_street_data()]))
    print(get_street_recordcount())
