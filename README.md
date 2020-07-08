# comedy_show_recommender

comedy_show_recommender is a machine learning recommender for recommending personalized comedy shows in Nigeria based on ratings.

## Cloning the repository

In your git terminal use git command to clone:

```bash
git clone https://github.com/ezekielolugbami/comedy_show_recommender.git
```

## Setup environment

Open a new terminal in whatever editor you are using and create a new environment. Remember to use the same Python version as in the requirement file.

```python
conda create -n "comedy-recommender" python==3.7
```

Then proceed to activate the environment using:

```python
conda activate comedy-recommender
```

### Installing requirements

Pip install the requirements file, contained in the root folder of the cloned project:

```python
pip install -r requirements.txt
```

Navigate to the base_model.py folder to run the script:

```bash
cd src/scripts/modeling/
```

Finally, run the command:

```python
python base_model.py
```
