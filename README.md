# IoT and Machine Learning Project

## Overview

This project applies machine learning techniques to detect and recognize ZigBee-connected IoT devices. The aim is to enhance security in IoT networks by simulating passive network attacks and identifying active connected devices. The project explores various IoT transport protocols and develops strategies for mitigating potential threats.

## Table of Contents

1. [Introduction](#introduction)
2. [Technologies and Protocols](#technologies-and-protocols)
3. [Hardware and Software Requirements](#hardware-and-software-requirements)
4. [Methodology](#methodology)
5. [Results](#results)
6. [Limitations and Future Work](#limitations-and-future-work)
7. [Contributors](#contributors)

## Introduction

The security of IoT (Internet of Things) networks is critical, especially with the widespread use of protocols like ZigBee, Z-Wave, and LoRa. This project focuses on recognizing ZigBee-connected devices by capturing network traffic and analyzing it using machine learning models. The goal is to detect vulnerabilities and develop effective security strategies to protect IoT networks from potential threats.

## Technologies and Protocols

### Protocols Analyzed

- **ZigBee**: A low-power, low-cost wireless mesh network standard used in many IoT applications.
- **Z-Wave**: A wireless communication protocol primarily for home automation, enabling secure device communication.
- **LoRa**: A long-range, low-power wireless platform designed for Internet of Things networks.

### Network and Application Layers

The project also involves studying protocols such as TCP/UDP and HTTP and examining packet protection mechanisms, including SSL keys.

## Hardware and Software Requirements

### Hardware

- **HackRF**: A versatile software-defined radio used to capture wireless communications.

### Software

- **Wireshark**: For capturing and analyzing network packets.
- **BurpSuite**: For modifying and inspecting network traffic.
- **Dumpcap**: A tool for capturing network packets.
- **Scapy**: For data extraction and manipulation.
- **Pandas**: A Python library used for data analysis and managing datasets.

## Methodology

The project employs a step-by-step approach to identify ZigBee-connected IoT devices:

1. **Data Capture**: Using tools like Dumpcap to capture network traffic.
2. **Data Processing**: Utilizing Scapy and Pandas to extract and process the captured data.
3. **Machine Learning Model Development**: Training models to recognize and classify different IoT devices based on the processed data.
4. **Evaluation**: Assessing the performance of the models using various metrics to ensure accuracy and reliability.

## Results

The machine learning models developed were successful in identifying ZigBee-connected IoT devices with high accuracy. The project demonstrated that:

- **Device Recognition**: The models could accurately distinguish between different types of ZigBee devices based on network traffic patterns.
- **Anomaly Detection**: The models effectively detected anomalies in network behavior, which could indicate potential security breaches or unauthorized device activities.
- **Performance Metrics**: The models showed strong performance metrics, including precision, recall, and F1-score, indicating their effectiveness in real-world IoT environments.
- **Scalability**: The approach can be scaled to include other IoT protocols, enhancing the robustness and applicability of the security measures developed.

## Limitations and Future Work

While the project successfully recognized ZigBee-connected devices, there are areas for improvement:

- **Expanding Protocol Coverage**: Including more IoT protocols beyond ZigBee to create a more comprehensive security solution.
- **Improving Data Capture Techniques**: Enhancing data capture methods to improve model accuracy and robustness.
- **Real-World Testing**: Conducting more extensive testing in diverse real-world environments to validate the models further.
- **Automated Threat Response**: Developing automated systems that can respond to detected threats in real-time to prevent potential security breaches.

## Contributors

- Abdennacer Badaoui
- Louis Fouché
- Emma Guetta
- Reda Mouqed
- Rémy Taha

Supervised by Jocelyn Fiorina with the collaboration of L'Exocube.

## Acknowledgments

This project was part of the Security and Defense module at CentraleSupélec, conducted in June 2022.

