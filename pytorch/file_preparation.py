import argparse
import os
from random import shuffle

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', default='./training_data', type=str,
                    help='The folder path')
parser.add_argument('--train_filename', default='./training_data_list/data_list.txt', type=str,
                    help='The output filename.')
parser.add_argument('--is_shuffled', default='0', type=int,
                    help='Needed to shuffle')

if __name__ == "__main__":

    args = parser.parse_args()

    # make 1 list to save file path
    training_file_names = []

    training_folder = os.listdir(args.folder_path)

    for training_item in training_folder:
        training_item = args.folder_path + "/" + training_item
        training_file_names.append(training_item)

    # print all file paths
    for i in training_file_names:
        print(i)
    # This would print all the files and directories

    # shuffle file names if set
    if args.is_shuffled == 1:
        shuffle(training_file_names)

    # make output file if not existed
    if not os.path.exists(args.train_filename):
        os.open(args.train_filename,os.O_CREAT)

    # write to file
    fo = open(args.train_filename, "w")
    fo.write("\n".join(training_file_names))
    fo.close()

    # print process
    print("Written file is: ", args.train_filename, ", is_shuffle: ", args.is_shuffled)