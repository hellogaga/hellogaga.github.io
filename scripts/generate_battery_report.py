#!/usr/bin/env python3
"""
Daily Battery Report Generator for Hugo Blog

Usage:
    python generate_battery_report.py
    python generate_battery_report.py --date 2026-02-27
    python generate_battery_report.py --data battery_data.json

This script generates a Hugo markdown post with interactive Plotly charts
for your daily battery status.
Customize the `get_battery_data()` function to pull from your actual data source.
"""

import argparse
import json
import os
from datetime import datetime, date


def get_battery_data(target_date: date, data_file: str = None) -> dict:
    """
    Replace this function with your actual data source.
    Could read from: CSV, API, database, SCADA system, etc.
    """
    if data_file and os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)

    # Sample data — replace with your real data pipeline
    return {
        "battery_id": "BESS-001",
        "date": target_date.isoformat(),
        "soh_percent": 96.2,
        "total_cycles": 2,
        "max_temp_c": 32.5,
        "min_temp_c": 18.3,
        "start_soc": 45.2,
        "end_soc": 41.3,
        "energy_charged_kwh": 1250,
        "energy_discharged_kwh": 1180,
        "profile": [
            {"time": "00:00", "power_kw": 0, "soc": 45.2, "temp_c": 18.3, "mode": "Idle"},
            {"time": "06:00", "power_kw": 250, "soc": 55.0, "temp_c": 20.5, "mode": "Charging"},
            {"time": "08:00", "power_kw": 250, "soc": 78.0, "temp_c": 25.5, "mode": "Charging"},
            {"time": "10:00", "power_kw": -200, "soc": 85.0, "temp_c": 28.5, "mode": "Discharging"},
            {"time": "14:00", "power_kw": -200, "soc": 32.1, "temp_c": 32.5, "mode": "Discharging"},
            {"time": "16:00", "power_kw": 250, "soc": 45.0, "temp_c": 27.5, "mode": "Charging"},
            {"time": "20:00", "power_kw": -180, "soc": 78.5, "temp_c": 29.5, "mode": "Discharging"},
            {"time": "23:59", "power_kw": 0, "soc": 41.3, "temp_c": 20.0, "mode": "Idle"},
        ],
        "observations": [
            "Two full cycles completed",
            "Temperature within normal range",
            "SoH stable — no degradation observed",
        ],
    }


def generate_plotly_soc_power(data: dict) -> dict:
    """Generate Plotly JSON for SoC + Power dual-axis chart."""
    times = [p["time"] for p in data["profile"]]
    socs = [p["soc"] for p in data["profile"]]
    powers = [p["power_kw"] for p in data["profile"]]

    return {
        "data": [
            {
                "x": times, "y": socs,
                "type": "scatter", "mode": "lines+markers",
                "name": "SoC (%)",
                "line": {"color": "#3b82f6", "width": 2},
                "marker": {"size": 6},
                "yaxis": "y",
            },
            {
                "x": times, "y": powers,
                "type": "bar",
                "name": "Power (kW)",
                "marker": {"opacity": 0.6},
                "yaxis": "y2",
            },
        ],
        "layout": {
            "title": {"text": f"Battery SoC & Power - {data['date']}", "font": {"size": 16}},
            "xaxis": {"title": "Time", "gridcolor": "#e5e7eb"},
            "yaxis": {"title": "State of Charge (%)", "range": [0, 100], "side": "left", "gridcolor": "#e5e7eb"},
            "yaxis2": {"title": "Power (kW)", "overlaying": "y", "side": "right", "range": [-400, 400], "gridcolor": "#e5e7eb"},
            "legend": {"x": 0.01, "y": 0.99, "bgcolor": "rgba(255,255,255,0.7)"},
            "hovermode": "x unified",
            "template": "plotly_white",
            "paper_bgcolor": "#ffffff",
            "plot_bgcolor": "#f9fafb",
            "font": {"color": "#333333"},
        },
    }


def generate_plotly_temperature(data: dict) -> dict:
    """Generate Plotly JSON for temperature chart with limits."""
    times = [p["time"] for p in data["profile"]]
    temps = [p["temp_c"] for p in data["profile"]]

    return {
        "data": [
            {
                "x": times, "y": temps,
                "type": "scatter", "mode": "lines+markers",
                "name": "Temperature (°C)",
                "line": {"color": "#ef4444", "width": 2},
                "fill": "tozeroy",
                "fillcolor": "rgba(239,68,68,0.1)",
            }
        ],
        "layout": {
            "title": {"text": f"Battery Temperature - {data['date']}", "font": {"size": 16}},
            "xaxis": {"title": "Time", "gridcolor": "#e5e7eb"},
            "yaxis": {"title": "Temperature (°C)", "range": [0, 45], "gridcolor": "#e5e7eb"},
            "shapes": [
                {"type": "line", "x0": times[0], "x1": times[-1], "y0": 35, "y1": 35,
                 "line": {"color": "red", "width": 2, "dash": "dash"}},
                {"type": "line", "x0": times[0], "x1": times[-1], "y0": 10, "y1": 10,
                 "line": {"color": "blue", "width": 2, "dash": "dash"}},
            ],
            "annotations": [
                {"x": times[-1], "y": 36, "text": "High Limit", "showarrow": False, "font": {"color": "red"}},
                {"x": times[-1], "y": 11, "text": "Low Limit", "showarrow": False, "font": {"color": "blue"}},
            ],
            "hovermode": "x unified",
            "template": "plotly_white",
            "paper_bgcolor": "#ffffff",
            "plot_bgcolor": "#f9fafb",
            "font": {"color": "#333333"},
        },
    }


def generate_markdown(data: dict) -> str:
    d = data["date"]
    profile_rows = "\n".join(
        f"| {p['time']} | {p['power_kw']:+d} | {p['soc']:.1f} | {p['mode']} |"
        for p in data["profile"]
    )
    observations = "\n".join(
        f"{i+1}. {obs}" for i, obs in enumerate(data["observations"])
    )

    return f"""---
title: "Battery Status - {d}"
date: {d}
summary: "Daily battery running status: SoH {data['soh_percent']}%, {data['total_cycles']} cycles, {data['energy_charged_kwh']} kWh charged."
categories:
  - Battery
tags:
  - battery
  - daily-report
  - energy-storage
---

## Battery Overview

| Metric | Value |
|---|---|
| Battery ID | {data['battery_id']} |
| Date | {d} |
| State of Health (SoH) | {data['soh_percent']}% |
| Total Cycles Today | {data['total_cycles']} |
| Max Temperature | {data['max_temp_c']}°C |
| Min Temperature | {data['min_temp_c']}°C |
| Energy Charged | {data['energy_charged_kwh']} kWh |
| Energy Discharged | {data['energy_discharged_kwh']} kWh |

## SoC & Power Profile (Interactive)

{{{{< plotly id="soc-power-chart" json="soc_power.json" height="450px" >}}}}

## Temperature Profile (Interactive)

{{{{< plotly id="temp-chart" json="temperature.json" height="400px" >}}}}

## Charge/Discharge Log

| Time | Power (kW) | SoC (%) | Mode |
|---|---|---|---|
{profile_rows}

## Key Observations

{observations}
"""


def main():
    parser = argparse.ArgumentParser(description="Generate daily battery report")
    parser.add_argument(
        "--date",
        type=str,
        default=None,
        help="Target date (YYYY-MM-DD). Defaults to today.",
    )
    parser.add_argument(
        "--data",
        type=str,
        default=None,
        help="Path to JSON data file",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="content/battery",
        help="Output directory for the report",
    )
    args = parser.parse_args()

    target_date = (
        datetime.strptime(args.date, "%Y-%m-%d").date()
        if args.date
        else date.today()
    )

    data = get_battery_data(target_date, args.data)
    markdown = generate_markdown(data)

    # Create output directory
    post_dir = os.path.join(args.output_dir, f"{target_date.isoformat()}-daily")
    os.makedirs(post_dir, exist_ok=True)

    # Write markdown
    output_path = os.path.join(post_dir, "index.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"Generated: {output_path}")

    # Write Plotly JSON chart data files
    soc_power_json = generate_plotly_soc_power(data)
    soc_path = os.path.join(post_dir, "soc_power.json")
    with open(soc_path, "w", encoding="utf-8") as f:
        json.dump(soc_power_json, f, indent=2)
    print(f"Generated: {soc_path}")

    temp_json = generate_plotly_temperature(data)
    temp_path = os.path.join(post_dir, "temperature.json")
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(temp_json, f, indent=2)
    print(f"Generated: {temp_path}")


if __name__ == "__main__":
    main()
