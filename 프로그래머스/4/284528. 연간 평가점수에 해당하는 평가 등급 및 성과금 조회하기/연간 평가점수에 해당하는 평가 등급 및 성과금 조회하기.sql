WITH C AS (
    SELECT EMP_NO, AVG(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT A.EMP_NO, A.EMP_NAME, A.GRADE, 
                                CASE 
                                    WHEN A.GRADE LIKE "S" THEN A.SAL * 0.2
                                    WHEN A.GRADE LIKE "A" THEN A.SAL * 0.15
                                    WHEN A.GRADE LIKE "B" THEN A.SAL * 0.1
                                    WHEN A.GRADE LIKE "C" THEN A.SAL * 0
                                END AS BONUS
FROM (
SELECT B.EMP_NO, B.EMP_NAME, B.SAL, 
    CASE 
        WHEN C.SCORE >= 96 THEN "S"
        WHEN C.SCORE >= 90 THEN "A"
        WHEN C.SCORE >= 80 THEN "B"
    ELSE "C"
    END AS GRADE
FROM HR_EMPLOYEES B 
JOIN C ON B.EMP_NO = C.EMP_NO
    ) A

