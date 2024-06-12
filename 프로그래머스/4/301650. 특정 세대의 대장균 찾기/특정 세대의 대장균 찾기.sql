-- 코드를 작성해주세요
SELECT ID
  FROM ECOLI_DATA
 WHERE PARENT_ID IN (SELECT ED1.ID
                       FROM ECOLI_DATA ED1 JOIN (SELECT ID
                                                   FROM ECOLI_DATA
                                               WHERE PARENT_ID IS NULL) ED2
                         ON ED1.PARENT_ID = ED2.ID)
 ORDER BY ID;
                      
                      