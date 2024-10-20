# drl-stock-trading-1
Based on Maxim Lapin's DRL Hands On book, Chapter 10 DRL for Trading

### Installation
After upgrading the required packages to the latest version, 
I had to install the following packages manually:

```
pip install opencv-python
```



Had to use Python version 3.8 for Conda environment

Install Pytorch v1.7 (required for ptan version)
```
conda install pytorch==1.7 cudatoolkit=10.2 -c pytorch -c nvidia

# Downgrade protobuf
pip install protobuf==3.20.0

```

### Example training command for the Simple DQN:
```
python train_model.py --cuda --run="botrain1"
```

### Example training command for the 1D Convolution DQN:
```
python train_model_conv.py --cuda --run="botrain1-conv"
```

### Example for running the model
Set --conv flag to False to use the Simple DQN Network.
Set --conv flag to True to use the 1D Conv Network.
```
python run_model.py --data="" --model="" --cuda --commission=0.0 --conv=False -n="borun1"
```

### Starting TensorBoard
1. Open command prompt
2. Activate virtual or conda environment
```
tensorboard --logdir=runs --port=8080
```
3. Open web browser and go to:
http://localhost:6006
