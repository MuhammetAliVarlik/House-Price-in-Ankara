from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import GridSearchCV, ShuffleSplit
from sklearn.tree import DecisionTreeRegressor
import pandas as pd


# Function to search which model and hyper parameters are best for the dataset
class GridSearch:
    def __init__(self):
        pass

    @staticmethod
    def grid_search(X, y):
        algorithms = {
            'linear_regression': {
                'model': LinearRegression(),
                'params': {
                    'normalize': [True, False]
                }
            },
            'lasso': {
                'model': Lasso(),
                'params': {
                    'alpha': [1, 2],
                    'selection': ['random', 'cyclic']
                }
            },
            'decision_tree': {
                'model': DecisionTreeRegressor(),
                'params': {
                    'criterion': ['mse', 'friedman_mse'],
                    'splitter': ['best', 'random']
                }
            }
        }
        scores = []
        cv = ShuffleSplit(n_splits=5, test_size=0.25, random_state=15)
        for algo_name, config in algorithms.items():
            gs = GridSearchCV(config['model'], config['params'], cv=cv, return_train_score=False)
            gs.fit(X, y)
            scores.append({
                'model': algo_name,
                'best_score': gs.best_score_,
                'best_params': gs.best_params_
            })

        return pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])
