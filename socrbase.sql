
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
	SELECT [IID],
	       [Level],
		   [ScName],
		   [SocrName],
		   [KodTST]
	FROM [SocrBase]
	WHERE [IID] BETWEEN ((1 - 1) * 20) AND (1 * 20 - 1);
    