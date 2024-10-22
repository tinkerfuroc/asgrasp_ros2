# ASgrasp implement for ros2

## Install
```
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2  # pytorch2.0.1+cu117

git clone https://github.com/NVIDIA/MinkowskiEngine.git
cd MinkowskiEngine
python setup.py install --user --blas=openblas

cd gsnet/pointnet2
python setup.py install --user

pip install autolab_core cvxopt grasp_nms

```
