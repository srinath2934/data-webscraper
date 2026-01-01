# Part A — Landmark-Based Fetal Head Biometry

## Overview
This module estimates fetal head biometry using **landmark localization** from ultrasound images.
The goal is to predict landmarks defining **Biparietal Diameter (BPD)** and
**Occipitofrontal Diameter (OFD)** and compute these measurements automatically.

Both **direct coordinate regression** and **heatmap-based landmark regression**
are explored to improve robustness under noisy ultrasound conditions.

## Models Implemented
- **AlexNet** — Direct coordinate regression
- **ResNet-18** — Direct coordinate regression
- **ResNet-34** — Direct coordinate regression
- **Heatmap CNN (ResNet-18 backbone)** — Dense heatmap regression

## Approach
1. Input ultrasound image
2. Model predicts:
   - Coordinates (x, y), or
   - Landmark heatmaps
3. Extract landmark pairs for BPD and OFD
4. Compute distances using Euclidean geometry

## Training
- Multi-frame ultrasound data treated as independent samples
- Images resized and normalized
- Regression loss for coordinate models
- Pixel-wise loss on Gaussian heatmaps for heatmap model

## Testing & Evaluation
- Testing performed on **unseen images**
- Emphasis on **qualitative visualization**
- Heatmap landmarks extracted via argmax
- Visual inspection used to assess stability

## Files
- `Part_A_Train.ipynb` — Training
- `Part_A_testing.ipynb` — Testing & visualization
- `Model_Weights/` — Saved checkpoints

## Observations
- Heatmap regression improves spatial stability
- Coordinate regression is sensitive to blur and low contrast
- Landmark-based methods are efficient but limited by sparse supervision

## Notes
Multi-frame subject-level aggregation is identified as future work.

