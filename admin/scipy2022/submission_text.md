# SciPy 2022 Tutorial Submission: introduction to causal modeling (intermediate skill level)

Author:

Roni Kobrosly, PhD 

* https://www.kobrosly.net
* https://www.linkedin.com/in/ronikobrosly/
* https://github.com/ronikobrosly


## Brief Note to SciPy Committee

Thanks for considering this tutorial for SciPy 2022. It is basically 98% complete with both attendee and teacher versions of Jupyter notebooks for exercises, a complete deck in PDF format, datasets included, and instructions on how to set up one's local machine to go through the exercises. If accepted, between now and the final submission date I would likely make slight tweaks to the flow of the presentation along with any suggestions you may provide.


## Presenter Bio

I am a former epidemiology researcher who has spent approximately a decade employing causal modeling and inference. The bulk of my academic career was spent conducting data analyses to estimate the population-level effects of harmful environment exposures, when traditional randomized experiments were infeasible or unethical. During this time, I taught a couple undergraduate epidemiology courses, once of which involved a sizable introduction to causal thinking. I've also presented many one-off departmental presentations and at a few epidemiology conferences on causal inference in both cases.

Since leaving the academic world, I've been loving my second life in the tech industry as a data scientist, ML engineer, and more recently as the Head of Data Science at a medium-sized health tech company based in Washington DC. I love mentoring junior data folks and explaining the magic of data analysis and modeling to non-technical audience.

I also am a member of the open-source community, being the author and maintainer of the `causal-curve` python package. This package provides a set of tools for estimating the causal impact of continuous/non-binary treatments (e.g. estimating the causal impact of a neighborhood's income inequality on local crime, or understanding the causal effect of increasing a product's price on conversion rates).


## Short Description

This tutorial session is intended to give attendees a gentle introduction to applying causal thinking and causal inference to data using python. Causal data analysis is very common in many academic domains (e.g. in social psychology, epidemiology, macroeconomics, public policy research, sociology, and more) as well as in industry (all of the largest Silicon Valley tech companies employ teams of scientists who answer business questions purely with causal inference methods). 

The tutorial will involve a combination of presentations with open Q&A and hands-on exercises contained in Jupyter notebooks. This session will cover the difference between correlation and causation, the pitfalls of conducting an analysis using observational data, how causal inference can help get around these pitfalls, and examples of common, modern modeling approaches used to conduct causal inference (propensity score matching, estimating causal curves, g-computation, and double ML). After the tutorial, the attendees should have a good foundational understanding of causality and the ability to confidently explore the topic on their own. Causal inference can be a very theory-heavy topic, making it impenetrable to novices. In this tutorial, we'll aim to take a more practical perspective on causal inference, while still occasionally touching on the theory. 

Tutorial participants are not expected to be familiar with causal inference before attending, but we hope they have an earnest curiosity to learn about it! To get the most out of the session, the participants ought to have experience working with the common python data stack: `matplotlib`, `numpy`, `pandas`, and `scikit-learn`. Attendees should have some experience conducting classic machine learning modeling using the `scikit-learn` API, although having advanced machine learning expertise is absolutely not a prerequisite. A very basic understanding of statistics would be helpful (e.g. understanding what a mean is, what confidence intervals represent). 


## Long Description with Outline


* Housekeeping (__10 min block__)
	* Check whether most people were able to load tutorials 
	* Identify if there are groups experiencing same issue. Encourage neighbors to help anyone struggling.
	* Poll audience for their level of comfort with topic so I can fine-tune pacing and descriptions to their comfort level.
	* Introduce myself
	* Introduce format, "feel free to interrupt and ask questions anytime"
	* Outline goals of talk. By the end you should be able to ...
		* Understand the pitfalls of observational data analysis
		* Understand the various types of causal relationships
		* Describe the hierarchy of statistical analyses, causal inference, and experiments
		* Start conducting preliminary causal analyses on your own data
		* Ability to confidently explore the topic on your own (now that you have a solid foundational understanding of causal thinking)


* Introducing causal thinking: (__20 min block__)
	* Introducing the concept of "counterfactuals" using a COVID-19 example
	* We can't directly see counterfactuals but experiments are the best tool we have for estimating effects
	* Unfortunately though, randomized controlled trials AKA experiments AKA A/B tests can't always save us, here's why...
	* Describing the differences between correlative statistics/associations, vs causal inference, vs experiments
	* Describing the distinction between predictive and inferential ML modeling
	* Introducing causal graphs
		* What the nodes and edges represent in a causal graph
		
		
* LARGE GROUP EXERCISE  (__5 min__)
	* Drawing out car insurance causal graph as a large group. Attendees will call out their answers from their seats. 
		

* More on causal structures (__20 min block__) 
	* Introducing confounding: 
		* Walking through canonical confounding example: the classic association of ice cream sales and violent crime
		* Positive vs negative confounding
		* Determining confounding direction
	* Introducing colliders
	* Introducing mediators
	* Introducing unrelated predictors in causal graphs
	* How causal thinking helps visualizing and thinking through fairness/bias issues with modeling
	* IF WE'RE AHEAD OF TIME HERE: will discuss structure learning for causal graphs...
	
	
* SOLO OR SMALL GROUP EXERCISES: NOTEBOOK 1 (__20 min__)
	* In this notebook attendees will explore how confounders, colliders, mediators, and unrelated predictors play out in simulated data. 
	* They'll learn what happens if you control for each of these in real datasets.
	
	
* BREAK (__20 min__)
	
	
* Introduction to causal inference methods: (__10 min block__) 
	* A few simple suggestions for a causal inference workflow
	* The core assumptions of causal inference
		* Temporality. Causes always occur before effects: The treatment variable needs to occur before measured outcome. Similarly, All confounders occur before treatment. 
		* Positivity. For each level of each covariate in your data, there needs to be some variability of the treatment and outcome variables.
		* The treatment status of a given individual does not affect the potential outcomes of any other individuals.
		* All major confounding variables are included in your data. This is a tough one, but necessary unless you want a biased estimate of the treatment effect. 


* LARGE GROUP EXERCISE (__10 min__)
	* I'll share a few sloppy examples of causal inference analyses, and the audience will shout out which of the above causal assumptions each is violating.


* How the classic interpretability-to-predictive-power tradeoff that is so well-known in the machine learning field is very much present in causal inference. How the PSM method is very interpretable but less powerful, but Double ML is least interpretable but provides powerful estimates of causal impact: (__10 min block__) 
* Returning to the concept of counterfactuals to motivate an explanation for the common causal inference metrics:
	* Average Treatment Effect (ATE)
	* Average Treatment Effect Among Treated (ATT)
	* Average Treatment Effect Among Untreated (ATU)
* A warning that traditional machine learning variable importance methods don't tell you anything about causality.

	
* `Propensity Score Matching (PSM)` for binary treatments: (__15 min block__) 
	* Walking through the standard, caliper-matching approach to PSM, step-by-step, with a small table on the screen.
		* How to calculate propensity scores with standard machine learning models
		* How to calculate calipers and match treated to "controls"
		* Calculating a treatment effect from matched treatment and "control" groups. 
	* Briefly describing alternative approaches to caliper-matching (stratification, inverse weighting, etc.)
	* Estimating confidence intervals via bootstrapping
	* Describing the benefits of PSM (incredibly interpretable, easy for readers or stakeholders to understand)
		
	
* SOLO OR SMALL GROUP EXERCISES: NOTEBOOK 2 (__20 min__)
	* In this notebook attendees will walk step by step through a custom implementation of PSM, using the canonical LaLonde dataset. Attendees will attempt to determine the true, causal impact of a job training program on wages years later. Attendees will compare the raw treatment effect (which is biased) against the PSM-estimated treatment effect. The notebook will also show readers how to estimate confidence intervals via bootstrapping. 
		

* Estimating `causal curves` for continuous treatments: (__15 min block__) 
	* Motivating the problem of handling continuous treatments; not all "treatments" are binary, sometimes they can be prices in USD, temperatures, income inequality measures, blood lead levels, etc.
	* How standard, bivariate plots of treatment and effect can fail us, and how to conceptualize counterfactuals in the context of continuous treatments.
	* How to interpret the causal curve in words
	* A simple overview of how to estimate the causal curve using generalized propensity scores (GPS)


* SOLO OR SMALL GROUP EXERCISES: NOTEBOOK 3 (__20 min__)
	* Attendees will explore the public National Health and Nutrition Examination Survey (NHANES) III dataset. They will learn how to use the causal-curve API and the GPS method to estimate the treatment effect of continuous treatments and will get practice in interpreting these results. 
		

* Final block, more advanced methods (__15 min block__) 
	* `G-Computation` for binary treatments: 
		* A brief explanation the algorithm, step-by-step with a simple table in the deck
		* Explaining the advantages and costs of g-computation over PSM	
	* `Double ML` for binary treatments
		* A brief explanation the algorithm
		* Explaining the advantages and costs of Double ML over the previous approaches
	* Closing thoughts
		* How to troubleshoot common issues in causal inference analyses
		* Remember, running causal inference and experiments can be incredibly humbling. A great many research ideas don't pan out, and many many business ideas that seem clever and so intuitive don't work at all.
		
	
* SOLO OR SMALL GROUP EXERCISES: NOTEBOOK 4 or NOTEBOOK 5 (__20 min__)
	* At this step attendees will get to choose whether they would like to do a hands-on exercise with g-computation or with double ML. Naturally they get to keep both exercises and look at them later.
		

__Total time required: 230 minutes__


## Materials and Setup Instructions

The entire set of materials needed for this tutorial are available via the following public GitHub repository: <git@github.com:ronikobrosly/causal_inference_intro.git>. Instructions for setting up machines using both standard python virtualenv environments and Anaconda environments will be provided. Both "student" and "teacher" Jupyter notebooks are available in the "notebooks" folder of the repo. Presentations that correspond to the lesson blocks of the outline are available in the "slides" folder. These decks are available in PDF format so they will be accessible to all.

