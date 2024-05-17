# TekkenAI
I'm trying to make my own bot that can play Tekken 8 via neural networks and computer vision, instead of the option that the game gives me. I **WILL NOT** share my finished code, since I don't want people to use it for online play (you might get banned). But, I'll make a complete video about it once I'm 100% done. I'm just using this repository to keep track of what I've done so far.

## Part 1: IDE Setup
Did a clean reinstall of Ubuntu 24.04 for WSL, redownloaded [OpenCV](https://opencv.org/), [PyTorch](https://pytorch.org/) and [Anaconda](https://www.anaconda.com/), as well as installing [Ultralytics and YOLOv8](https://github.com/ultralytics/ultralytics). This took a day.

## Part 2: Recording Gameplay
Downloaded the PC Version of Tekken 8 and used the [Nvidia app](https://www.nvidia.com/en-us/software/nvidia-app/) for recording gameplay. I did 31 fights with my main, with one round being recorded. The fights consist of me versus the hardest Super Ghost. The position, stage, round that's being captured and ability to use Rage or Heat is randomized. My hope is that this bot can play as anyone instead of just Xiaoyu, since I really don't want to record 528 fights. This took two days.

## Part 3: Preprocessing
From the 31 videos, I seperated them into 3 datasets: train, valid and test. I then created a Python script using OpenCV where I split the dataset into separate frames. The amount of frames were around 3150 for Training, close to 1000 for Validation and 500 for Testing. This took a couple of hours.

## Part 4: Object Detection and Roboflow
I then uploaded the images on [Roboflow](https://universe.roboflow.com/), where I create bounding boxes for objects, including enemies, players, their health, blocks and hits. Currently I'm 27% finished with the Training dataset and I expect object detection for all three datasets to be done by the end of May, since I'm also applying for Fall 2024 Co-Ops/Internships, which takes up time. This will probably be the longest part.
