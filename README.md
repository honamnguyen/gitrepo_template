# Machine Learning for ...
## Installation guide
- Create a `conda` environment `ENV_NAME`: 
```
conda create -n ENV_NAME python==3.10
conda activate ENV_NAME
```
- Install the required packages
```
pip install -r requirements.txt
sh setup.sh ENV_NAME
```
- Attach the conda environment to jupyter
```
python -m ipykernel install --user --name=ENV_NAME
```
