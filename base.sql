-- String 형식 맞추기 위한 
-- column 명 LIKE '% string %'
DATE_OF_BIRTH LIKE '%-03-%'

-- DATE_FORMAT 형식 맞춰기 위한
-- DATE_FORMAT(column 명, "%Y-%m-%d")
DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH

-- null 이 아닌 경우만 출력하기 위한 방법
TLNO IS NOT NULL