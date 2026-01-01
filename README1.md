
Landmark-Based Fetal Head Biometry
Overview

Part A focuses on estimating fetal head biometry using a landmark-based deep learning approach.
The objective is to predict anatomical landmarks corresponding to Biparietal Diameter (BPD) and Occipitofrontal Diameter (OFD) from ultrasound images and compute these measurements automatically.

This part explores both direct coordinate regression and heatmap-based landmark regression.

Models Implemented

The following models were trained and evaluated:

AlexNet – Direct landmark coordinate regression

ResNet-18 – Direct landmark coordinate regression

ResNet-34 – Direct landmark coordinate regression

Heatmap-Based CNN (ResNet-18 backbone) – Landmark localization via dense heatmap prediction

Approach

Each ultrasound image is provided as input to the model.

The model predicts either:

Direct landmark coordinates (x, y), or

Landmark probability heatmaps.

Landmark pairs corresponding to BPD and OFD are extracted.

Final biometry values are computed using Euclidean distance.

Training Strategy

Multi-frame ultrasound data is treated as independent samples.

Standard image preprocessing (resize, normalization) is applied.

Coordinate regression models are trained using regression loss.

Heatmap-based models are trained using pixel-wise loss on Gaussian landmark heatmaps.

Testing and Evaluation

Testing is performed on unseen ultrasound images.

Qualitative evaluation is emphasized through visualization of predicted landmarks.

Heatmap predictions are converted to coordinates using argmax operations.

Performance is analyzed visually rather than relying solely on numeric accuracy.

Files

Part_A_Train.ipynb – Training notebook for all Part A models

Part_A_testing.ipynb – Testing and visualization notebook

Model_Weights/ – Saved model weights

Key Observations

Heatmap-based regression provides improved spatial stability under noisy conditions.

Direct coordinate regression is sensitive to low-contrast and blurred frames.

Landmark-based approaches are efficient but limited by sparse supervision.
