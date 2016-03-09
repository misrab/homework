import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from nl_utils import tscvsplit
import csv
import pdb

#load data
data_folder = "c:\\Users\\Nelson\\SG-DAT-NL\\Project\\data\\"
pickle_file = data_folder + 'nifty_one_minute_checkpoint.pkl'
print "loading %s" % pickle_file
one_minute_dataframe = pd.read_pickle(pickle_file)

#print "'" + "','".join(one_minute_dataframe.columns) + "'"

feature_columns = ['DayOfWeek','Hour',
'1_min_prior','5_min_prior','10_min_prior','20_min_prior','40_min_prior','80_min_prior',
'1_last_vs_ma','5_last_vs_ma','10_last_vs_ma','20_last_vs_ma','40_last_vs_ma','80_last_vs_ma',
'1_min_log_volume_vs_hx','5_min_log_volume_vs_hx','10_min_log_volume_vs_hx','20_min_log_volume_vs_hx','40_min_log_volume_vs_hx','80_min_log_volume_vs_hx',
'1_min_busd_log','5_min_busd_log','10_min_busd_log','20_min_busd_log','40_min_busd_log','80_min_busd_log',
'1_min_busd_time','5_min_busd_time','10_min_busd_time','20_min_busd_time','40_min_busd_time','80_min_busd_time',
'1_min_hilo','5_min_hilo','10_min_hilo','20_min_hilo','40_min_hilo','80_min_hilo',
'1_min_price_vs_range','5_min_price_vs_range','10_min_price_vs_range','20_min_price_vs_range','40_min_price_vs_range','80_min_price_vs_range']

print "We start with %s features" % len(feature_columns)

X = one_minute_dataframe[feature_columns].dropna()
X_std = StandardScaler().fit_transform(X)

FOLDS = 3
X_len = len(X_std)
datasets = [X_std[:X_len/3], X_std[X_len/3:X_len*2/3], X_std[X_len*2/3:]]
components_list = []
cum_var_exp_list = []

for dataset in datasets:
    pca = PCA()
    pca.fit(dataset)
    #print(pca.components_)
    components_list.append(pca.components_)
    #print "Here is PCA explained_variance_ratio_ of len %s" % len(pca.explained_variance_ratio_)
    #print(pca.explained_variance_ratio_) 

    var_exp = [(i / sum(pca.explained_variance_ratio_))*100 for i in sorted(pca.explained_variance_ratio_, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)
    #print cum_var_exp
    cum_var_exp_list.append(cum_var_exp)

    # with plt.style.context('seaborn-whitegrid'):
    #     plt.figure(figsize=(6, 4))

    #     plt.bar(range(len(var_exp)), var_exp, alpha=0.5, align='center',
    #             label='individual explained variance')
    #     plt.step(range(len(cum_var_exp)), cum_var_exp, where='mid',
    #              label='cumulative explained variance')
    #     plt.ylabel('Explained variance ratio')
    #     plt.xlabel('Principal components')
    #     plt.legend(loc='best')
    #     plt.tight_layout()
    # plt.show()
f = open('pca_output.csv','wb')
writer = csv.writer(f)
writer.writerow(['COMPONENTS'])
for i in range(len(components_list)):
    writer.writerow(['fold %s' % i])
    for j in range(len(components_list[i])):
        writer.writerow(components_list[i][j])
writer.writerow(['CUMULATIVE EXPLAINED VARIANCE'])
for i in range(len(cum_var_exp_list)):
    writer.writerow(['fold %s' % i])
    writer.writerow(list(cum_var_exp_list[i]))
f.close()

# np.savetxt('components_list.txt',components_list)
# np.savetxt('cum_var_exp_list.txt',cum_var_exp_list)