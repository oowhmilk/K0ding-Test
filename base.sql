-- String 형식 맞추기 위한 
-- column 명 LIKE '% string %'
DATE_OF_BIRTH LIKE '%-03-%'

-- DATE_FORMAT 형식 맞춰기 위한
-- DATE_FORMAT(column 명, "%Y-%m-%d")
DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH

-- String 형식 맞추기 위한 
-- column 명 LIKE '%string%'
DATE_OF_BIRTH LIKE '%-03-%'

-- DATE_FORMAT 형식 맞춰기 위한
-- DATE_FORMAT(column 명, "%Y-%m-%d")
DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH

-- null 이 아닌 경우만 출력하기 위한 방법
-- where 안에 넣어서 사용
TLNO IS NOT null
TLNO IS null

-- & 연산 가능

-- LIMIT 1 순서대로 정렬 이후 가장 위에 있는거 하나 선택
-- ORDER BY 뒤에 작성해야함
ORDER BY DATETIME
LIMIT 1

-- null 값으로 출력 만들기 
SELECT NULL AS USER_ID

-- 출력 형식 맞추기 위한 문자열 합치기
CONCAT(MAX(LENGTH), 'cm')

-- MONTH 함수로 DATE 값 넣어주면 월 값만 구할수 있음
-- BETWEEN '2022-08-01' AND '2022-11-01' 
-- BETWEEN 의 경우 마지막 값이 포함되지 않기 때문에 하나 큰 값 넣어줘야함
-- GROUP BY 그룹 묶을 때 동시에 2개 묶을 수 있음
-- 월 별, ID 별 일 경우 => 월, ID 순으로 GROUP BY 

-- NULL 인 경우 출력 형식 맞추기
-- IFNULL(column 명, "값")
IFNULL(FREEZER_YN, "N") AS FREEZER_YN

-- 반올림
-- 3456
ROUND(3456.1234567)

-- RANK 
RANK() OVER(ORDER BY Population DESC) AS rnk


-- grouping 한 결과 한 줄로 출력하기
-- GROUP_CONCAT(column 명 SEPARATOR '구분자') 
SELECT member_id, GROUP_CONCAT(name SEPARATOR '|') FROM product GROUP BY member_id;

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