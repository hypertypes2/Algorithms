SELECT A.FLAVOR
FROM FIRST_HALF A
    JOIN (SELECT SHIPMENT_ID, FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
          FROM JULY
          GROUP BY FLAVOR) B
    ON A.SHIPMENT_ID=B.SHIPMENT_ID
GROUP BY A.FLAVOR
ORDER BY (A.TOTAL_ORDER+B.TOTAL_ORDER) DESC
LIMIT 3