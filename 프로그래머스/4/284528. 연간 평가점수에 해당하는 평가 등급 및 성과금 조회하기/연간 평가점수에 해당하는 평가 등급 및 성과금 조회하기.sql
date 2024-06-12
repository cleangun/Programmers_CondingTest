-- 코드를 작성해주세요
-- HR_DEPARTMENT , HR_EMPLOYEES , HR_GRADE

SELECT HE.EMP_NO
     , HE.EMP_NAME
     , CASE WHEN HG.SCORE >= 96 THEN 'S'
            WHEN HG.SCORE >= 90 THEN 'A'
            WHEN HG.SCORE >= 80 THEN 'B'
                                ELSE 'C'
        END AS 'GRADE'
     , CASE WHEN HG.SCORE >= 96 THEN HE.SAL * 0.2
            WHEN HG.SCORE >= 90 THEN HE.SAL * 0.15
            WHEN HG.SCORE >= 80 THEN HE.SAL * 0.1
                                ELSE 0
        END AS 'BONUS'
  FROM HR_EMPLOYEES HE JOIN (SELECT EMP_NO, AVG(SCORE) AS SCORE
                               FROM HR_GRADE
                              GROUP BY EMP_NO) HG
    ON HE.EMP_NO = HG.EMP_NO
  JOIN HR_DEPARTMENT HD
    ON HE.DEPT_ID = HD.DEPT_ID
 ORDER BY HE.EMP_NO;