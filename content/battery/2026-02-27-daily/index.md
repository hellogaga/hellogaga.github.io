---
title: "Battery Status - February 27, 2026"
date: 2026-02-27
summary: "Daily battery running status summary with charge/discharge cycles and health metrics."
categories:
  - Battery
tags:
  - battery
  - daily-report
  - energy-storage
---

## Battery Overview

| Metric                | Value      |
| --------------------- | ---------- |
| Battery ID            | BESS-001   |
| Date                  | 2026-02-27 |
| State of Health (SoH) | 96.2%      |
| Total Cycles Today    | 2          |
| Max Temperature       | 32.5°C     |
| Min Temperature       | 18.3°C     |
| Energy Charged        | 1,250 kWh  |
| Energy Discharged     | 1,180 kWh  |

## SoC & Power Profile (Interactive)

{{< plotly id="soc-power-chart" json="soc_power.json" height="450px" >}}

## Temperature Profile (Interactive)

{{< plotly id="temp-chart" json="temperature.json" height="400px" >}}

## Charge/Discharge Log

| Time  | Power (kW) | SoC (%) | Mode        |
| ----- | ---------- | ------- | ----------- |
| 00:00 | 0          | 45.2    | Idle        |
| 06:00 | +250       | 45.2    | Charging    |
| 08:00 | +250       | 85.0    | Charging    |
| 10:00 | -200       | 85.0    | Discharging |
| 14:00 | -200       | 32.1    | Discharging |
| 16:00 | +250       | 32.1    | Charging    |
| 20:00 | -180       | 78.5    | Discharging |
| 23:59 | 0          | 41.3    | Idle        |

## Key Observations

1. **Two full cycles completed** — Morning charge/discharge and afternoon charge/evening discharge
2. **Temperature within normal range** — Peak at 32.5°C during afternoon discharge
3. **SoH stable** — No degradation observed compared to yesterday

## Notes

This is a sample daily battery report. Charts are interactive — hover to see values, zoom, and pan. You can automate this with a Python script that generates both the markdown and JSON data files.
