# alitraffic





## slq 语句

SELECT Deal_time,Line_name,count(*) FROM tianchi.gd_train group by Deal_time, Line_name having Line_name = "线路10" order by Deal_time ;
根据成交时间,线路分组, 选择线路10, 使用时间排序

SELECT FROM_UNIXTIME( UNIX_TIMESTAMP( Deal_time ) , '%Y-%m-%d' ) AS ctime, Line_name,count(*) FROM tianchi.gd_train group by ctime having Line_name = "线路15";
根据天进行分组

20141128提交数据说明
何永兴
数据分成两个部分正常时间部分,和放假部分
何永兴result_GradientBoosting2
正常部分也就是0104至0107, 使用1125至1231和所有特征作为训练数据, 利用gradientboostingregression 进行回归
放假部分也就是0101至0103, 使用0901至1231和[1, 2, 3, 4, 5, 7, 9]作为训练数据, 利用gradientboostingregression 进行回归

尚result_GradientBoosting
正常部分也就是0104至0107, 使用1125至1231和所有特征作为训练数据, 利用gradientboostingregression 进行回归
放假部分也就是0101至0103, 使用1125至1231和[1, 2, 3, 4, 5, 7, 9]作为训练数据, 利用gradientboostingregression 进行回归
