-- String 형식 맞추기 위한 
-- column 명 LIKE '% string %'
DATE_OF_BIRTH LIKE '%-03-%'

-- DATE_FORMAT 형식 맞춰기 위한
-- DATE_FORMAT(column 명, "%Y-%m-%d")
DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH

-- null 이 아닌 경우만 출력하기 위한 방법
TLNO IS NOT NULL

-- null 인 경우 형식에 맞게 출력 하는 방법 
SELECT IFNULL(TLNO, "NONE") AS TLNO

-- 가장 크거나 작은 값 찾을때 ORDER BY 로 정렬 후에 
-- LIMIT 1 : 정렬된 가장 위에 있는 값 가져오기 

-- DATE_FORMAT(column 명, "%Y-%m-%d") as column 명 : 년, 월, 일 로 date 형식 만들기 
-- like "% %" : 문자열 형식 비교 방법
-- NULL AS USER_ID : null 값으로 출력 만들기 

-- 같은 talbe 내에서 2개 이상인 값 찾기 위해서 
-- group by 로 묶고
-- having count(*) > 1 로 2개 이상인 값 찾기
SELECT  USER_ID, PRODUCT_ID
FROM  ONLINE_SALE
GROUP BY  USER_ID, PRODUCT_ID
HAVING  COUNT(*) > 1
ORDER BY  USER_ID ASC, PRODUCT_ID DESC
