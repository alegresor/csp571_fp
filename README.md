# CSP 571 Final Project: Predicting NBA player Salaries from Stats and NBA 2K Game Ratings

## Members

- Aleksei Sorokin
- Hyungtaeg Oh
- Arjuna Anilkumar
- Hardev Ranglani

## Reproducibility
Ensure `csp571_fp/` is in your R path when running `code/*.Rmd` files

## Files

`data/`
- `raw/` original primary and secondary dataset
- `pooled/` primary and complete, secondary, and complete (combined) datasets
- `train_test/` primary and complete train/test datasets for modeling
- `predictions/` optimal model predictions
- `glossary_*_vars.pdf` glossary of *primary* and *secondary* variables
- `optimal_model.*.rds` copy of optimal model from an algorithm 

`code/`
- `load_clean_explore_data.Rmd` data preparation
- `models_and_deployment.Rmd` build prediction models
- `deploy_optimal_model.R` deploy optimal model with API using *plumber* package
- `analyze_results.Rmd` explore optimal model predictions

`code_pdfs/` pdf renderings of `code/*.Rmd` files

`figures/` figures output by `code/*.Rmd` files

`depricated/`
- `load_data.Rmd` web scrape *every* NBA player from [espn.com](espn.com)
  - [Lebron James example](https://www.espn.com/nba/player/_/id/1966/lebron-james)
  - dataset was later replaced with `data/raw/primary_dataset_raw.xlsx` from Kaggle
- `load_2k_data.Rmd` merged into `code/load_clean_explore_data.Rmd`
- `clean_and_link_datasets.Rmd` merged into `code/load_clean_explore_data.Rmd`
