### Chamfer Distance

Cuda implementation of Chamfer Distace, can be used on the GPU. This code is originally from [GRNet](https://github.com/hzxie/GRNet/tree/master/extensions/chamfer_dist) written by Haozhe Xie. 

For easy incorporation into other project, i changed the setup.py such that we can create a python package that can be installed through pip. 

You can now install this package through:
```
pip install git+https://github.com/nielsRocholl/chamfer-distance.git
```

After installing, you can import the distance function:
```
from chamfer_dist import ChamferDistanceL1, ChamferDistanceL2
```