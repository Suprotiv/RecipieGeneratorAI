
# Infectious Spread Tracking Program

This initiative assesses the dissemination of infections based on the interactions among people. It monitors which individuals come into contact with initially infected individuals and tracks how the illness propagates through these interactions over time.

## Functions
1. process_interaction_records(records_data) :

This function accepts raw interaction information and transforms it into a structured list of engagements for future use.

Input: 

A collection of pairs indicating interactions between two people at a specific moment: (individual1, individual2, timestamp).

Output:

A collection of interaction pairs organized for application in the infection tracking algorithm.

Purpose:
To convert unrefined interaction data into a log format that the system can readily utilize for tracing contacts and infections.

2. identify_contacts(individual, timestamp, records_data, infection_period) :

This function detects all persons with whom a specified individual had contact after they became infectious.

Input:

individual: The person whose contacts we are tracing.
timestamp: The time from which interactions should be analyzed.

records_data: The structured interaction log.

infection_period: The timeframe in which the individual can transmit the infection.

Output:

A collection of pairs representing individuals that the person has engaged with after the specified time and within the infection period.

Purpose:
To obtain all contacts that transpired during or after the designated infection period for an infected individual.

3. track_infection(initially_infected, records_data, infection_period) :

This is the primary function that monitors the propagation of infection from initially infected individuals through their interactions.

Input:

initially_infected: A collection of individuals who were initially infected.

records_data: The interaction logs of all individuals.

infection_period: The duration (in hours) during which an 
infected individual can transmit the infection.

Output:
A collection of all individuals who became infected.

Step-by-Step Process:


Transform the initially_infected collection into a set termed infected to eliminate duplicates and facilitate rapid lookups.
Process the interaction log using process_interaction_records(records_data).

For each individual in the initially_infected collection:

Add them to the infected set.
Utilize a DFS-like strategy with a stack, beginning with the initially infected individual.

For each person in the stack, locate their contacts using the identify_contacts function.

If a contact is not already infected, mark them as infected and add them to the stack for further contact tracing.

The infection spread continues until all potential contacts within the infection period have been traced.


## Testing

Test Cases: Both black box and white box testing methodologies are employed to address various scenarios effectively:

No interactions

Simple interaction within the infection period

Interactions outside the infection period

Chain of interactions (indirect transmission)

Multiple initially infected individuals

Circular interactions

## Time Complexity

process_interaction_records(records_data) function:

Iterates through all entries in records_data, leading to a time complexity of O(n), where n is the number of interactions.

identify_contacts(individual, timestamp, records_data, infection_period) function:

For each individual, it reviews all log entries, resulting in a time complexity of O(n) for each invocation.


track_infection(initially_infected, records_data, infection_period) function:

Employs DFS to trace contacts. In the worst scenario, DFS will examine the entire log for each individual in the stack. Thus, the time complexity is O(n^2) in the most extreme case.

#### Overall Time Complexity:

O(n^2) in the most extreme case.

## Space Complexity

process_interaction_records(records_data) function:

Requires a collection of size n to retain parsed log data.
Space complexity: O(n).

identify_contacts(individual, timestamp, records_data, infection_period) function:

Can produce a collection of contacts of size n in the most extreme instance.
Space complexity: O(n) per call.

track_infection(initially_infected, records_data, infection_period) function:

Maintains an infected set and DFS stack, each of which can expand up to m (where m is the number of distinct individuals involved).
Space complexity: O(m).

#### Overall Space Complexity:

O(n + m), where n is the number of interactions and m is the number of distinct individuals involved.

Summary
Time complexity: O(n^2)
Space complexity: O(n + m)
This program effectively tracks infection dissemination, ensuring scalability for extensive datasets of interactions while managing various edge cases and infection chains.
