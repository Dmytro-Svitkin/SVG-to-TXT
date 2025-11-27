# SVG-to-TXT Converter

A simple Python utility that converts SVG files into plain text format.  
It extracts the `<svg>...</svg>` section, removes unnecessary whitespace, and saves the result as a `.txt` file.

## Features
- Select multiple SVG files through a file dialog
- Choose an output folder for the converted files
- Automatically handles duplicate filenames by appending `(1)`, `(2)`, etc.
- Produces clean, one-line text output for each SVG, directly usable as an HTML tag

## Requirements
- Python 3.x
- Tkinter (included with standard Python installations)

## Usage
1. Run the program.
2. Select one or more SVG files.
3. Choose an output folder.
4. The converted `.txt` file(s) will be saved in the chosen location.

## License
This project is licensed under the GNU General Public License (GPL).
