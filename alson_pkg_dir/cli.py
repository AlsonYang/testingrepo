import click

import os

# @click.command()
def cli():
    return 'return Hello World'
    
import pandas as pd
def create():
    print(os.getcwd())
    pd.DataFrame(columns =[1,2,3] ).to_csv('./data/test.csv', index=False)

if __name__ == '__main__':
    cli()
    create()