from data_calculate import DataCalculator
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


class DataVisualization:
    def data_vis(self, dataCal, jsFile, tFile):
        result = DataCalculator.data_calculate(dataCal, jsFile, tFile)

        bar = Bar(init_opts= opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(list(result.keys()))
        bar.add_yaxis('Sales Revenue', list(result.values()),
                      label_opts= opts.LabelOpts(is_show= False))

        bar.set_global_opts(
            title_opts= opts.TitleOpts(title='Sales Revenue Each Day')
        )

        bar.render('Revenue_Visualization.html')



