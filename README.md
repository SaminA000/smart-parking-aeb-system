# Smart Parking Sensor & Emergency Braking System

A Python-based simulation of a car parking sensor system that utilizes Object-Oriented Programming (OOP) to detect obstacles and trigger an Automatic Emergency Braking (AEB) system.

## Project Overview

This project simulates how hardware sensors interact with vehicle control systems. It is organized into a modular, multi-tier architecture using three distinct classes:
1.  **ParkingSensor**: The base class handling power states and general occupancy logic.
2.  **Proximity**: A specialized sensor class that calculates distance, provides auditory/visual feedback ("beeping"), and monitors safety thresholds.
3.  **Car**: A vehicle class that manages speed (MPH) and responds to external safety overrides.

## Project Architecture

The project is structured into logical packages to demonstrate professional software organization:

```text
.
├── main.py                     # Entry point - Orchestrates the simulation
├── Sensor_lib/
│   ├── __init__.py
│   ├── ParkingSensor.py        # Base Sensor Class
│   └── Proximity.py            # Advanced Proximity & Safety Logic
└── VehicleInformation/
    ├── __init__.py
    └── Car.py                  # Vehicle Model and Controls
