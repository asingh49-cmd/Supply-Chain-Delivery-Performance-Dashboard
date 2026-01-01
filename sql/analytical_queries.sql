#1. Market and Type of payment used for orders analysis 
select 
	market,
    count(order_id) as no_of_transactions, 
    SUM(case when type = 'DEBIT' then 1 else 0 end) as 'debit',
    SUM(case when type = 'TRANSFER' then 1 else 0 end) as 'transfer',
    SUM(case when type = 'payment' then 1 else 0 end) as 'payment',
    SUM(case when type = 'cash' then 1 else 0 end) as 'cash',
    round(avg(on_time_delivery),2) as otd_rate
from 
	orders 
group by 
	market 
order by 
	no_of_transactions desc;
#2. Performance Benchmarking of Shipping Modes
select 
	shipping_mode,
    count(order_id) as order_volume,
    (round(avg(on_time_delivery)*100,2)) as otd_rate,
    round(avg(days_for_shipping_real),2) as avg_days_ship,
    round(sum(sales),2) as total_rev,
    round(avg(sales),2) as avg_rev,
    round(avg(order_profit_per_order),2) as avg_profit_per_order
from
	orders
group by
	shipping_mode
order by 
	otd_rate desc;
#3. Weekend vs Weekday Orders
select
	case when is_weekend = 1 then "Weekend" else "Weekday" end as "weekend?",
    count(order_id) as order_volume,
    round(sum(on_time_delivery),2) as on_time_orders,
    count(*) - round(sum(on_time_delivery),2) as late_orders,
    round(avg(on_time_delivery),2) as on_time_orders
from
	orders
group by
	is_weekend
order by
	order_volume desc;
#4 Peak Period Performance - Monthly Basis
select
	order_month as month,
    count(order_id) as order_volume,
    round(avg(on_time_delivery),2) as otd_rate,
    round(avg(days_for_shipping_real),2) as avg_days_shipping,
    round(sum(sales),2) as total_revenue
from 
	orders
group by
	order_month
order by
	order_month asc;
#5 Product Category Reliability and Comparison
select 
	product_category_id,
    product_name,
    round(avg(on_time_delivery),2) as otd_rate,
    count(order_id) as order_volume,
    sum(on_time_delivery) as on_time_orders,
    count(*) - sum(on_time_delivery) as late_orders,
    round(sum(order_profit_per_order),2) as total_profit
from
	orders
group by
	product_category_id,product_name
order by
	total_profit desc;
#6 Market Penetration vs Performance
select
	market,
    count(order_id) as order_volume,
    sum(on_time_delivery) as on_time_orders,
    count(*) - sum(on_time_delivery) as late_orders,
    round(avg(on_time_delivery),2) as otd_rate,
    round(avg(delay_days),2) as delay_avg
from
	orders
group by 
	market
order by 
	order_volume desc;
#7 Bulk-order analysis
select 
	case when is_bulk_order = 1 then "bulk_order" else "normal_order" end as "is_bulk_or_not",
    count(order_id) as order_volume,
    round(sum(on_time_delivery),2) as on_time_orders,
    count(*) - round(sum(on_time_delivery),2) as late_orders,
    round(avg(on_time_delivery),2) as otd_rate,
    round(avg(order_profit_per_order),2) as avg_profit_per_order
from 
	orders
group by
	is_bulk_order
order by
	order_volume desc;