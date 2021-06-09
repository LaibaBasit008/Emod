#Laiba basit
#Alina tabish
#Ayesha muqeem

from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score
from utils import load_data

import os
import pickle

# load RAVDESS dataset
X_train, X_test, y_train, y_test = load_data(test_size=0.25)
# training data
print("[+] Number of training samples:", X_train.shape[0])
#  testing data
print("[+] Number of testing samples:", X_test.shape[0])
# features used

print("[+] Number of features:", X_train.shape[1])
# best model, determined by a grid search
model_params = {
    'alpha': 0.01,
    'batch_size': 256,
    'epsilon': 1e-08, 
    'hidden_layer_sizes': (300,), 
    'learning_rate': 'adaptive', 
    'max_iter': 500, 
}
#  Multi Layer Perceptron classifier
model = MLPClassifier(**model_params)
# Train the model
print("[*] Training the model...")
model.fit(X_train, y_train)
# Predict 25% of 
y_pred = model.predict(X_test)
# Calculate the accuracy
accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

# Make result directory if doesn't exist yet
if not os.path.isdir("result"):
    os.mkdir("result")
pickle.dump(model, open("result/mlp_classifier.model", "wb"))#storing result
