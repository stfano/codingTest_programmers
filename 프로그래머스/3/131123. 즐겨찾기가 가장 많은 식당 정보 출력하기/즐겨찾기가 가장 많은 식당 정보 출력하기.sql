SELECT 
    R.FOOD_TYPE,
    R.REST_ID,
    R.REST_NAME,
    R.FAVORITES
FROM 
    REST_INFO AS R
JOIN (
    SELECT 
        FOOD_TYPE,
        MAX(FAVORITES) AS MAX_FAVORITES
    FROM 
        REST_INFO
    GROUP BY 
        FOOD_TYPE
) AS bb ON R.FOOD_TYPE = bb.FOOD_TYPE 
AND R.FAVORITES = bb.MAX_FAVORITES
ORDER BY
    R.FOOD_TYPE DESC;