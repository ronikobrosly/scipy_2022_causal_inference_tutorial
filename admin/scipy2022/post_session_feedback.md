# SciPy 2022 Tutorial Session Feedback

## Technical / Environments

* It seemed like a handful of people struggled with installing the platform-specific dependencies
	* On Macbooks: Intel-libraries not working on M1 Apple chipsets
	* Some windows specific packages related to graphviz

* Consider using [Binder](https://mybinder.org/) or [Colab](https://colab.research.google.com/?utm_source=scs-index) to put the notebooks entirely in the cloud and so the notebooks become platform-agnostic. I don't think Docker will help here. Or perhaps ditch graphviz and causal graph plotting and just provide attendees with what the causal graph should look like, instead of having students create their own plots.


## Making Content Easier to Consume / Understand

* Some of the second exercise notebook was clearly causing confusion among participants
	* Some feedback was to add clearer markdown comment cells above each code cell better describing what the following cell was going to accomplish. Specifically for the matching pieces
* Double check PSM-adjusted result and how it varies between when doing 1:1 matching, 1:n matching, and IPW weighting. Consider just
* Add better transition between Exercise 1 and PSM explanation. Explain that now that we know the four types of causal relationships and how we're going to assume that we have a valid set of confounders going forward, and find good ways to control for them. Going to assume you're not including colliders, mediators, and unrelated predictors going forward. 
* Better explain what it means to "control" for covariates. Explain the stratification method (which we do in exercise 1), and explain how we can control for covariates in more complex model.


## Great Causal Inference Questions That I Want to Research More Thoroughly

* It's very possible the PS model can give people similar PS's even if their attributes are not exactly the same. Better explain the intuition behind generating PS scores and what they actually represent. Asked by Oliver Zeigermann (github username `DJCordhose`).

* What is the benefit of using linear models vs complex boosting models when calculating PS's. It was suggested by Gabe Okasa (github username `okasag`) that a paper did a simulation and showed that actually a linear model might be preferable: https://www.sciencedirect.com/science/article/abs/pii/S0927537120300592. Or at least that a random forest model can sometimes do worse, surprisingly.

* Gabe also provided this paper describing some of the limitations of g-computation (at least in the calculation of CATEs): https://www.pnas.org/doi/10.1073/pnas.1804597116

* Come up with a better explanation for why SHAP values aren't causal. Related to this point, Simon Brugman (github username `sbrugman`) provided a paper on a SHAP approach that is causal this point: https://proceedings.neurips.cc/paper/2020/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf. I should look into this and how it differs from standard SHAP value calculation. 
