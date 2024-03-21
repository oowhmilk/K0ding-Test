SELECT  USER_ID, PRODUCT_ID
FROM  ONLINE_SALE
GROUP BY  USER_ID, PRODUCT_ID
HAVING  COUNT(*) > 1
ORDER BY  USER_ID ASC, PRODUCT_ID DESC

-- 같은 talbe 내에서 2개 이상인 값 찾기 위해서 
-- group by 로 묶고
-- having count(*) > 1 로 2개 이상인 값 찾기