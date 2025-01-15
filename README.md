# Sarcomeric Z-Line Analysis

This repository contains tools and data for analyzing sarcomeric Z-lines, including images, skeleton branch information, and Python scripts for 2D autocorrelation and branch length analysis.

### Data
- **Images (A, B, C)**: Example images showcasing sarcomeric Z-line patterns.  
  - **Source**: [Dryad Dataset](https://datadryad.org/stash/dataset/doi:10.7280/D12Q2X)
  - **Processing**: The images were processed in FIJI using the following steps:
    1. Background subtraction
    2. Thresholding
    3. Skeletonize 2D to generate branch information.
- **Branch Information CSVs**: Datasets containing branch metadata generated from the processed images.

### Scripts
- **`autocorrelation_2d.py`**: Script for calculating 2D autocorrelation in Z-line patterns.
- **`sarc_skeleton2d.py`**: Script for analyzing Z-line branch length distributions and related metrics.

### System config
- Spyder IDE 5.4.3  (conda) with Python 3.9.16 64-bit
- DIPlib 3.4.1

