# config.py

## Module with config and constants

## Class  `MLConfig`

 ``` 
 A class for storing basic models settings
    and other necessary constants
 ```

#### Class variables

+ `DATE_TIME_ORIGIN_FORMAT` = %Y-%m-%d %H:%M:%S: str

+ `LGBM_FEATURES_TO_APPLY` = add_synthetic_feature1, add_synthetic_feature2: list

+ `LGBM_DEFAULT_METRICS` = WMAPE: object

+ `RF_FEATURES_TO_APPLY` = add_synthetic_feature3, add_synthetic_feature2: list

# exc.py

## Import exceptions

# __init__.py

## Ml lib module with functions for models

## Variable assignment

+ `__version__` = 0.0.1: str

+ `__all__`: Tuple[str, can't parse] = 'MLConfig', 'MLModel': tuple

## exc.py

### Module with exceptions ML global

### Class  `MLException(Exception)`

 ``` 
 class for base exceptions
 ```

### Class  `ModelNotFoundException(Exception)`

 ``` 
 Exception if model not found in time execution method `load`
 ```

## ml_model.py

### Module with abstract class for ML Models

### Class  `MLModel(ABC)`

 ``` 
 Base class for ML Models
 ```

##### Class variables

+ `__model_details`: Dict

+ `__fit_params`: Dict

#### Function `MLModel.model_type`

 ``` 
 Property for naming models 
 ```

###### Decorators

+ @property

#### Function `MLModel.fit`

 ``` 
 Method fit model 
 ```

###### Decorators

+ @abstractmethod

#### Function `MLModel.predict`

 ``` 
 Method predict result by inputted value 
 ```

###### Decorators

+ @abstractmethod

###### Declared returns: `Any`

#### Function `MLModel.save`

 ``` 
 save model to storage 
 ```

###### Decorators

+ @abstractmethod

#### Function `MLModel.load`

 ``` 
 load model from storage 
 ```

###### Decorators

+ @abstractmethod

## __init__.py

### exc.py

#### Module with exceptions LGBM

#### Class  `LGBMException(Exception)`

 ``` 
 Base class for lgbm exceptions
 ```

### lgbm.py

#### Module with example class for lgbm model

#### Variable assignment

+ `default_logger` = Logger[__name__]: object

#### Class  `LGBM(MLModel)`

 ``` 
 Model LGBM for example
 ```

###### Class variables

+ `model_type` = example_lgb: str

+ `__model`: lgb.Booster

+ `__fit_params`: Dict[str, Any]

+ `__model_details`: Dict[str, Any]

##### Function `LGBM.__init__`

 ``` 
 Init lgbm adapter class 
 ```

###### **Arguments**:

 + `path_to_model`: `Optional[Union]` - empty description

 + `logger`: `Optional[Logger]` -  for logging information

 + `config`: `Optional[MLConfig]` -  settings class which will use some static constants

##### Function `LGBM._apply_features`

###### **Arguments**:

+ `base_df`: pd.DataFrame

####### Declared returns: `pd.DataFrame`

##### Function `LGBM.fit`

 ``` 
 Method to fit lgb model 
 ```

###### **Arguments**:

 + `df_x`: `pd.DataFrame` - empty description

 + `df_y`: `pd.Series` - empty description

 + `valid_sets`: `List[Tuple]` -  list of valid sets in format
[(valid1_X, valid1_Y), (valid2_X, valid2_Y), ...]

 + `feval`: `Optional[Callable]` -   custom evaluation function
if needed - (pred, pred_y) -> (name, score, higher_is_better)
check out metrics.make_feval function to turn your metric in feval func

##### Function `LGBM.predict`

###### **Arguments**:

 + `data_to_predictions`: `pd.DataFrame` - empty description

####### Declared returns: `pd.Series`

##### Function `LGBM.save`

###### **Arguments**:

+ `path_to_model`: Union[Path,str]

##### Function `LGBM.load`

###### **Arguments**:

+ `path_to_model`: Union[Path,str]

### __init__.py

#### metrics.py

##### Module for metrics
X stands for predicted values
Y stands for true values

##### Function `MAE`

 ``` 
 Mean absolute error 
 ```

###### **Arguments**:

 + `X`: `np.ndarray` - empty description

 + `Y`: `np.ndarray` - empty description

##### Function `MAPE`

 ``` 
 Mean absolute percentage error 
 ```

###### **Arguments**:

 + `X`: `np.ndarray` - empty description

 + `Y`: `np.ndarray` - empty description

##### Function `RMSE`

 ``` 
 Root mean squared error 
 ```

###### **Arguments**:

 + `X`: `np.ndarray` - empty description

 + `Y`: `np.ndarray` - empty description

##### Function `MSE`

 ``` 
 Mean squared error 
 ```

###### **Arguments**:

 + `X`: `np.ndarray` - empty description

 + `Y`: `np.ndarray` - empty description

##### Function `WMAPE`

 ``` 
 Weighted mean absolute percentage error 
 ```

###### **Arguments**:

 + `X`: `np.ndarray` - empty description

 + `Y`: `np.ndarray` - empty description

##### Function `sMAPE`

 ``` 
 Symmetric mean absolute percentage error 
 ```

###### **Arguments**:

 + `X`: `np.ndarray` - empty description

 + `Y`: `np.ndarray` - empty description

##### Function `make_feval`

 ``` 
 Function factory to transform @f to @feval required by LightGBM
:
f: function of 2 arguments (predictions, true_values) -> score
name: name of function (f.__name__ will be used if None)
higher_better: True if higher score is better, otherwise False
Returns:
feval: function of 2 arguments
(predictions, Dataset with true labels) -> (name, score, higher_better) 
 ```

###### **Arguments**:

 + `f`: `Callable` - empty description

 + `name`: `str` - empty description

 + `higher_better`: `bool` - empty description

####### Declared returns: `Callable`

###### Function `feval`

####### **Arguments**:

+ `X`: np.ndarray

+ `Y`: Dataset

#### __init__.py

### exc.py

#### Module with exceptions random forest

#### Class  `RandomForestException(Exception)`

 ``` 
 Base class for random forest exceptions
 ```

### random_forest.py

#### Module with example class for random forest model

#### Variable assignment

+ `default_logger` = Logger[__name__]: object

#### Class  `RandomForest(MLModel)`

 ``` 
 Model RandomForestClassifier for example
 ```

###### Class variables

+ `model_type` = example_random_forest: str

+ `__model`: RandomForestClassifier

+ `__fit_params`: Dict[str, Any]

+ `__model_details`: Dict[str, Any]

##### Function `RandomForest.__init__`

 ``` 
 Init RandomForestClassifier adapter class 
 ```

###### **Arguments**:

 + `path_to_model`: `Optional[Union]` - empty description

 + `logger`: `Optional[Logger]` -  for logging information

 + `config`: `Optional[MLConfig]` -  settings class which will use some static constants

##### Function `RandomForest._apply_features`

###### **Arguments**:

+ `base_df`: pd.DataFrame

####### Declared returns: `pd.DataFrame`

##### Function `RandomForest.fit`

 ``` 
 Method to fit RandomForestClassifier model 
 ```

###### **Arguments**:

 + `df_x`: `pd.DataFrame` - empty description

 + `df_y`: `pd.Series` - empty description

##### Function `RandomForest.predict`

###### **Arguments**:

 + `data_to_predictions`: `pd.DataFrame` - empty description

####### Declared returns: `pd.Series`

##### Function `RandomForest.save`

###### **Arguments**:

+ `path_to_model`: Union[Path,str]

##### Function `RandomForest.load`

###### **Arguments**:

+ `path_to_model`: Union[Path,str]

### __init__.py

## __init__.py

## features.py

### module with features necessary for work

### Function `add_synthetic_feature1`

 ``` 
 The function adds a feature to df
one function - one feature
is necessary for a convenient combination of them when researching 
 ```

#### **Arguments**:

 + `df`: `pd.DataFrame` -  df to add a feature

#### **Returns**:

```console

 updated df

```

##### Declared returns: `pd.DataFrame`

### Function `add_synthetic_feature2`

 ``` 
 similar to earlier 
 ```

#### **Arguments**:

 + `df`: `pd.DataFrame` - empty description

##### Declared returns: `pd.DataFrame`

### Function `add_synthetic_feature3`

 ``` 
 similar to earlier 
 ```

#### **Arguments**:

 + `df`: `pd.DataFrame` - empty description

##### Declared returns: `pd.DataFrame`

## pre_processing.py

### Module contains functions for data preprocessing before training

### Function `change_raw_data`

 ``` 
 Function to modify or extend raw data 
 ```

#### **Arguments**:

 + `df`: `pd.DataFrame` -  data to modify

#### **Returns**:

```console

 changed pd.DataFrame df

```

##### Declared returns: `pd.DataFrame`

## __init__.py

### import preprocessing functions

## validator.py

### module with validation functions

### Function `get_object_config`

 ``` 
 Function to get config for work models 
 ```

#### **Arguments**:

 + `obj`: `Optional[Union]` - object to check

#### **Returns**:

```console

 default  if obj is none or incorrect type

```

##### Declared returns: `MLConfig`

## __init__.py

### Import utils functions and classes

### Variable assignment

+ `__all__`: Tuple[str, can't parse] = 'get_object_config': tuple