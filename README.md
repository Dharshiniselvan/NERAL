# NERAL
Mini AI for agronomy-based crop recommendation.
A beginner-friendly crop recommendation tool.

## Features
  - It takes the following inputs from the user:
  - Mode of farming (rooftop, open, closed, hill, barren)
  - Water level (low, medium, high)
  - Soil type (clay, sandy, loamy, or ignore)
  - Manure type (organic, chemical, or ignore)

  - It provides the following outputs:
  - Recommended crops
  - Suggestion if the combination is not suitable

## How it Works

The system uses the following mode-based decision-making system:

- Mode is given the highest priority
- According to the water, soil, and manure conditions, a suitable crop is selected
- If no valid combination exists, a suggestion is made

## Example

Input:
Mode - Open  
Water - High  
Soil - Clay  

Output:
Rice

## Technology Used

- Python
- Conditional statements if-elif

## Purpose

It is a mini AI to help people choose the right crop based on the conditions they have.
