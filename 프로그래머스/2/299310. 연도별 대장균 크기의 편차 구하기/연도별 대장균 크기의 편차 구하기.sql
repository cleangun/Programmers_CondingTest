-- 코드를 작성해주세요

# select DIFFERENTIATION_DATE from ecoli_data;

select e1.year,
       (e1.max_colony - e1.size_of_colony) as year_dev,
       e1.id
  from (select extract(year from DIFFERENTIATION_DATE) as year,
               id,
               size_of_colony,
               max(size_of_colony) over(partition by extract(year from DIFFERENTIATION_DATE)) as "max_colony"
          from ecoli_data) as e1
 order by year, year_dev;