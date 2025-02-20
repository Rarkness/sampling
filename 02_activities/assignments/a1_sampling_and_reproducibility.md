# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Rarkness (Rick)

```
Sampling is happening for the infection stage. Everyone at an event has a 10% chance of getting infected. Then there’s tracing; the infected people have a 20% chance of being traced. If two or more cases get traced from the same event, they trace everyone from that event and find all the infections. The sampling frame is all 1000 people, 200 at weddings, 800 at brunches. Since weddings are easier to trace, they end up overrepresented in the data, even if brunches are spreading more. 

Yes, the code appear to reproduce the graphs from the original blog post.

If you kept running the script over and over, the graphs would look a bit different each time because it’s random who gets infected and who gets traced. And since it’s only running 100 times instead of 1000, the results change more. You’ll still see weddings, but the shape of the graph changes. It’s not consistent unless you set a random seed, so I added np.random.seed. Now, every time you run it, you’ll get the same graph.
```







YOU WROTE:
Please address the following changes/additions:

Please Describe in words the:

    sampling procedure
    referencing the functions used
    any underlying distributions involved, and how these relate to the procedure outlined in the blog post

If you take a closer look you should notice differences between your code and the original blog post. Please comment on this

MY ANSWER TO THIS:

So, the way the sampling works in the code is pretty straightforward. First, each person has a 10% chance of getting infected, then if they’re infected, there’s a 20% chance they get traced. If 2 or more traced cases are from the same event, everyone at that event gets traced. It’s mostly random yes/no checks, except for that last part, which is more like a rule kicking in. This kind of lines up with the blog’s point about weddings being easier to trace, but there’s a big difference the code treats all weddings and all brunches like two big groups, instead of lots of smaller, separate events like the blog was talking about. So, it kind of misses the point about small brunches being harder to trace, and it probably makes weddings look even more important than they actually are.





Question 1: Examine the code. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post."
Sampling is happening for the infection stage. Everyone at an event has a 10% chance of getting infected. Then there’s tracing; the infected people have a 20% chance of being traced. If two or more cases get traced from the same event, they trace everyone from that event and find all the infections. The sampling frame is all 1000 people, 200 at weddings, 800 at brunches. Since weddings are easier to trace, they end up overrepresented in the data, even if brunches are spreading more. That’s the bias the model is showing.

Question 2: Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?
YES



Question 3:
Now provide the entire code and modify the number of repetitions in the simulation to 100 (from the original 1000). 
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Constants representing the parameters of the model
ATTACK_RATE = 0.10
TRACE_SUCCESS = 0.20
SECONDARY_TRACE_THRESHOLD = 2


def simulate_event(m):
    # Create DataFrame for people at events with initial infection and traced status
    events = ['wedding'] * 200 + ['brunch'] * 800
    ppl = pd.DataFrame({
        'event': events,
        'infected': False,
        'traced': np.nan
    })

    # Infect individuals with probability ATTACK_RATE
    ppl['infected'] = np.random.rand(len(ppl)) < ATTACK_RATE

    # Primary contact tracing with success probability TRACE_SUCCESS
    traced_primary = np.random.rand(len(ppl)) < TRACE_SUCCESS
    ppl.loc[ppl['infected'], 'traced'] = traced_primary[ppl['infected']].astype(bool)

    # Secondary contact tracing when at least SECONDARY_TRACE_THRESHOLD traced in an event
    traced_events = ppl.loc[ppl['traced'], 'event']
    for event in traced_events.unique():
        if traced_events.value_counts().get(event, 0) >= SECONDARY_TRACE_THRESHOLD:
            ppl.loc[ppl['event'] == event, 'traced'] = ppl.loc[ppl['event'] == event, 'infected']

    # Calculate proportion of traced cases from weddings
    total_infected = ppl['infected'].sum()
    traced_cases = ppl.loc[ppl['traced'] == True, 'event'].value_counts()
    traced_wedding_cases = traced_cases.get('wedding', 0)

    prop_infected_wedding = ppl.loc[ppl['infected'] & (ppl['event'] == 'wedding')].shape[0] / total_infected
    prop_traced_wedding = traced_wedding_cases / traced_cases.sum()

    return prop_infected_wedding, prop_traced_wedding


# Run simulation over 100 repetitions
results = [simulate_event(i) for i in range(100)]

results_df = pd.DataFrame(results, columns=['prop_infected_wedding', 'prop_traced_wedding'])

# Plot results
sns.histplot(results_df['prop_traced_wedding'], kde=True)
plt.title('Proportion of Traced Cases from Weddings')
plt.xlabel('Proportion')
plt.ylabel('Frequency')
plt.show()




Question 4:

Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

If you ran the script over and over, the graphs would look a little different each time because it’s random who gets infected and who gets traced. Since it’s only running 100 times instead of 1000, the results change even more. You’ll still see weddings showing up more, but the graph’s shape changes. It’s not perfectly reproducible unless you set a random seed, but the main point stays the same. I added np.random.seed to make it random. When you run it, you’ll get the same output.

Question 5:
Alter the code so that it is reproducible. 
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Set random seed for reproducibility
np.random.seed(42)

# Constants representing the parameters of the model
ATTACK_RATE = 0.10
TRACE_SUCCESS = 0.20
SECONDARY_TRACE_THRESHOLD = 2


def simulate_event(m):
    # Create DataFrame for people at events with initial infection and traced status
    events = ['wedding'] * 200 + ['brunch'] * 800
    ppl = pd.DataFrame({
        'event': events,
        'infected': False,
        'traced': np.nan
    })

    # Infect individuals with probability ATTACK_RATE
    ppl['infected'] = np.random.rand(len(ppl)) < ATTACK_RATE

    # Primary contact tracing with success probability TRACE_SUCCESS
    traced_primary = np.random.rand(len(ppl)) < TRACE_SUCCESS
    ppl.loc[ppl['infected'], 'traced'] = traced_primary[ppl['infected']].astype(bool)

    # Secondary contact tracing when at least SECONDARY_TRACE_THRESHOLD traced in an event
    traced_events = ppl.loc[ppl['traced'], 'event']
    for event in traced_events.unique():
        if traced_events.value_counts().get(event, 0) >= SECONDARY_TRACE_THRESHOLD:
            ppl.loc[ppl['event'] == event, 'traced'] = ppl.loc[ppl['event'] == event, 'infected']

    # Calculate proportion of traced cases from weddings
    total_infected = ppl['infected'].sum()
    traced_cases = ppl.loc[ppl['traced'] == True, 'event'].value_counts()
    traced_wedding_cases = traced_cases.get('wedding', 0)

    prop_infected_wedding = ppl.loc[ppl['infected'] & (ppl['event'] == 'wedding')].shape[0] / total_infected
    prop_traced_wedding = traced_wedding_cases / traced_cases.sum()

    return prop_infected_wedding, prop_traced_wedding


# Run simulation over 100 repetitions
results = [simulate_event(i) for i in range(100)]

results_df = pd.DataFrame(results, columns=['prop_infected_wedding', 'prop_traced_wedding'])

# Plot results
sns.histplot(results_df['prop_traced_wedding'], kde=True)
plt.title('Proportion of Traced Cases from Weddings')
plt.xlabel('Proportion')
plt.ylabel('Frequency')
plt.show()



























## Criteria

|Criteria|Complete|Incomplete|
|--------|----|----|
|Altercation of the code|The code changes made, made it reproducible.|The code is still not reproducible.|
|Description of changes|The author explained the reasonings for the changes made well.|The author did not explain the reasonings for the changes made well.|

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 16/02/2025`
* The branch name for your repo should be: `assignment-1`
* What to submit for this assignment:
    * This markdown file (a1_sampling_and_reproducibility.md) should be populated.
    * The `whitby_covid_tracing.py` should be changed.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/sampling/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-1`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via the help channel in Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
