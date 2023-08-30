# Tip-Calculator
# 💡How the Code Works

This Python code is designed to calculate the fair split of a restaurant bill, including a tip, among a specified number of people. Here's a breakdown of how it works:

1. **User Input**: The code starts by asking the user for three pieces of information:
   - The total bill amount (`bill`).
   - The desired tip percentage (`tip`), which can be 10%, 12%, or 15%.
   - The number of people to split the bill between (`ppl`).

2. **Data Conversion**: The user inputs (`bill`, `tip`, and `ppl`) are initially stored as strings. To perform mathematical operations, these values are converted to appropriate data types:
   - `Bill`: The bill amount is converted to a floating-point number.
   - `Tip`: The tip percentage is converted to an integer.
   - `Ppl`: The number of people is converted to an integer.

3. **Tip Calculation**: The code calculates the tip amount by multiplying the `Bill` by the tip percentage divided by 100. This step computes how much tip needs to be added to the total bill.

4. **Total Bill Calculation**: The total bill amount after adding the tip is determined by adding the tip amount to the original bill. This represents the total cost to be split among the group.

5. **Fair Split Calculation**: To find out how much each person should pay, the total bill is divided by the number of people (`Ppl`). This calculation ensures an equal split.

6. **Rounding**: The split bill amount is rounded to two decimal places using Python's `round` function. It's then formatted as a string with two decimal places to ensure a consistent format for displaying the result.

7. **Output**: The final split bill amount per person is displayed to the user, rounded to two decimal places. This amount represents how much each person should contribute to cover the bill and tip evenly.

# 🌟 How It Can Be Used in Daily Life

This code can be a handy tool in daily life for anyone who dines out with friends or family and wants to ensure a fair and convenient way to split the bill. Here are some scenarios where this code can be beneficial:

1. **Group Dinners**: When dining with a group of people, it's common for one person to pay the bill initially. This code can help calculate how much each person owes to reimburse the payer accurately.

2. **Restaurant Visits**: Whether you're eating at a restaurant, café, or ordering takeout, you can quickly determine each person's share of the bill, taking into account the tip.

3. **Event Planning**: When organizing events or parties where expenses are shared, this code can help you distribute costs evenly among participants.

4. **Budgeting**: It's useful for individuals who want to budget and track their expenses accurately, especially when dining out with different groups of people.

5. **Learning Python**: For those learning Python programming, this code serves as an example of simple input, calculation, and output operations.

By using this code, you can avoid the hassle of manual bill splitting and ensure that everyone pays their fair share, making dining out with friends or family a more enjoyable experience.
