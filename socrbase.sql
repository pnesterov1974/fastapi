
    WITH [SocrBase] AS
	(
	SELECT ROW_NUMBER() OVER (ORDER BY [Pid]) AS [IID],
		   [Level],
		   [ScName],
		   [SocrName],
		   [KodTST]
	FROM [dbo].[SocrBase]
    --
	)
	SELECT [IID] AS [IID],
	       [Level] AS [LEVEL],
		   [ScName] AS [SCNAME],
		   [SocrName] AS [SOCRNAME],
		   [KodTST] AS [KOD_T_ST]
	FROM [SocrBase]
	WHERE [IID] BETWEEN ((1 - 1) * 20) AND (1 * 20 - 1);
    