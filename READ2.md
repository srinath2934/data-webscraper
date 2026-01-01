# Part B — Segmentation-Based Fetal Head Biometry

## Overview
This module estimates fetal head biometry using **skull segmentation**.
A binary skull mask is predicted and used to compute **BPD** and **OFD**
via geometric post-processing.

## Models Implemented
- **U-Net**
- **Downsampling CNN**
- **ResNet-UNet**

## Segmentation-to-Biometry Pipeline
1. Ultrasound image input
2. Skull segmentation (binary mask)
3. Thresholding and cleanup
4. Largest contour extraction
5. Ellipse fitting
6. BPD & OFD from ellipse axes

## Training
- Pixel-wise supervision using skull masks
- Binary segmentation losses
- Frames treated as independent samples
- Pretrained encoders explored for feature extraction

## Testing & Evaluation
- Focus on **qualitative evaluation**
- Visual comparison against ground truth masks
- Ellipse fitting applied to valid predictions
- Dice and IoU reported for reference

## Files
- `Partb_Trainner.ipynb` — Training
- `Part_b_tester.ipynb` — Testing & visualization
- `Model_Weights/` — Saved checkpoints

## Key Findings
- U-Net and Downsampling CNN often predict empty masks
- ResNet-UNet produces partial but noisy skull segmentation
- Segmentation is more interpretable but significantly harder than landmarks

## Status & Future Work
- Training completed
- Testing in progress
- Future work includes improved losses, augmentation, and subject-level aggregation
