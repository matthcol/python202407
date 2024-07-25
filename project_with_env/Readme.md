# Virtual Environment
## venv
https://docs.python.org/3/library/venv.html
### creation in a local sub-directory
python -m venv .venv

### activate environment
Change environment variable PATH:
```
.\.venv\Scripts\Activate.ps1
.venv\Scripts\activate.bat
.venv/Scripts/activate
```

## install libraries
```
pip install numpy
```
### exit environment
deactivate

## virtualenv
https://virtualenv.pypa.io/en/stable/user_guide.html

pip install virtualenv

## conda
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

```
conda env list

conda create --name env310 python=3.10

conda activate env310

conda deactivate
```

### Install libraries
```
conda install  numpy pytest mypy
```

NB: check scripts directory containing mypy and pytest scripts
