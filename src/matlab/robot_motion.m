
clc; clear; close all;

% Define robot parameters
robotSpeed = 2; % speed in m/s
timeInterval = 0:0.1:10; % time vector

% Compute distance traveled
distance = robotSpeed * timeInterval;

% Plot robot movement
figure;
plot(timeInterval, distance, 'b-', 'LineWidth', 2);
xlabel('Time (seconds)');
ylabel('Distance (meters)');
title('Robot Motion Control');
grid on;
