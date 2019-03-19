# tool-mxd-imageperzoom

This tool creates jpeg exports from a map document on different scale levels and locations,
in order to easily create map presentations to show the implemented styling.

## Dependencies

- arcpy

You need no additional packages, other than the python 2.7 that comes shipped with ArcGIS Desktop.


## Setup
The values that need to be edited for running the tool can be found in `config.py`

- Indicate path of the mxd to handle
- Configure scale levels that are needed (mind the syntax)
- Configure locations that are needed (mind the syntax)

## Run

After setting up the analysis, you can run `main.py` and the results will be generated.
Hooray.