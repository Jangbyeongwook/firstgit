import pandas as pd
import argparse
from progress import printProgressBar

parser = argparse.ArgumentParser(description='Rename word ""cam"" in csv')
parser.add_argument('--rename', type=str, help='rename')
parser.add_argument('--csv_input', type=str, help='csv input')
parser.add_argument('--csv_output', type=str, help='csv output.')
def renaming(name,input_path, output_path):
    
    printProgressBar(0, 1000, prefix='Converting', suffix='Complete', length=50)


    cols = ['filename','width','height','class','xmin','ymin','xmax','ymax']
    data =[]
    annotations = pd.read_csv(input_path, header=None, names=cols, sep=' *, *', engine='python')

    row_count = annotations.shape[0]
    
    for idx, row in annotations.iterrows():
        row['filename'] = name+row['filename'][3:10]+'.jpg'
        data.append(row)
        printProgressBar(idx, row_count, prefix='Converting', suffix='Complete', length=50)

    output_csv = pd.DataFrame.from_dict(data)
    output_csv = output_csv[cols]
    output_csv.to_csv(output_path, mode='w', index=False, header=False)

if __name__ == '__main__':
    args = parser.parse_args()
    renaming(args.rename, args.csv_input, args.csv_output)