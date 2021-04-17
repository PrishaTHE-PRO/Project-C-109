import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import csv
import pandas as pd

df=pd.read_csv('SP.csv')
reading_score_list=df['reading score'].to_list()

reading_score_mean=statistics.mean(reading_score_list)
reading_score_std_deviation=statistics.stdev(reading_score_list)
reading_score_median=statistics.median(reading_score_list)
reading_score_mode=statistics.mode(reading_score_list)

reading_score_first_sd_start,reading_score_first_sd_end=reading_score_mean-reading_score_std_deviation,reading_score_mean+reading_score_std_deviation
reading_score_second_sd_start,reading_score_second_sd_end=reading_score_mean-(2*reading_score_std_deviation),reading_score_mean+(2*reading_score_std_deviation)
reading_score_third_sd_start,reading_score_third_sd_end=reading_score_mean-(3*reading_score_std_deviation),reading_score_mean+(3*reading_score_std_deviation)

# fig=ff.create_distplot([dice_result],['Result'],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
# fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1'))
# fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1'))
# fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2'))
# fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2'))
# fig.show()

reading_score_list_of_data_within_1_sd=[result for result in reading_score_list if result > reading_score_first_sd_start and result < reading_score_first_sd_end]
reading_score_list_of_data_within_2_sd=[result for result in reading_score_list if result > reading_score_second_sd_start and result < reading_score_second_sd_end]
reading_score_list_of_data_within_3_sd=[result for result in reading_score_list if result > reading_score_third_sd_start and result < reading_score_third_sd_end]

print('mean,median,and mode of reading score is{},{},and{}respectivly'.format(reading_score_mean,reading_score_median,reading_score_mode))

print('{}% of data lies with in 1 standard deviation'.format(len(reading_score_list_of_data_within_1_sd)*100.0/len(reading_score_list)))
print('{}% of data lies with in 2 standard deviation'.format(len(reading_score_list_of_data_within_2_sd)*100.0/len(reading_score_list)))
print('{}% of data lies with in 3 standard deviation'.format(len(reading_score_list_of_data_within_3_sd)*100.0/len(reading_score_list)))
 