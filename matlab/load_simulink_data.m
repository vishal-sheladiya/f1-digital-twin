clc;
clear;
close all;

data = readtable('../data/simulink_inputs.csv');

throttle = data.Throttle;

speed = data.Speed;

distance = data.Distance;

time = (0:length(throttle)-1)';

throttle_signal = [time throttle];

speed_signal = [time speed];