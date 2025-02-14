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
        'traced': False
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
