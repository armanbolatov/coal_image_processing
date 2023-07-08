# Image Processing for Evaluating Hydraulic Fracturing

This repository contains the resources for the article ["Application of Image Processing in Evaluation of Hydraulic Fracturing with Liquid Nitrogen: A Case Study of Coal Samples from Karaganda Basin."](https://www.mdpi.com/2076-3417/13/13/7861)

## Repository Structure

- `data`: Contains processed and raw images of coal samples before and after fracturing.
- `results`: Includes comparisons of processes and all other figures presented in the article.
- `get_stats.ipynb`: The main notebook that generates the figures in the results folder.
- `dilate_erode.py`: A script to execute the dilation and erosion morphological operations.
- `preprocess.py`: A script to run the image processing pipeline.

## Citation
```
@article{Longinos2023,
  doi = {10.3390/app13137861},
  url = {https://doi.org/10.3390/app13137861},
  year = {2023},
  month = jul,
  publisher = {{MDPI} {AG}},
  volume = {13},
  number = {13},
  pages = {7861},
  author = {Sotirios Nik. Longinos and Azza Hashim Abbas and Arman Bolatov and Piotr Skrzypacz and Randy Hazlett},
  title = {Application of Image Processing in Evaluation of Hydraulic Fracturing with Liquid Nitrogen: A Case Study of Coal Samples from Karaganda Basin},
  journal = {Applied Sciences}
}
```

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/armanbolatov/coal_image_processing/blob/main/LICENSE)