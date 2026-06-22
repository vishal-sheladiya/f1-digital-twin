clc;
clear;
close all;

telemetry = readtable('../data/ver_monza_telemetry.csv');

class(telemetry.Brake)

figure;

plot(telemetry.Distance, telemetry.Speed, 'LineWidth', 2);

grid on;

xlabel('Distance [m]');
ylabel('Speed [km/h]');
title('Verstappen Monza Speed Trace');

figure;

plot(telemetry.Distance, telemetry.RPM, 'LineWidth', 2);

grid on;

xlabel('Distance [m]');
ylabel('RPM');
title('Verstappen RPM Trace');

brake_numeric = strcmp(telemetry.Brake, 'True') * 100;

figure;

plot(telemetry.Distance, telemetry.Throttle, 'LineWidth', 2);

hold on;

plot(telemetry.Distance, brake_numeric, 'LineWidth', 2);

legend('Throttle','Brake');

grid on;

xlabel('Distance [m]');
ylabel('Input [%]');

title('Driver Inputs');

figure;

plot(telemetry.Distance, telemetry.nGear, 'LineWidth', 2);

grid on;

xlabel('Distance [m]');
ylabel('Gear');

title('Gear Trace');