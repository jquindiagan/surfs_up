# Surf's Up

## Overview of Project

### Purpose

The purpose of this analysis was to practice using Python, Pandas functions and methods, and SQLAlchemy to analyze Oahu's temperature trends in order to determine if the surf and ice cream shop business is sustainable year-round.

## Results

Below is a summary of temperatures for June (left) and December (right).

<p align="center"><img src="resources/jun_summary.png" height="25%" width="25%"> <img src="resources/dec_summary.png" height="25%" width="25%"></p>

Key differences:
- **mean**: The average temperature in the month of June was 74 degrees while the average temperature in December was 71.
- **min**: The lowest temperature in June was 64 degrees but 56 degrees in December.
- **max**: The highest temperature in June was 85 degrees while December's highest temperature was 83 degrees.

## Summary

While the difference in the lowest temperatures for the month is eight percent, there is only a two to three percent difference in other areas such as the average and highest temperatures.
We can conclude that the surf and ice cream shop business can be sustainable year-round.

### Additional queries

1. An additional query performed was to filter the June and December data sets to a single year. The most recent and complete data set was analyzed, which was the year 2016.

    Below is a summary of temperatures for June (left) and December (right).

    <p align="center"><img src="resources/jun16_summary.png" height="25%" width="25%"> <img src="resources/dec16_summary.png" height="25%" width="25%"></p>

    Unlike the initial query, the minimum temperature for June and December in 2016 was only a four percent difference. The percentage differences in other areas stayed consistent, with the difference increasing three to four percent.

2. To gain a better understanding of the temperature year-round, a query was performed to compare the June and December temperatures to other months in the year. The entire year of 2016 was analyzed.

    <img src="resources/y2016_temp.png" align="center">

    <p align="center"><img src="resources/y2016_summary.png" width="25%" height="25%"></p>

    The graph and summary above shows that other than peak temperatures in August, temperatures range in the 70's year-round.