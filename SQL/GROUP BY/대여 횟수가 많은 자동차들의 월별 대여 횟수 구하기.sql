SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(HISTORY_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE START_DATE BETWEEN '2022-08-01' AND '2022-11-01'
AND
  CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-11-01'
    GROUP BY CAR_ID
    HAVING COUNT(HISTORY_ID) >= 5
  )
GROUP BY MONTH, CAR_ID
HAVING RECORDS > 0
ORDER BY MONTH ASC, CAR_ID DESC;

-- MONTH 함수로 DATE 값 넣어주면 월 값만 구할수 있음
-- BETWEEN '2022-08-01' AND '2022-11-01' 
-- BETWEEN 의 경우 마지막 값이 포함되지 않기 때문에 하나 큰 값 넣어줘야함
-- GROUP BY 그룹 묶을 때 동시에 2개 묶을 수 있음
-- 월 별, ID 별 일 경우 => 월, ID 순으로 GROUP BY 