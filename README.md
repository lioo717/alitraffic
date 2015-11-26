# alitraffic





## slq 语句

SELECT Deal_time,Line_name,count(*) FROM tianchi.gd_train group by Deal_time, Line_name having Line_name = "线路10" order by Deal_time ;
根据成交时间,线路分组, 选择线路10, 使用时间排序

SELECT FROM_UNIXTIME( UNIX_TIMESTAMP( Deal_time ) , '%Y-%m-%d' ) AS ctime, Line_name,count(*) FROM tianchi.gd_train group by ctime having Line_name = "线路15";
根据天进行分组