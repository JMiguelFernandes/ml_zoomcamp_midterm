# Predicting sales at the BigMart supermarket chain

Hello everyone! I'm Joao, and this is my midterm project for the Machine Learning Zoomcamp :)

For this project, I'll be using the following dataset:
- https://www.kaggle.com/shivan118/big-mart-sales-prediction-datasets

This dataset contains a number of features about products sold in a supermarket chain, including the number of items sold for each product at different BigMart stores. You can find a detailed description of what each column means at the link above. 

My goal will be **to predict the number of items sold for new products at these stores**. This can be helpful to the management of BigMart when it comes to deciding which products to invest in, how much shelf space to allocate to each product, or how much to charge for each product at each location, for example.


Data cleaning, EDA and model selection can be found in the notebook called bigmart.ipynb.
Training of the final model is done in the model_train.py script, and it is deployed as a web service using Flask in the sales_prediction.py script. The sales_prediction.py script was deployed in a Docker container on Heroku; see below for more info on this.


## Notes on how to run the scripts/notebooks 


First of all, clone the repo by running the following command:

```
git clone https://github.com/JMiguelFernandes/ml_zoomcamp_midterm.git
```

In order to run these notebooks/scripts, you will need to have python installed, as well as jupyter notebook and a few extra packages. These are detailed in the Pipfile/Pipfile.lock files. To install all these packages, you can use pipenv to create a dedicated environment for this project. To do so, make sure you have pipenv installed; if not, just run the following: 

```
pip install pipenv
```

Then, open a Git Bash window in the folder containing the Pipfile/Pipfile.lock files and run the following:

```
pipenv install
```

And there you go, all packages should be installed in your new virtual environment! To start using the environment, you can run the following:

```
pipenv shell
```

And then run the scripts as you normally would.


# Predicting sales of a new product - How to submit a request to the web service

The sales_prediction.py script was deployed in a Docker container on Heroku. You can check the Dockerfile for details on how the Docker container was built.

Deployment to Heroku was done with the help of [this guide](https://github.com/nindate/ml-zoomcamp-exercises/blob/main/how-to-use-heroku.md). Many thanks to fellow zoomcamper Ninad Date for putting it together :D

To predict the number of items sold for a new product, you need to have python installed, along with the requests package and ideally jupyter notebook (this one is optional, you can also run it directly from your command line).
To submit a request for a prediction, run the following in a jupyter notebook:

```
import requests
url = "https://mlzoomcamp-midterm-sales-pred.herokuapp.com/sales_prediction"
product = {'ProductType': 'Fruits and Vegetables',
           'OutletID': 'OUT027',
           'ProductVisibility': 0.042354152,
           'MRP': 227.272}
response = requests.post(url, json=product)
response.json()
```

And that will return the sales prediction for your product! :D

The product above is just an example; you can submit different products, but the structure of the dictionary must remain the same. ProductType and OutletID can be one of the categories below. ProductVisibility is a number between 0 and 1, reflecting the percent of total shelf space that is occupied by your product in the store. MRP (list price) is a positive float.

ProductType:


- Breads
- Fruits and Vegetables
- Dairy
- Baking Goods
- Soft Drinks
- Others
- Canned
- Snack Foods
- Meat
- Frozen Foods
- Starchy Foods
- Health and Hygiene
- Seafood
- Hard Drinks
- Household
- Breakfast
 
OutletID: 


- OUT046
- OUT045
- OUT018
- OUT017
- OUT010
- OUT027
- OUT013
- OUT035
- OUT049
- OUT019
