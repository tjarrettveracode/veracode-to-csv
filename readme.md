[![travis-ci build status](https://travis-ci.org/ctcampbell/veracode-to-csv.svg?branch=master)](https://travis-ci.org/ctcampbell/veracode-to-csv)

This is not an official Veracode project. The Veracode support team will not be able to assist with troubleshooting. Please raise an issue on this project for improvements or bug fixes.

# Install

`pip install veracodetocsv`

Supports Python 2.7 and 3.6+

API credentials must be enabled on a Veracode account and placed in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>

File permissions should be set appropriately

    chmod 600 ~/.veracode/credentials

# Configure

An example configuration file is provided `config_example.py` which can be passed on the command line using `-c`. Defaults are as shown:

    # Logging
    # debug_logging = True
    
    # Directory to output .csv files
    output_directory = "output"
    
    # UTF-8 encoded text file containing list of application profile names to include.
    # Note - an empty file will include all application profiles
    # app_include_list = "app_include_list.txt"
    
    # Include static/dynamic flaws
    include_static_flaws = True
    include_dynamic_flaws = True
    
    # Include sandboxes
    include_sandboxes = True
    
    # Add headers to csv files
    include_csv_headers = True
    
    # Proxy configuration, see http://docs.python-requests.org/en/master/user/advanced/#proxies for options
    # proxies = {"https": "http://user:pass@10.10.10.10:8080/"}

# Run

    veracodetocsv [-c </path/to/config.py>]
    
A text file `processed_builds.txt` keeps track of which builds have been successfully processed. Delete this file to regenerate all CSVs.

# Splunk

`\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}","` can be used as a TIME_PREFIX in props.conf to extract the build_published_date as an event timestamp
