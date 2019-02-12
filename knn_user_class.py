# ---------------------------------------- Import Libraries ---------------------------------------- #
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier as KNN
# ---------- Import Your Modules HERE ---------- #



if (__name__ == "__main__"):
    # ---------- Load HR Data For Both Users, Training sets ---------- #
    hr1_tr = 
    hr2_tr = 
    
    
    # ---------- Format Data ---------- #
    # Perform any format processing here
    #   This depends on the format you saved the data in.
    hr1_tr = 
    hr2_tr = 
    
    
    # ---------- Plot Both User's HR ---------- #
    plt.figure()
    # PLOT HERE
    plt.legend()
    plt.show()
    
    
    # ---------- Cropping Data ---------- #
    # It is VERY important that both classes / users have the same number of datapoints
    #   For example, if hr1_tr has length of 32 and hr2_tr has length of 40, randomly toss 8 datapoints from hr2_tr
    hr1_tr = 
    hr2_tr = 
    
    
    # ---------- Prepare Data For KNN ---------- #
    # For training, the KNN classifier is expecting two numpy arrays: data_tr and labels_tr
    #   data_tr:   must be a numpy array with dimensions (N, 1)
    #   labels_tr: must be a numpy array with dimensions (N)  
    # We need to concatenate hr1_tr and hr2_tr into a single array, and reshape it into (N, 1)
    data_tr = np.concatenate((hr1_tr, hr2_tr))
    data_tr = np.reshape((data_tr), [len(data_tr), 1])
    # Create labels
    labels_tr = np.concatenate((np.zeros(len(hr1_tr)), np.ones(len(hr2_tr))))
    
    
    # ---------- KNN ---------- # 
    # Create KNN object
    # K is set to 3, but you may user a different odd number
    K = 3
    neigh = KNN(n_neighbors = K)
    # Fit / train the KNN model
    neigh.fit(  # Pass correct parameters, here  )
    
    
    # ---------- Load HR Data For Both Users, Validation sets ---------- #
    hr1_va = 
    hr2_va = 
    
    
    # ---------- Format, Crop, and Prepare the data as you did above ---------- #
    data_va   = 
    labels_va = 
        
    
    # ---------- Classify Validation Data ---------- #
    # Get the predicted labels
    labels_va_pred = neigh.predict(  # Pass correct parameter, here  )
            
    
    # ---------- Plot Both User's HR and Predicted Labels ---------- #
    plt.figure()
    # PLOT HERE
    plt.legend()
    plt.show()
    
    
    # ---------- Calculate Accuracy ---------- #
    # Using the predicted labels and the actual labels, calculate the accuracy percentage
    acc = 
    print("Accuracy is: " + str(acc))




