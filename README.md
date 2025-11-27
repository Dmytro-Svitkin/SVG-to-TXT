# SVG-to-TXT Converter

A simple Python utility that converts SVG files into plain text format.  
It extracts the `<svg>...</svg>` section, removes unnecessary whitespace, and saves the result as a `.txt` file.

## Features
- Select multiple SVG files through a file dialog
- Choose an output folder for the converted files
- Automatically handles duplicate filenames by appending `(1)`, `(2)`, etc.
- Produces clean, one-line text output for each SVG, directly usable as an HTML tag

## Requirements

### For the Python script (`.py `)
- Python 3.x
- Tkinter (included with standard Python installations)

### For the executable (`.exe`)
- Runs directly on Windows with no additional requirements

## Usage
1. Run the program.
2. Select one or more SVG files.
3. Choose an output folder.
4. The converted `.txt` file(s) will be saved in the chosen location.

## License
This project is licensed under the GNU General Public License (GPL).

## Disclaimer
When running the packaged executable (`.exe`), Windows SmartScreen may display a warning.  
This is a common false positive for newly built applications that are unsigned and have not yet built reputation.  
The software is safe to use, and the warning can be bypassed by choosing **"Run anyway"**.  
If you prefer not to bypass the warning or do not fully trust the executable, you can run the Python script version directly instead.
