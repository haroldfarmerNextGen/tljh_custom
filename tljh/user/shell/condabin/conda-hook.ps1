$Env:CONDA_EXE = "/opt/tljh/user/bin/conda"
$Env:_CE_M = ""
$Env:_CE_CONDA = ""
$Env:_CONDA_ROOT = "/opt/tljh/user"
$Env:_CONDA_EXE = "/opt/tljh/user/bin/conda"

Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1"
Add-CondaEnvironmentToPrompt