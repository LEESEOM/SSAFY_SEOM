### SQL 연습 문제

- 조건 : user 테이블을 기준으로 조회합니다.
-- SELECT
1. 전체 데이터 조회하기
SELECT
  *
FROM
  user;
2. 이름과 나이 조회하기
SELECT
  이름, 나이
FROM
  user;
3. rowid와 이름 조회하기
SELECT
  rowid, 이름
FROM
  user;
4. 이름과 나이를 나이가 어린 순서대로 조회하기
SELECT
  이름, 나이
FROM
  user
ORDER BY
  나이;
5. 이름과 나이를 나이가 많은 순서대로 조회하기
SELECT
  이름, 나이
FROM
  user
ORDER BY
  나이 DESC;
6. 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기
SELECT
  이름, 나이, 계좌 잔고
FROM
  user
ORDER BY
  나이, 계좌 잔고 DESC;
7. 중복없이 모든 지역 조회하기 (=중복되는 레코드(행)은 제거)
SELECT DISTINCT
  지역
FROM
  user;
8. 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT
  지역
FROM
  user
ORDER BY
  지역;
9. 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
SELECT DISTINCT
  이름, 지역
FROM 
  user;
10. 이름과 지역 중복 없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회하기
SELECT DISTINCT
  이름, 지역
FROM
  user
ORDER BY
  지역;
11. 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT
  이름, 나이, 계좌 잔고
FROM
  user
WHERE
  나이 >= 30;
12. 나이가 30살 이상인 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT
  이름, 나이, 계좌 잔고
FROM
  user
WHERE
  나이 >= 30
  AND 계좌 잔고 > 50만원;
13. 이름에 ‘호’가 포함되는 사람들의 이름과 성 조회하기
SELECT
  이름, 성
FROM
  user
WHERE
  이름 LIKE '%호%';
14. 이름이 ‘준’으로 끝나는 사람들의 이름 조회하기
SELECT
  이름
FROM
  user
WHERE
  이름 LIKE '%준';
15. 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
SELECT
  이름, 전화번호
FROM
  user
WHERE
  전화번호 IS NOT NULL
  AND 지역 = '서울';
16. 나이가 20대인 사람들의 이름과 나이 조회하기
SELECT
  이름, 나이
FROM
 user
WHERE
  나이 BETWEEN 20 AND 29;
17. 전화번호 중간 4자리가 ’51’로 시작하는 사람들의 이름과 전화번호 조회하기
SELECT
  이름, 전화번호
FROM
  user
WHERE
  전화번호 LIKE '%-51__-%';
18. 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
SELECT
  이름, 지역
FROM
  user
WHERE
  지역 IN ('경기도', '강원도');
19. 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
SELECT
  이름, 지역
FROM
  user
WHERE
  지역 NOT IN ('경기도', '강원도');
20. 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
SELECT
  이름, 나이
FROM
  user
WHERE
  나이 BETWEEN 20 AND 30;
21. 첫 번째 부터 열 번째 데이터까지 rowid와 이름 조회하기
SELECT
  rowid, 이름
FROM
  user
LIMIT 10;
22. 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
SELECT
  이름, 계좌 잔고
FROM
  user
ORDER BY
  계좌 잔고 DESC
LIMIT 10;
23. 나이가 가장 어린 5명의 이름과 나이 조회하기
SELECT
  이름, 나이
FROM
  user
ORDER BY
  나이
LIMIT 5;
24. 11번째 부터 20번째 데이터의 rowid와 이름 조회하기
SELECT
  rowid, 이름
FROM
  user
LIMIT 10, 10;
25. user 테이블의 전체 행 수 조회하기
SELECT
  COUNT(*) AS 전체 행 수
FROM
  user;
26. 전체 유저의 평균 계좌 잔고 조회하기
SELECT
  AVG('계좌 잔고') AS 평균 계좌 잔고
FROM
  user;
27. 지역별 각각 계좌 잔고 평균 조회하기
SELECT
  지역, 
  AVG('계좌 잔고') AS 지역별 계좌 잔고
FROM
  user
GROUP BY
  지역;
28. 지역별 각각 계좌 잔고 평균을 잔고 평균 오름차순으로 조회하기
SELECT
  지역,
  AVG('계좌 잔고') AS 지역별 계좌 잔고
FROM
  user
GROUP BY
  지역
ORDER BY
  지역별 계좌 잔고;
29. 나이가 30살 이상인 사람들의 평균 나이를 조회하기
SELECT
  AVG(나이) AS 평균 나이
FROM
  user
WHERE
  나이 >= 30;
30. 각 지역별로 몇 명씩 살고 있는지 조회하기
SELECT
  지역,
  COUNT(*) AS 인구
FROM
  user
GROUP BY
  지역;
31. 각 성씨가 몇 명씩 살고 있는지 조회하기
SELECT
  성,
  COUNT(*) AS 인원 수
FROM
  user
GROUP BY
  성;
32. 인원이 가장 많은 성씨 순으로 조회하기
SELECT
  성,
  COUNT(*) AS 인원 수
FROM
  user
GROUP BY
  성
ORDER BY
  인원 수 DESC;
33. 각 지역별 평균 나이 조회하기
SELECT
  지역,
  AVG(나이) AS 평균 나이
FROM
  user
GROUP BY
  지역;

-- INSERT
1. 단일 행 삽입하기
2. 여러 행 삽입하기

-- UPDATE
1. 두번째 행의 이름을 ‘김철수한무두루미’로, 주소를 ‘제주도’로 수정하기

-- DELETE
1. 다섯번째 행의 데이터를 삭제하기
2. 이름에 ‘영’이 포함되는 데이터 삭제하기
3. 테이블의 모든 데이터 삭제하기

*따로 제공된 DB가 없습니다. SQL문을 어떻게 작성할지를 구상해보시면 됩니다.
-- JOIN
1. 게시글과 작성된 유저의 이름 정보를 같이 가져오기
2. 게시글과 작성된 유저가 일부 삭제된 테이블에서 이름 정보를 같이 가져오기 (이 때에 모든 게시글 레코드는 출력 결과에 포함되어 있어야함)