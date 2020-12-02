import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine

from django.shortcuts import render
from django.conf import settings

from utils import sqlparser, statictical


def index(request):
    ENGINE = create_engine(os.path.join('sqlite:///', settings.BASE_DIR, 'db_sqlite3'))
    sql = sqlparser.sqlparse('test_data', 'MAT', 'Value', " [tc_3] = 'C09C ANGIOTENS-II ANTAG, PLAIN|血管紧张素II拮抗剂，单一用药'")
    df = pd.read_sql_query(sql, ENGINE)
    pivoted = pd.pivot_table(df,
                             values='amount',  # 数据透视汇总值为AMOUNT字段，一般保持不变
                             index='date_time',  # 数据透视行为DATE字段，一般保持不变
                             columns='molecule',  # 数据透视列为MOLECULE字段，该字段以后应跟随分析需要动态传参
                             aggfunc=np.sum)  # 数据透视汇总方式为求和，一般保持不变

    if pivoted.empty is False:
        pivoted.sort_values(by=pivoted.index[-1], axis=1, ascending=False, inplace=True)  # 结果按照最后一个DATE表现排序

    context = {
        'market_size': statictical.kpi(pivoted)[0],
        'market_gr': statictical.kpi(pivoted)[1],
        'market_cagr': statictical.kpi(pivoted)[2],
        'ptable': statictical.ptable(pivoted).to_html()
    }

    return render(request, 'chpa_data/display.html', context)
