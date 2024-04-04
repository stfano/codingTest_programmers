SELECT CAR_ID,
    CASE WHEN CAR_ID in 
        (SELECT CAR_ID 
         FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
         WHERE "2022-10-16" Between START_DATE and END_DATE) THEN "대여중"
    else "대여 가능"
    end  AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    GROUP BY CAR_ID
    ORDER BY CAR_ID desc