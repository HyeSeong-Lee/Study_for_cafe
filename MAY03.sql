-- 코드를 입력하세요
SELECT C.CART_ID
from CART_PRODUCTS C, CART_PRODUCTS CC
where 
C.NAME='Milk'
and CC.NAME='Yogurt'
and C.CART_ID=CC.CART_ID
