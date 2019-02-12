# ---------------------------------------- Import Libraries ---------------------------------------- #
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig
from sklearn.mixture import GaussianMixture as GM
import matplotlib.mlab as mlab
# ---------- Import Your Modules HERE ---------- #



if (__name__ == "__main__"):
    # ---------- Load Data ---------- #
    # Load numpy array
    data = np.load("Current Working Directory\ir_time_data.npy")
    # OR load from text file
    file = open("Current Working Directory\ir_time_data.txt", "r")
    data = file.readlines()
    
    
    # ---------- Format Data ---------- #
    # Perform any format processing here
    #   This depends on the format you saved the data in.
    #   At the end of this section, you should have two nmupy arrays
    #     data_ir:   holds raw IR values
    #     data_time: holds times stamps
    data_ir   = 
    data_time = 
    
    
    # ---------- Plot 5 sec of Raw Data ---------- #
    plt.figure()
    # PLOT HERE
    plt.show()
    
    
    # ---------- IR Digital Signal Processing ---------- #
    # Here you will use the DSP modules you created, in the previous lab, to:
    #   1. Scale the IR data
    #   2. Initialize Filter coefficients, and initial conditions, and other parameters (cutoff frequencies)
    #   3. Filter the IR signal (LPF, HPF)
    processed_ir = 
    
    
    # ---------- Split Data ---------- #
    # Do a 70/30 split on your data.
    # The GMM will be trained on the first 70% of your data.
    data_ir_tr   = 
    data_ir_va   = 
    data_time_tr = 
    data_time_va = 
    
    
    # ---------- Plot Histogram ---------- #
    # Plot the histogram of your training dataset, here.
    plt.figure()
    plt.hist(data_ir_tr, 50)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Count (#)")
    plt.title("IR Signal Histogram")
    
    
    # ---------- Find GMM ---------- #
    # Create GMM object
    gmm = GM(n_components = 2)
    
    # Fit 2 component Gaussian to the data
    gmm_fit = gmm.fit(  # Pass correct parameters, here  )
    
    # Retrieve Gaussian parameters
    mu0 = gmm_fit.means_[0]
    mu1 = gmm_fit.means_[1]
    sig0 = np.sqrt(gmm_fit.covariances_[0])
    sig1 = np.sqrt(gmm_fit.covariances_[1])
    w0 = gmm_fit.weights_[0]
    w1 = gmm_fit.weights_[1]
    
    
    
    # ---------- Plot Gaussians sum over histogram ---------- #
    x = np.reshape((np.linspace(np.min(data_ir_tr), np.max(data_ir_tr), 1000)), [1000, 1])
    plt.figure()
    plt.hist(data_ir_tr, bins=50, density=True)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Count (#)")
    plt.title("IR Signal Histogram")
    plt.plot(x, w0*mlab.normpdf(x, mu0, sig0) + w1*mlab.normpdf(x, mu1, sig1))
    
    # ---------- Plot two Gaussians over histogram ---------- #
    
    
    # ---------- Predict Labels ---------- #
    # Predict training labels
    train_pred_lbl = gmm_fit.predict(  # Pass correct parameters, here  )
    # Predict validation labels
    validation_pred_lbl = gmm_fit.predict(  # Pass correct parameters, here  )
    
    
    
    # ---------- Plot Training Set predictions ---------- #
                  
                  
    # ---------- Plot Validation Set predictions ---------- #
    
    
    # ---------- Store Training Set predictions ---------- #
                  
                  
    # ---------- Store Validation Set predictions ---------- #
    
    
    
