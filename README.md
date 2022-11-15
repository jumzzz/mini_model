# Mini Model
Mini Model Repo

# Dependencies
Should run on `Python 3.8`

# Getting Started 

Run this following commands to install dependencies

```bash
conda create -n mini_model python=3.8
conda activate mini_model

pip install -r requirements.txt

```

Then you should do this to produce an output

```
python run_model.py sample_files/sample_input.json sample_files/sample_output.json
```

This produces the following output
```
Reading file from sample_files/sample_input.json
Making Prediction:
{
    "age": 82,
    "workclass": "Private",
    "fnlwgt": 132870,
    "education": "HS-grad",
    "marital.status": "Widowed",
    "occupation": "Exec-managerial",
    "relationship": "Not-in-family",
    "race": "White",
    "sex": "Female",
    "capital.gain": 0,
    "capital.loss": 4356,
    "hours.per.week": 18,
    "native.country": "United-States"
}
Prediction Output:
{
    "status": "success",
    "prediction_raw": 0.08823289115946195,
    "predicted_income_class": "<=50k"
}
Saving file to sample_files/sample_output.json
```