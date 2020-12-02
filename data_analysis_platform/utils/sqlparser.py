import os


def sqlparse(DB_TABLE, period, unit, filter_sql=None):
    sql = "Select * from %s Where PERIOD = '%s' And UNIT = '%s'" % (DB_TABLE, period, unit)  # 必选的两个筛选字段
    if filter_sql is not None:
        sql = "%s And %s" % (sql, filter_sql)  # 其他可选的筛选字段，如有则以And连接自定义字符串
    return sql
