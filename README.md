# intro-to-causal-inference

A introduction to causal inference using common tools from the python data stack


# Table of Contents

- [Getting Started](#getting-started)
  - [Install graphviz](#install-graphviz)
  - [Clone the repository](#clone-the-repository)
  - [Determine your installation preference](#determine-your-installation-preference)
  - [Install a new IPython kernelspec](#install-a-new-ipython-kernelspec)
  - [Start up jupyter lab and open a notebook](#start-up-jupyter-lab-and-open-a-notebook)
- [Acknowledgements](#acknowledgements)
- [Feedback](#feedback)


## Getting Started

### Install graphviz

You'll need `graphviz` for our first exercise notebook, to visualize causal graphs.

- Linux:
  - Depending on your distro, [here are the possible commands](https://graphviz.org/download/#linux)
- MacOS:
  - You can easily install it via [homebrew](https://docs.brew.sh/Installation): `brew install graphviz`
- Windows:
  - The graphviz.org website [has convenient installers for you](https://graphviz.org/download/#windows)


### Clone the repository

In your terminal, use `git` to clone the repo to your machine.

```bash
git clone git@github.com:ronikobrosly/causal_inference_intro.git
```

If you are less comfortable with `git`, there is an easy alternative: [You can simply download a zip file of it here :)](https://github.com/ronikobrosly/causal_inference_intro/archive/refs/heads/main.zip)


### Determine your installation preference

Now that you've installed `graphviz` and cloned the repo locally, you'll need to ensure you have a working python environment set up. There are two ways you can go about doing this, shown as Options 1 and 2 below.

**Note: if you already have installed and are using Anaconda python on your laptop please use Option 2. In addition, you're going to need python version `3.6+` for this tutorial and this guide assumes you already have it installed.**


#### Option 1: installing via `pip install` in a `virtualenv`

Create a new virtual environment for this tutorial. You can do this a number of ways but one of the simpler involves the use of the `virtualenv` python package. If you are a Windows or Linux user, please [use this guide](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/). If you are a MacOS user [you can follow this guide](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html).

Name your environment `causal_modeling`

"Activate" this environment (see the above guide) and then run the following command in the root folder of this repo:
`pip install -r requirement.txt`

This will install all the necessary packages for the tutorial.

As an optional step, you can try to run the `check_environment.py` file (in the root folder of the repo)
while within your virtual environment. You can do so by running `python check_environment.py` in your terminal. It will alert you if you're missing any required python packages.


#### Option 2: installing via Anaconda python and the `conda` package manager

If you do not already have the [Anaconda distribution](https://www.anaconda.com/download/) of Python 3,
please install it.

You can then use the `conda` tool in your terminal to install the necessary packages:

`conda env create -f conda_env.yml`

"Activate" the new environment via:

`conda activate causal_modeling`

As an optional step, you can try to run the `check_environment.py` file (in the root folder of the repo)
while within your virtual environment. You can do so by running `python check_environment.py` in your terminal. It will alert you if you're missing any required python packages.


### Install a new IPython kernelspec

Once the above is complete, you'll need to run the following commands:

`python -m ipykernel install --user --name causal_modeling --display-name "Python (causal_modeling)"`


### Start up jupyter lab and open a notebook

In the terminal, execute `jupyter lab`.

Navigate to the `notebooks` directory and open your notebook of choice. You will probably be asked which environment you would like to use with the notebook. Select the `Python (causal_modeling)` environment you created in the step above. 


## Acknowledgements

I would like to like to acknowledgement the following individuals for creating public causal inference
materials that were useful in the creation of this tutorial:

- Konstantinos Papadopoulos @ [Analytics Mayhem](https://analyticsmayhem.com/)
- Ramin Ghelichi @ [Wayfair](https://www.aboutwayfair.com/tech-innovation/the-importance-of-covariates-in-causal-inference)

## Feedback

I love would to hear your feedback on these tutorial materials!
Please send your comments to <roni.kobrosly@gmail.com>.
