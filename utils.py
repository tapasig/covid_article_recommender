from configuration import Configuration
import boto3
import os
import pandas as pd



def download_catalog(config: Configuration):
    """
    Downloads data from S3
    """
    catalog_name, catalog_path = config.catalog.split("/")[-1], config.catalog

    boto3_client = boto3.client(
        "s3",
        region_name=config.s3["region_name"],
        aws_access_key_id=config.s3["access_key"],
        aws_secret_access_key=config.s3["secret_key"],
    )
    boto3_client.download_file(config.s3["bucket"], catalog_name, catalog_path)


def download_data(config: Configuration):
    """
    Downloads data from S3
    """
    data_name, data_path = config.data.split("/")[-1], config.data

    boto3_client = boto3.client(
        "s3",
        region_name=config.s3["region_name"],
        aws_access_key_id=config.s3["access_key"],
        aws_secret_access_key=config.s3["secret_key"],
    )
    boto3_client.download_file(config.s3["bucket"], data_name, data_path)


def load_model(config: Configuration):
    """
    Loads data from disk if available, otherwise its first downloaded from S3.
    """

    if not os.path.exists(config.data):
        download_data(config)

    model = pd.read_csv(config.data)
    model = dict(zip(model['id'], model['recommendations']))
    model = {key: value.split(',') for key, value in model.items()}
    return model


def load_catalog(config: Configuration):
    """
    Loads data from disk if available, otherwise its first downloaded from S3.
    """

    if not os.path.exists(config.catalog):
        download_catalog(config)

    catalog = pd.read_csv('./data/paper_catalog.csv')
    return catalog
