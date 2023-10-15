-- INSERT INTO article 
--     VALUES 



-- article, user 같이 조회
SELECT *
    FROM article, user
WHERE article.userid = user.id;

-- EMPLOYEE, DEPARTMENT
SELECT e.name, e.deptno, d.name
    FROM EMPLOYEE e, DEPARTMENT d -- alias(별명) 설정해서 보기 편하게
 WHERE e.deptno = d.deptno;

 -- 동등 JOIN == INNER JOIN
 SELECT e.name, e.deptno, d.name, d.location
    FROM EMPLOYEE e
 INNER JOIN DEPARTMENT d
    ON e.deptno = d.deptno;

-- 각 직원의 상사 이름을 조회
SELECT e1.name, e1.job, e1.deptno, e1.boss, e2.name
    FROM EMPLOYEE e1, EMPLOYEE e2
WHERE e1.boss = e2.empno;

SELECT * FROM EMPLOYEE;

-- LEFT (OUTER) JOIN
-- 한쪽이라도 값을 가지고 있으면 일단 조회, 없는 쪽은 NULL 표시
SELECT e1.name, e1.job, e1.deptno, e1.boss, e2.name
    FROM EMPLOYEE e1
 LEFT JOIN EMPLOYEE e2
    ON e1.boss = e2.empno;

-- 직원의 이름, 상사 이름, 부서 이름 조회
SELECT e1.name AS '직원명', e2.name AS '상사명', d.name AS '부서명'
    FROM EMPLOYEE e1
 LEFT JOIN EMPLOYEE e2
    ON e1.boss = e2.empno
 LEFT JOIN DEPARTMENT d
    ON e1.deptno = d.deptno;


