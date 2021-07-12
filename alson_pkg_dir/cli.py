import click
import pandas as pd
import os
# os.listdir('/Users/yangj2/Desktop/testingrepo/alson_pkg_dir/../data/')
print(os.getcwd())

# @click.command()
def cli():
    return 'return Hello World'
    
def create():
    pd.DataFrame(columns =[1,2,3] ).to_csv('./data/test.csv', index=False)

if __name__ == '__main__':
    cli()
    create()