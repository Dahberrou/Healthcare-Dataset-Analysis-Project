healthcare_data = LOAD '/user/healthcare-project1/healthcare-project1.csv' USING PigStorage(',') AS (
    date:chararray,
    county:chararray,
    total_cases:int,
    new_cases:int,
    total_confirmed:int,
    new_confirmed:int,
    total_probable:int,
    new_probable:int,
    pos_tests:int,
    new_pos_tests:int,
    neg_tests:int,
    new_neg_tests:int,
    total_tests:int,
    new_tests:int,
    new_deaths:int,
    total_deaths:int,
    new_active:int,
    total_active:int,
    new_inactive_recovered:int,
    total_inactive_recovered:int,
    new_hospitalized:int,
    total_hospitalized:int,
    total_deaths_by_dod:int
);

-- Filter rows with missing values
filtered_data = FILTER healthcare_data BY total_cases IS NOT NULL;

-- Group by county
grouped_data = GROUP filtered_data BY county;

-- Calculate total cases per county
total_cases_per_county = FOREACH grouped_data GENERATE group AS county, SUM(filtered_data.total_cases) AS 
total_cases;

-- Store the result
STORE total_cases_per_county INTO '/user/healthcare-project1/output';
