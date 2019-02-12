# ---------------------------------------- Import Libraries ---------------------------------------- #
import numpy as np
from sklearn.mixture import GaussianMixture as GM
# ---------- Import Your Modules HERE ---------- #


# Fits a Gaussian Mixture Model based on "data_tr"
# The fit is done based on the assumption that there are "num_classes" number of classes in our data.
#   In our case, the assumption is that there are 2.
def fit_GMM(data_tr, num_classes=2):
    # Create GMM object
    gmm = GM(n_components = num_classes)
    # Fit 2 component Gaussian to the data
    gmm_fit = gmm.fit(  # Pass correct parameters, here  )
    # Return the GMM fit object
    return gmm_fit


# Predicts the class of each data point in our "data", based on our fitted GMM ("gmm_fit")
def predict(gmm_fit, data):
    # Make class prediction
    pred_lbl = gmm_fit.predict(  # Pass correct parameters, here  )
    # Return the class predictions / labels
    return pred_lbl


# Use your algorithm to calculate the heart rate.
#   Remember, the labels themselves don't tell you the heart rate.
#   On top of everything, the labels could be wrong at times.
#   It is up to you to decipher what the labels are telling you, and when they could be wrong.
def calculate_hr(labels, timestamps):
    # YOUR ALGORITHM GOES HERE
    return hr_array
