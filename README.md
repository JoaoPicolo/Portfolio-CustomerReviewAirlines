# Portfolio Airline Customer Review

<p align="center">
  <img style="width: 100px" src="./assets/logo.png" alt="Project's logo"/>
</p>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![Build Status](https://app.travis-ci.com/JoaoPicolo/Portfolio-CustomerReviewAirlines.svg?branch=main)](https://app.travis-ci.com/JoaoPicolo/Portfolio-CustomerReviewAirlines)
  [![codecov](https://codecov.io/gh/JoaoPicolo/Portfolio-CustomerReviewAirlines/branch/main/graph/badge.svg?token=9EQYB1J5VD)](https://codecov.io/gh/JoaoPicolo/Portfolio-CustomerReviewAirlines)

</div>

---

Project develope to collect customer's airlines reviews from [SkyTrax](https://www.airlinequality.com/).

The description of the steps taken during the development can be found on [Medium](https://picolojoaop.medium.com/airline-customer-review-web-scraping-1e812a79b995).

**NOTE:** you may need to change the source files to fit your needs, feel free to do it. If any help is necessary, please contact me.

## Data structure

The airlines to be processed are located under the directory *./data/helpers/airlines.json*, if any airline need to be added in the future, just update this file.

## Run project

The project was designed to run in a specific order. Execute the following commands in the *.src/* directory.

### Web Scraping

To collect the data run:

```bash
python3 scrap.py -i ../data/helpers/airlines.json -o ../data/raw
```

The *-i* argument specifies the path to the json were the airlines data is stored (section **Data Structure**), and the *-o* argument specifies the output directory where the collected data will be stored.

### Data Cleaning

To clean the collected dataset, in the same folder run:

```bash
python3 clean.py -i ../data/raw
```

The *-i* argument specifies the path were the datasets to be cleaned are stored. If a file is provided, then only this dataset will be cleaned.

It's important to note that the cleaned datasets will be stored under **../data/interim** so make sure to have follow the proposed tree structure.

### Merge Datasets

Finally, to integrate all the collected data to be used in future steps, e.g., a Power BI dashboard just run:

```bash
python3 merger.py -i ../data/interim -o ../data/processed/reviews.csv
```

The *-i* argument specifies the location of the datasets to be merged, and the *-o* argument specifies the file were the merged dataset will be saved.

It's important to note that all the datasets to be merged must have the same headers names, otherwise this code will not work.
