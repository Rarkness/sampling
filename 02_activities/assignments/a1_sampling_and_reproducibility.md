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
