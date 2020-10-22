# Download WebEmo dataset

Note: Modified README to be compatible with markdown, and added download script. The dataset and contact belong to Rameswar Panda (rpand002@ucr.edu)

# Dataset: WEBEmo

## Overview
The WEBEmo dataset contains 267441 high quality stock photos across 25 fine-grained emotion categories. Here, we provide all the urls to download those images. The dataset contains both training and test partitions as indicated in two separate .txt files. We hope our efforts in releasing this emotion benchmark will open up avenues for facilitating progress in this emerging area of computer vision. 

Note that although all the image urls given in the dataset were available to downlaod while preparing the dataset in July 2017, it might be the case that the uploading party, subsequent to our preparation of this dataset, have either removed or modified the license. Before using the stock photos we encourage you to review whether the activities you intend to perform in connection with this dataset comply with intellectual property laws. We do not provide any assurances, or makes any representations, under intellectual property law, or otherwise, regarding your use of this dataset. 

If you have any questions on the dataset, please contact:
Rameswar Panda (rpand002@ucr.edu)


## Contents
This dataset contains three txt files:
```
(1) category.txt
(2) train25.txt
(3) test25.txt
```
(1) `category.txt`: This txt file contains the three-level emotion hierarchy, starting from two
basic categories (positive and negative) at level-1, six categories (anger, fear, joy, love, sadness, and surprise) at level-2 to 25 fine-grained emotion categories.

E.g., ('affection', 'love', '+') indicates "positive" emotion at level-1, "love" emotion at level-2, and "affection" emotion at level-3.

(2) `train25.txt`: This txt files contains the urls of 213952 images that are used to train the models.

E.g., https://as2.ftcdn.net/jpg/00/42/93/78/220_F_42937802_2rowA8aFZs20JZ2Iq6WKArKKaaj1BIv4.jpg 0
indicates that "0" (i.e., affection) as the emotion at level-3. 

(3) `test25.txt`: This txt files contains the urls of 53489 images that are used to test the models.
-------------------------------------------------------------------------------------

Please cite our paper if you find it useful for your research.
```
>@inproceedings{panda2018contemplating,
>  title={Contemplating Visual Emotions: Understanding and Overcoming Dataset Bias},
>  author={Panda, Rameswar and Zhang, Jianming and Li, Haoxiang and Lee, Joon-Young and Lu, Xin and Roy-Chowdhury, Amit K},
>  booktitle = {European Conference on Computer Vision},
>  year={2018}
>}
```
 




