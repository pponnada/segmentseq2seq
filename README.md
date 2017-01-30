# segmentseq2seq
Multi-layer Sequence to Sequence Recurrent Neural Networks for storage block models in Tensorflow

This code implements a multi-layer Sequence to Sequence Recurrent Neural Network for training and predicting a sequence of block offsets given an input of sequence of block offsets. To train the model, an input file with a sequence of block offsets and a labels file with the corresponding block offsets (to be predicted) are input the model. 10% of the data from the trace file is held out as test data to predict block accesses.

OLTP block storage traces for training this model have been downloaded from [umass website](http://traces.cs.umass.edu/index.php/Storage/Storage). Details of the traces and preprocessing performed on the traces are descrived in a separate [blog](https://pponnada.github.io/2017/01//27/storage-segment-prediction.html) post. 

# Requirements
This code is written in python 3.5 and requires [Tensorflow] (https://www.tensorflow.org/get_started/os_setup). I trained this model on 64 bit Ubuntu, Tensorflow 12.1 with GPU support. 

# Usage
## Data
Data is stored in the datasets directory. If the file `Financial1.spc` file is not found in the datasets directory, it is downloaded from the [umass](http://skuld.cs.umass.edu/traces/storage/Financial1.spc.bz2) website.

## Training
To train the model edit the file `predict.py` so as to make `train_model = True`. 

## Prediction
To predict a sequence of block offsets, edit the file `predict.py` so as to make `train_model = False`. A random sequence of blocks of size batch size from the test data will be input to the model for it make its predictions. A corresponding plot of predicted v/s actual sequence of blocks with a file name `predict-*freq-*win-*.png` will be saved in the parent directory. Depending upon the hyperparameters, number of epochs chosen and the data drawn randomly from the test input, a plot similar to the one below will be generated.

![predictions](https://raw.githubusercontent.com/pponnada/segmentseq2seq/plots/predict-1024freq-5win-64.png)



