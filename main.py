'''
    39956a10efc09429356600eae9bf58a7519347b12364afe2b74a1873
    #print(tushare.__version__)
'''
import pandas as pd
# df = DailyDataOne('300059.sz','20220520')
# df = _dbDrive.DailyDataOneBak('300059.sz','20220520')
# df = DailyDataOneBak('300059.sz','20220520')
# print(df[ (df['market']=='中小板') & (df['list_status']=='L')])
import rmtDataDrive.StockBase as stb
import AnalyData.AnalyStockBase as anl
code = '601398.sh'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth',10000)
pd.set_option('display.width',10000)
# pd.set_option('display.unicode.ambiguous_as_wide',True)
# pd.set_option('display.unicode.east_asian_width',True)

########################################################################################################################

# df = stb.GetAllStockBase()
# df = stb.StockCompany()
# df = stb.BakBasic('','601398.sh',0)
# df = stb.GetTradeCal('SSE','','','1')
# df = stb.NewShare(20220628,20220630)
# df = stb.DailyMd('601398.sh',20220628,20220630)

# stb.UpdateDaily(code)
# df = stb.Daily(code,20220630)
# stb.UpdateWeekly(code)
# df = stb.Weekly(code,20220701)
# stb.UpdateMonthly(code)
# df = stb.Monthly(code,20220630)

##############################################
#这两个是直接获取，所以日期入参是字符串
# df = stb.MoneyFlow(code,'20220630')
# df = stb.MoneyFlowMd(code,'20220624','20220630')
##############################################

# 日行情，备用
# stb.BakDaily(20220101,20220912,False)


##############################################

# df = anl.GetStockBase()
# print(df.shape[0])
# start = 20190101
# end = 20220701
# for i,row in df.iterrows():
#     df = stb.DailyMd(row.ts_code, start, end)

##############################################
# 主板 和深圳中小板
'''
1、主板 和深圳中小板
'''
df = stb.GetStockbaseBoardCust("market == '主板' | market == '中小板'")
# print(df)


'''
2、市值过滤
'''
# da = stb.BakBasicEx("float_share > 50 & float_share < 100") # 流通股条件
da = stb.BakBasicEx("total_share > 10") # 流通股条件
dk = pd.merge(df,da,left_on='ts_code',right_on='ts_code',how='inner')
# dk["rate"] = dk["float_share"] / dk["total_share"] * 100    # 流通股 / 总股本
columns = ['ts_code','float_share', 'total_share', 'total_assets','liquid_assets','fixed_assets','name_x']
# print(dk[columns].rename(columns={'ts_code':'股票代码','name_x':'股票名称','float_share':'流通股本(亿)','total_share':'总股本','total_share':'总资产','liquid_assets':'流动资产','fixed_assets':'固定资产'}))
# print(dk[columns].sort_values(by='float_share'))
# print(dk.shape[0])

'''
3、股价分析 总市值波动大于0.5
'''

dtmp = dk[columns].sort_values(by='float_share')
Bool = dtmp.name_x.str.contains("ST")
dtmp = dtmp[~Bool]
ret = anl.AnStocksWave(20220101,20220606,dtmp)
ret_qry = ret.query('total_mv_rate > 0.5')
print(ret_qry.sort_values(by=['total_mv_rate','waverate']))
# print(ret.sort_values(by='waverate'))
print(ret_qry.shape[0])

##############################################


 
