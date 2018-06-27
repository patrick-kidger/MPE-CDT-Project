"""
Utility functions to retrieve data from the MOGREPS repository.
"""

from pathlib import Path

import boto3
import botocore


s3 = boto3.resource(
    's3', 
    config=botocore.client.Config(signature_version=botocore.UNSIGNED))


def make_data_object_name(
        dataset_name,
        year, month, day, hour,
        realization, forecast_period):
    """Create a string formatted to give a filename in the MOGREPS dataset."""
    template_string = "prods_op_{}_{:02d}{:02d}{:02d}_{:02d}_{:02d}_{:03d}.nc"
    return template_string.format(
        dataset_name, year, month, day, hour, realization, forecast_period)


def download_data(bucket, name, data_folder=Path("../data")):
    """Download a file from the Amazon AWS.
    If the target already exists, nothing is done.
    
    Retuns a `pathlib.Path` object pointing to the target file."""
    target = data_folder / name
    if not target.exists():
        try:
            print("Downloading {} ...".format(name))
            s3.Bucket(bucket).download_file(name, str(target))
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise
    else:
        print("File {} already exists.".format(target))
        
    return target