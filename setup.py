# # # -*- coding: utf-8 -*-
# # # @Author: Haozhe Xie
# # # @Date:   2019-08-07 20:54:24
# # # @Last Modified by:   Niels Rocholl
# # # @Last Modified time: 2024-09-04
# # # @Email:  nielsrocholl@gmail.com

from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='chamfer_dist',
    version='2.0.0',
    author='Niels Rocholl',
    author_email='nielsrocholl@gmail.com',
    description='A package for computing Chamfer Distance',
    # url='https://github.com/yourusername/chamfer_dist',  # Your repo URL
    packages=find_packages(),
    ext_modules=[
        CUDAExtension('chamfer_dist.chamfer', [
            'chamfer_dist/chamfer_cuda.cpp',
            'chamfer_dist/chamfer.cu',
        ]),
    ],
    cmdclass={'build_ext': BuildExtension}
)
