SELECT II.ITEM_ID, II.ITEM_NAME
FROM ITEM_INFO AS II, 
(SELECT ITEM_ID
FROM ITEM_TREE
WHERE PARENT_ITEM_ID IS NULL) AS IT
WHERE II.ITEM_ID = IT.ITEM_ID
ORDER BY II.ITEM_ID