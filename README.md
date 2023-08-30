# weather_app

This is a simple CLI application that uses Python's pandas and argparse libraries to iterate over a given number of files and generate reports.

## Directory Structure

- `raw_data`: Contains the data files provided by you.
- `file_mover`: Moves/unzips files from any directory specified by the user to the `raw_data` directory.
- `data_formatter`: Converts the raw data into pandas dataframes which are later used.
- `weather_calculations`: Contains models that perform all calculations specified by the task.
- `report_generator`: Forms reports in the format specified by the task.
- `weatherman`: This is the main app which has the code for the CLI.

## Setup Instructions

1. Clone the directory on your system.
2. Install pandas and argparse into your virtual environment.
3. Go to the root directory of the project.
4. Run the project from the terminal using the following command (This is just one example; please read the instructions for other commands as well):
   ```bash
   python weatherman.py <path_to_the_directory_where_your_files_are> -c <YEAR>/<MONTH>

                                                     
5. If there is any confusion typein the terminal:
   ```bash
                               python weatherman.py --help or -h
6. Bonus task can be accessed by:
   ```bash
                               python weatherman.py <path_to_the_directory_where_your_files_are> -b <YEAR>/<MONTH>
7. Provide only YEAR if you are trying to test the first task out of the list of 5 specified in the instructions.For Example:
  ```bash
                               python weatherman.py <path_to_the_directory_where_your_files_are> -e <YEAR>
                                                    
