## This repository is evidence for new feature that allows python adk to configure different project and location for vertex models

The dist wheel comes out of the branch https://github.com/avidela/adk-python/tree/feat/add-project-location-config-to-vertex-models

## How to verify test : 
```bash
#create environment
uv venv
#activate 
source .venv/bin/activate
#install depdendencies including wheel
uv sync
#run adk web
uv run adk web