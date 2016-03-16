import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import cross_val_score
from nl_utils import tscvsplit, trade_z_score
import pdb

if __name__ == '__main__':
    data_folder = "c:\\Users\\Nelson\\SG-DAT-NL\\Project\\data\\"
    pickle_file = data_folder + 'nifty_pca_checkpoint.pkl'
    print "loading %s" % pickle_file
    one_minute_dataframe = pd.read_pickle(pickle_file)

    #print "'" + "','".join(one_minute_dataframe.columns) + "'"

    response_columns = ['1_min_return','5_min_return','10_min_return','20_min_return','40_min_return','80_min_return'] #cts response
    #[,'1_min_updown','5_min_updown','10_min_updown','20_min_updown','40_min_updown','80_min_updown'] #binary
    #['1_min_cat','5_min_cat','10_min_cat','20_min_cat','40_min_cat','80_min_cat'] #categorical

    all_feature_columns = ['pca_v0','pca_v1','pca_v2','pca_v3','pca_v4','pca_v5','pca_v6','pca_v7','pca_v8','pca_v9','pca_v10','pca_v11','pca_v12','pca_v13','pca_v14','pca_v15','pca_v16','pca_v17','pca_v18','pca_v19','pca_v20','pca_v21','pca_v22','pca_v23','pca_v24','pca_v25','pca_v26','pca_v27','pca_v28','pca_v29','pca_v30','pca_v31','pca_v32','pca_v33','pca_v34','pca_v35','pca_v36','pca_v37','pca_v38','pca_v39','pca_v40','pca_v41','pca_v42']

    CROSS_VALIDATION_FOLDS = 4

    num_feature_list = [2,3,4,5,8,15]
    depth_list = range(1,8)

    rmse_results = {}
    for response in response_columns:
        for num_features in num_feature_list:
            feature_columns = all_feature_columns[:num_features]

            for max_depth in depth_list:
                print "---working on response %s | num_features %s | max_depth %s" % (response, num_features, max_depth)
                regressor = DecisionTreeRegressor(max_depth = max_depth)
                X = one_minute_dataframe[feature_columns]
                y = one_minute_dataframe[response]
                cross_val_sse_list = cross_val_score(regressor, X, y, scoring=trade_z_score) #cv=tscvsplit(one_minute_dataframe,CROSS_VALIDATION_FOLDS), n_jobs = 1)
                pdb.set_trace()
                if response not in rmse_results:
                    rmse_results[response] = {num_features: {max_depth: np.mean([np.sqrt(x) for x in cross_val_sse_list])}}
                else:
                    if num_features not in rmse_results[response]:
                        rmse_results[response][num_features] = {max_depth: np.mean([np.sqrt(x) for x in cross_val_sse_list])}
                    else:
                        rmse_results[response][num_features][max_depth] = np.mean([np.sqrt(x) for x in cross_val_sse_list])
    
    print "response\tnum_features\tmax_depth\tRMSE"
    for response in response_columns:
        for num_features in num_feature_list:
            for max_depth in depth_list:
                print "%s\t%s\t\t%s\t\t%0.15f" % (response, num_features, max_depth, rmse_results[response][num_features][max_depth])
