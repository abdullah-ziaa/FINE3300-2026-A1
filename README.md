# FINE3300-2026-A1
FINE3300, Fall 2026, Assignment 1

## Assignment Description

In this assignment, two exchange rate calculators are created. One is designed manually using Visual Studio Code, and the second, using Vibe Coding that uses a Large Language Model (LLM) to write code in accordance to prompt specifications.

### Assignment Specifics

#### Part 1: Exchange Rates

Must create a currency calculator that prompts the user for 3 inputs; an amount, the corresponding currency to the inputted amount, and the currency you'd like to convert to. 

In detail, a class must be created that takes a CSV file containing different currency conversions, including but not limited to USD to CAD, and finds the appropriate conversion rates between these currencies. In addition, a function must be created to accurately convert from one currency to another in accordance with the user inputs.

#### Part 2: Vibe Coding

Must specify a prompt to an LLM of your choice to complete Part 1 of the assignment independently, focusing on high level requirements to allow the model to focus on technical implementation. Ensure accuracy through testing and compare written code vs the models code.

## Comparison & Write-up

### Write-up

#### Link to GitHub Repository

https://github.com/abdullah-ziaa/FINE3300-2026-A1.git

#### Program Output for $100,000 USD to CAD, and vice versa.

USD to CAD Output
> $100000.0 USD is equal to $139780.0 CAD.

CAD to USD Output
> $100000.0 CAD is equal to $71540.99 USD.

#### LLM & Prompt

LLM
> Claude Sonnet 5.5, Effort Level = Medium

Prompt
> "I need you to design an exchange rate calculator in python. Design a class (called Exchange Rates) that will read an exchange rate (USD to CAD, or vice versa only, though others may exist within the file) from a provided data file containing annual exchange rates reported by the Bank of Canada in csv format. Then write a method/function (called convert) that will take an input for the amount and 2 separate currency entries (USD or CAD), and converts from one currency to another using the exchange rate read from the file. Prompt the user to specify the amount, the 'from' & 'to' currency i.e. USD or CAD.  Assume users will provide legitimate input values so no validation checks will be performed on the input values and format the output so that it is rounded to the nearest penny and incorporates dollar signs and currency identifiers."

**NOTE:** In addition to the prompt, I uploaded the given Bank of Canada Exchange Rate File provided in the assignment to assist with implementation.

### Comparison

#### My Code Analysis + LLM Code Analysis + Comparison

To initially read the file in the ExchangeRates class, my version opens the file, reads it, and then splits it into an array by each comma. The first row contains the currencies and the last row contains the most recent currency conversion rates, so my code splits the first and last row. It then finds the column index at which the USD to CAD conversion sits in the first row, uses that index to find the most recent non-empty conversion value, and then defines variables for conversions between the two currencies. Once conversion rates are computed, my version creates a function that, using user inputs of amount and to and from currencies (USD and CAD), returns the computed currency conversion. My code uses an instance of the ExchangeRates class to gather the exchange rates from the given CSV file, and then prompts the user to enter the desired amount as well as the to and from currencies. These inputs are then used to compute the appropriate conversion using the convert function, and then rounded. The final result is printed out in an easy to read sentence in accordance to user inputs. In comparison, in the LLM code, to read the file in the ExchangeRates class, it initializes a dictionary and opens the file in a different way, using a "with" block and reads it through an imported csv module as well as using "DictReader" and "utf-8-sig" encoding. This loops through the entire data as opposed to reading the file and splitting based on a specific condition. While looping through the data, it extracts the 4-digit number for the rows' years, and eventually finds the latest year and its corresponding rate. This differs from my code as it loops the entire data instead of finding the "FXAUSDCAD" instance index and then scanning from the bottom row and up in the corresponding indexes to find the latest currency conversion. It does not compute the CAD to USD rate alongside the USD to CAD like I have. With the stored rate, it continues on to create the convert function that takes the amount and the to and from currencies. Given the inputs, it rids the entries of any whitespace and capitalizes the currency to allow for a broader range of inputs to work. The amount and the USD to CAD conversion is converted from a string to a Decimal value. Following these adjustments, the LLM confirms the to and from currencies, accounting for both being different as well as the same and computes the appropriate result which is then rounded. Under the assumption that the user will enter valid inputs, I did not account for the currency cleaning and currency inputs being the same but the LLM did so. Following the class, the user input entries are placed in a "main()" function that executes if under the condition "\_\_name__ == "\_\_main__"". The code proceeds to follow a similar format as mine except for a different output text for the user input initializations and print text.