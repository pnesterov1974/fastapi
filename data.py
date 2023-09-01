from sqlalchemy import create_engine, text

CONNECTION_STR = r'mssql+pymssql://sa:Exptsci123@192.168.1.78/kladr2'

# def iter_socrbase_data():
#     eng = create_engine(CONNECTION_STR);
#     sql = '''
#     SELECT TOP(15)
#        ROW_NUMBER() OVER(ORDER BY [Pid]) AS [NN],
#        [Level] AS [LEVEL],
#        [ScName] AS [SCNAME],
#        [SocrName] AS [SOCRNAME],
#        [KodTST] AS [KOD_T_ST]
#     FROM [dbo].[SocrBase];
#     '''
#     with eng.connect() as conn:
#         for r in conn.execute(text(sql)).fetchall():
#             yield dict(r._mapping)

def iter_socrbase_data_paged(page_size=20, current_page=1):
    eng = create_engine(CONNECTION_STR);
    sql = f'''
    WITH [SocrBase] AS
	(
	SELECT ROW_NUMBER() OVER (ORDER BY Pid) AS [iid],
		   [Level],
		   [ScName],
		   [SocrName],
		   [KodTST]
	FROM [dbo].[SocrBase]
	)
	SELECT [iid] AS [IID],
	       [Level] AS [LEVEL],
		   [ScName] AS [SCNAME],
		   [SocrName] AS [SOCRNAME],
		   [KodTST] AS [KOD_T_ST]
	FROM [SocrBase]
	WHERE [iid] BETWEEN (({current_page} - 1) * {page_size}) AND ({current_page} * {page_size} - 1);
    '''
    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)

def iter_kladr_data_paged(page_size=20, current_page=1):
    eng = create_engine(CONNECTION_STR);
    sql = f'''
    WITH [Kladr] AS
	(
	SELECT ROW_NUMBER() OVER (ORDER BY [Code]) AS [iid],
		   [Code],
           [Name],
           [Socr],
           [Index],
           [Gninmb],
           [Uno],
           [Ocatd],
           [Status]
	FROM [dbo].[Kladr]
	)
	SELECT [iid] AS [IID],
	       [Code] AS [CODE],
           [Name] AS [NAME],
           [Socr] AS [SOCR],
           [Index] AS [INDEX],
           [Gninmb] AS [GNINMB],
           [Uno] AS [UNO],
           [Ocatd] AS [OCATD],
           [Status] AS [STATUS]
	FROM [Kladr]
	WHERE [iid] BETWEEN (({current_page} - 1) * {page_size}) AND ({current_page} * {page_size} - 1);
    '''
    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)

def get_socrbase_recordcount():
    eng = create_engine(CONNECTION_STR);
    sql = 'SELECT COUNT(*) FROM [dbo].[SocrBase];'
    with eng.connect() as conn:
        return conn.execute(text(sql)).fetchone()[0]

# def iter_kladr_data():
#     eng = create_engine(CONNECTION_STR);
#     sql = '''
#     SELECT TOP(15)
#            [Code] AS [CODE],
#            [Name] AS [NAME],
#            [Socr] AS [SOCR],
#            [Index] AS [INDEX],
#            [Gninmb] AS [GNINMB],
#            [Uno] AS [UNO],
#            [Ocatd] AS [OCATD],
#            [Status] AS [STATUS]
#     FROM [dbo].[Kladr]
#     '''
#     with eng.connect() as conn:
#         for r in conn.execute(text(sql)).fetchall():
#             yield dict(r._mapping)

def get_kladr_recordcount():
    eng = create_engine(CONNECTION_STR);
    sql = 'SELECT COUNT(*) FROM [dbo].[Kladr];'
    with eng.connect() as conn:
        return conn.execute(text(sql)).fetchone()[0]

def iter_street_data():
    eng = create_engine(CONNECTION_STR);
    sql = '''
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
    '''
    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)

def get_street_recordcount():
    eng = create_engine(CONNECTION_STR);
    sql = 'SELECT COUNT(*) FROM [dbo].[Street];'
    with eng.connect() as conn:
        return conn.execute(text(sql)).fetchone()[0]

def iter_doma_data():
    eng = create_engine(CONNECTION_STR);
    sql = '''
    SELECT TOP (15) 
       [Code] AS [CODE],
       [Name] AS [NAME],
       [Korp] AS [KORP],
       [Socr] AS [SOCR],
       [Index] AS [INDEX],
       [Gninmb] AS [GNINMB],
       [Uno] AS [UNO],
       [Ocatd] AS [OCATD]
  FROM [dbo].[Doma]
    '''
    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)

def get_doma_recordcount():
    eng = create_engine(CONNECTION_STR);
    sql = 'SELECT COUNT(*) FROM [dbo].[Doma];'
    with eng.connect() as conn:
        return conn.execute(text(sql)).fetchone()[0]

def iter_altnames_data():
    eng = create_engine(CONNECTION_STR);
    sql = '''
    SELECT TOP (15)
       [OldCode] AS [OLDCODE],
       [NewCode] AS [NEWCODE],
       [Level] AS [LEVEL]
    FROM [dbo].[AltNames]
    '''
    with eng.connect() as conn:
        for r in conn.execute(text(sql)).fetchall():
            yield dict(r._mapping)

def get_altnames_recordcount():
    eng = create_engine(CONNECTION_STR);
    sql = 'SELECT COUNT(*) FROM [dbo].[AltNames];'
    with eng.connect() as conn:
        return conn.execute(text(sql)).fetchone()[0]

# def get_socrbase_data():
#     return [r for r in iter_socrbase_data()]

def get_socrbase_data_paged(page_size=20, current_page=1):
    return [r for r in iter_socrbase_data_paged(page_size=page_size, current_page=current_page)]

# def get_kladr_data():
#     return [r for r in iter_kladr_data()]

def get_kladr_data_paged(page_size=20, current_page=1):
    return [r for r in iter_kladr_data_paged(page_size=page_size, current_page=current_page)]
            
def get_street_data():
    return [r for r in iter_street_data()]
            
def get_doma_data():
    return [r for r in iter_doma_data()]

def get_altnames_data():
    return [r for r in iter_altnames_data()]

# -------------------------------------------------------------------------------------------------
if __name__== "__main__":
    print(get_socrbase_data_paged())