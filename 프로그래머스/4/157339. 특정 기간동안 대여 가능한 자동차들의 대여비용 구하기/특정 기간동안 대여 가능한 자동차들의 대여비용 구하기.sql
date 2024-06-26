SELECT
    A.CAR_ID, A.CAR_TYPE, 
    TRUNCATE(DAILY_FEE * 30 * (1 - DISCOUNT_RATE/100), 0) AS FEE
FROM
    CAR_RENTAL_COMPANY_CAR A 
    LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C
    ON A.CAR_TYPE = C.CAR_TYPE AND DURATION_TYPE = '30일 이상'
WHERE
    A.CAR_TYPE IN ('세단', 'SUV') AND
    DAILY_FEE * 30 * (1 - DISCOUNT_RATE/100) >= 500000 AND
    DAILY_FEE * 30 * (1 - DISCOUNT_RATE/100) < 2000000 AND
    A.CAR_ID NOT IN
    (SELECT 
        CAR_ID 
    FROM
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE
        (START_DATE LIKE '2022-11-%' OR END_DATE LIKE '2022-11-%')
        OR
        (START_DATE <= '2022-11-01' AND END_DATE >= '2022-11-30'))
ORDER BY 
    FEE DESC, CAR_TYPE ASC, CAR_ID DESC