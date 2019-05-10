## Introduction
This folder includes exercises for playing with mujoco_py 

## Installation
Now the OpenAI mojuco_py module has supported mujoco 200. To install this module, you need to 
download lib from official mujoco web www.mujoco.org. Once the download the package, unzip the file
and put it in the default directory '$HOME/.mujoco/'. **Note thate the folder should be
named with mujoco200. While if you use dm_control, the folder should be named mujoco200_linux.**



To use the mujoco software, you need a license. You can buy it or apply a one-year student
license  for free. Once you get the license, put it under directory '$HOME/.mujoco/'. If necessay, 
copy it and put it under the bin folder in mujoco200.

Once all the stuff is done, you can clone the mujoco_py package and install
it with 'pip install -e .'

**Note: pip install with -e suffix can make the installed package be editable.
So any modification of the original code can be responded instantly.**

At last, import the module in python to make sure it works  correctly.

