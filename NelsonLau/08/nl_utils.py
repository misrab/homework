import numpy as np
import sys
from sklearn.metrics import make_scorer
import pdb

def tscvsplit(mydata, folds):
    idxs = np.arange(len(mydata))
    return [(idxs[:i], idxs[i:]) for i in range(len(mydata)/(folds+1), len(mydata) - len(mydata)%(folds+1), len(mydata)/(folds+1))] #the modulo in 2nd term is to prevent making a very small test set e.g., if len(mydata) == 103 and folds = 3

def print_and_write(mytext, filewriter):
    print mytext
    filewriter.write(str(mytext))
    filewriter.write('\n')

def print_time_remaining(seconds_to_go):
    days_to_go = int(seconds_to_go) / (24*60*60)
    hours_to_go = int(seconds_to_go - days_to_go * 24*60*60) /  (60*60)
    minutes_to_go = int(seconds_to_go - days_to_go*24*60*60 - hours_to_go*60*60) / 60
    seconds_to_go = seconds_to_go - days_to_go*24*60*60 - hours_to_go*60*60 - minutes_to_go*60
    print "We still need %s days, %s hours, %s minutes, %s seconds" % (days_to_go, hours_to_go, minutes_to_go, seconds_to_go)

def trade_z_score_func(ground_truth, predictions):
    #if a positive return is predicted, we'll buy; if negative, we sell, if 0, do nothing
    #so, return the mean / std of {sign of prediction * true return}
    sign_of_predictions = np.sign(predictions)

    current_try = 0
    MAX_TRIES = 5
    EPSILON = 1e-100
    trade_pnls_ok = False
    while not trade_pnls_ok:
        trade_pnls = sign_of_predictions * ground_truth
        if max(abs(trade_pnls)) > EPSILON:
            trade_pnls_ok = True
        else:
            current_try += 1
            if current_try > MAX_TRIES:
                print "problem in trade_z_score_func"
                sys.exit(1)
    trade_z_score = np.mean(trade_pnls) / np.std(trade_pnls)
    return trade_z_score

def trade_z_score(estimator, X, y):
    estimator.fit(X,y)
    predictions = estimator.predict(X)
    trade_z_scorer = make_scorer(score_func=trade_z_score_func(y,predictions), greater_is_better = True)
    return trade_z_scorer

def cross_val_custom_score(estimator, X, y, cv, score_func):
    scores = []
    for data_split in cv:
        X_train = X.iloc[data_split[0]]
        X_test = X.iloc[data_split[1]]
        y_train = y.iloc[data_split[0]]
        y_test = y.iloc[data_split[1]]
    
        estimator.fit(X_train,y_train)
        result = score_func(y_test, estimator.predict(X_test))
        scores.append(result)

    return scores
