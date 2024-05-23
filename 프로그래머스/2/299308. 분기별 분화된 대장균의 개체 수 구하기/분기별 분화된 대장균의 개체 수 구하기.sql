-- 코드를 작성해주세요

select case when extract(month from DIFFERENTIATION_DATE) between 1 and 3 then '1Q'
            when extract(month from DIFFERENTIATION_DATE) between 4 and 6 then '2Q'
            when extract(month from DIFFERENTIATION_DATE) between 7 and 9 then '3Q'
            when extract(month from DIFFERENTIATION_DATE) between 10 and 12 then '4Q'
        end as QUARTER,
        count(*) as ECOLI_COUNT
  from ecoli_data
 group by 1
 order by QUARTER;