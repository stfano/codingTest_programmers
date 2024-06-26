SELECT 
    A.ID,
    CASE 
        WHEN N_GROUP = 1 THEN 'CRITICAL'
        WHEN N_GROUP = 2 THEN 'HIGH'
        WHEN N_GROUP = 3 THEN 'MEDIUM'
        WHEN N_GROUP = 4 THEN 'LOW'
    END AS COLONY_NAME
FROM (
    SELECT 
        ID,
        NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS N_GROUP
    FROM ECOLI_DATA
) AS A
ORDER BY A.ID ASC

