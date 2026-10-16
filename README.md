# FINE3300-2026-A1
FINE3300, Fall 2026, Assignment 1

## Assignment Description

In this assignment, two exchange rate calculators are created. One is designed manually using Visual Studio Code, and the second, using Vibe Coding that uses a Large Language Model (LLM) to write code in accordance to prompt specifications.

### Assignment Specifics

#### Part 1: Exchange Rates

Must create a currency calculator that prompts the user for 3 inputs; an amount, the corresponding currency to the inputted amount, and the currency you'd like to convert to. 

In detail, a class must be create that takes a CSV file containing different currency conversions, including but not limited to USD to CAD, and finds the appropriate conversion rates between these currencies. In addition, a function must be created to accurately convert from one currency to another in accordance with the user inputs.

#### Part 2: Vibe Coding

Must specify a prompt to a LLM model of your choice to complete Part 1 of the assignment independently, focusing on high level requirements to allow the model to focus on technical implementation. Ensure accuracy through testing and compare written code vs the models code.

## Comparison & Write-up

### Write-up

#### Link to GitHub Repository

https://github.com/abdullah-ziaa/FINE3300-2026-A1.git

#### Program Output for $100,000 USD to CAD, and vice versa.

USD to CAD Output
> $100000.0 USD is equal to $139780.0 CAD.

CAD to USD Output
> $100000.0 CAD is equal to $71540.99 USD.

#### LLM Model & Prompt

LLM Model
> Claude Sonnet 5.5, Effort Level = Medium

Prompt
> "I need you to design an exchange rate calculator in python. Design a class (called Exchange Rates) that will read an exchange rate (USD to CAD, or vice versa only, though others may exist within the file) from a provided data file containing annual exchange rates reporting by the Bank of Canada in csv format.  Then write a method/function (called convert) that will take an input for the amount and 2 separate currency entries (USD or CAD), and converts from one currency to another using the exchange rate read from the file. Prompt the user to specify the amount, the 'from' & 'to' currency i.e. USD or CAD.  Assume users will provide legitimate input values so no validation checks will be performed on the input values and format the output so that it is rounded to the nearest penny, incorporates, dollar signs, and currency identifiers."

**NOTE:** In addition to the prompt, I uploaded the given Bank of Canada Exchange Rate File provided in the assignment to assist with implementation.

### Comparison