GPU hours (1,000). One pass over the model is 24 checkpoints across 8 physics
tasks, about 600 answers. We are measuring how much results change between runs,
so that pass gets repeated under different settings and question wordings. That
comes to several thousand answers, or a few hundred GPU hours once failed runs
are counted. The rest covers hosting the model as a service other researchers can
query, where a GPU stays loaded and waiting rather than working in bursts.

CPU core-hours (4,000). The training text runs to billions of words and has to be
searched for anything written after the model's cutoff, since a model that has
read the answer is not rediscovering it. Comparing thousands of answers across
runs and scoring them adds more. This is searching and comparing, not heavy
computation, so it needs processors rather than GPUs.

Storage (500 GB). Checkpoints are about 160 GB, the training corpus is over 100
GB while being audited, and we keep every answer produced, including failures. A
reliability figure based only on runs that worked is not a reliability figure.

This is a deliberately small first request, under a third of our credits. We will
ask for more once the service is running and we can measure real usage.
