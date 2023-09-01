
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
    --
	)
	SELECT [IID] AS [IID],
	       [Code],
           [Name],
           [Socr],
           [Index],
           [Gninmb],
           [Uno],
           [Ocatd],
           [Status]
	FROM [Kladr]
	WHERE [IID] BETWEEN ((1 - 1) * 20) AND (1 * 20 - 1);
    