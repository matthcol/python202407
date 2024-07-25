## create and activate virtual env
python -m venv .venv
.\.venv\Scripts\Activate.ps1

## install local wheel
pip install  ..\project_with_env\dist\gauss_app-2024.7.0-py3-none-any.whl

