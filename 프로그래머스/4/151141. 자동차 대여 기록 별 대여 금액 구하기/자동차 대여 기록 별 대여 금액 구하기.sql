with rental as (
select h.CAR_ID, c.CAR_TYPE, c.DAILY_FEE, h.HISTORY_ID,
        datediff(h.END_DATE, h.START_DATE)+1 as renday
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
left join CAR_RENTAL_COMPANY_CAR c
    on h.CAR_ID=c.CAR_ID
    where c.CAR_TYPE in ('트럭')
),
discount as (
select p.DURATION_TYPE, p.DISCOUNT_RATE, c.CAR_TYPE, c.CAR_ID
from CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
left join CAR_RENTAL_COMPANY_CAR c
    on p.CAR_TYPE=c.CAR_TYPE
    where c.CAR_TYPE in ('트럭')
)

select r.HISTORY_ID,
round(r.DAILY_FEE*r.renday*(100-ifnull(d.DISCOUNT_RATE, 0))/100) FEE
from rental r
left join discount d
on r.CAR_ID=d.CAR_ID
    and case when renday >= 90 then '90일 이상'
             when renday >= 30 then '30일 이상'
             when renday >= 7 then '7일 이상' end = d.DURATION_TYPE
order by 2 desc, 1 desc