
# Importing necessary libraries
import math
import numpy as np
import pandas as pd
from scipy import stats

# Defining needed functions

def get_stats(X):
    """
    Calculate basic statistics of a given data set.
    """
    n = len(X)
    x = X.mean()
    s = X.std(ddof=1)
    return (n,x,s)


def t_value(n_v, x_v, s_v, n_c, x_c, s_c):

    s_v_n_v = np.square(s_v)/n_v
    s_c_n_c = np.square(s_c)/n_c
    numerator = x_v-x_c
    denominator = np.sqrt(s_v_n_v+s_c_n_c)
    t = numerator/denominator

    return t

def t_value(n_v, x_v, s_v, n_c, x_c, s_c):

    s_v_n_v = np.square(s_v)/n_v
    s_c_n_c = np.square(s_c)/n_c
    numerator = x_v-x_c
    denominator = np.sqrt(s_v_n_v+s_c_n_c)
    t = numerator/denominator

    return t

def p_value(d, t_value):
    t_d = stats.t(df=d)
    p = 1-t_d.cdf(t_value)
    return p

def make_decision(X_v, X_c, alpha = 0.05):

    n_v, x_v, s_v = get_stats(X_v)

    n_c, x_c, s_c = get_stats(X_c)

    d = degrees_of_freedom(n_v, s_v, n_c, s_c)

    t = t_value(n_v, x_v, s_v, n_c, x_c, s_c)

    p = p_value(d, t)

    if p<alpha:
        return 'Reject H_0'
    else:
        return 'Do not reject H_0'

# Load the data from the test
data = pd.read_csv("background_color_experiment.csv")
# Print the first 10 rows
data.head(10)
print(f"The dataset size is: {len(data)}")

# Separate the data from the two groups (sd stands for session duration)
control_sd_data = data[data["user_type"]=="control"]["session_duration"]
variation_sd_data = data[data["user_type"]=="variation"]["session_duration"]

# X_c stores the session tome for the control group and X_v, for the variation group.
X_c = control_sd_data.to_numpy()
X_v = variation_sd_data.to_numpy()

n_c, x_c, s_c = get_stats(X_c)
n_v, x_v, s_v = get_stats(X_v)

d = degrees_of_freedom(n_v, s_v, n_c, s_c)
print(f"The degrees of freedom for the t-student in this scenario is: {d:.2f}")

t = t_value(n_v, x_v, s_v, n_c, x_c, s_c)
print(f"The t-value for this experiment is: {t:.2f}")

t_10 = stats.t(df = 10)
cdf = t_10.cdf(1.21)
print(f"The CDF for the t-student distribution with 10 degrees of freedom and t-value = 1.21, or equivalently P(t_10 < 1.21) is equal to: {cdf:.2f}")

alphas = [0.06, 0.05, 0.04, 0.01]
for alpha in alphas:
    print(f"For an alpha of {alpha} the decision is to: {make_decision(X_v, X_c, alpha = alpha)}")
