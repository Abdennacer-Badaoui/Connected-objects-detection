import csv
from Builder.builder import *
from Guesser.guess import *
from Learner.learn import *
import sys
import argparse
import glob

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=[
                        'guess', 'learn', 'buildDB', 'mergeDB'])
    parser.add_argument("-path", type=str, required='guess' in sys.argv,
                        default="test_db/", nargs=1, help='path of the capture')

    subparser = parser.add_subparsers(
        dest="where", help="choose pcap files to transform")

    d_parser = subparser.add_parser("directory")
    d_parser.add_argument("path", type=str,
                          help="relative path of directory")
    d_parser.add_argument("-dest", type=str,
                          default=["DB/"], nargs=1)
    f_parser = subparser.add_parser("files")
    f_parser.add_argument("path", nargs='+',
                          type=str, help="relative path of file(s)")
    f_parser.add_argument("-dest", type=str,
                          default=["DB/"], nargs=1)

    a_parser = subparser.add_parser("all")
    a_parser.add_argument("-dest", type=str,
                          default=["DB/"], nargs=1)

    args = parser.parse_args()

    if args.action == 'guess':
        ######################################
        ## guess connected object on network##
        ######################################
        txt_xgboost, txt_randomforest = guess(
            args.path[0])
        print(txt_xgboost)
        print(txt_randomforest)

    elif args.action == 'learn':
        ######################################
        # learn from DB and test on small DB #
        ######################################
        txt, mat, _, _ = learn('xgboost')
        print("XGBoost : " + txt)
        print("matrice de confusion :\n", mat)
        txt, mat, _, _ = learn('randomforest')
        print("RandomForestClassifier : " + txt)
        print("matrice de confusion :\n", mat)

    elif args.action == 'mergeDB':
        ######################################
        ##   merge all DB in one csv file   ##
        ######################################

        print("...merging all files from DB/ into a .csv file...")
        if merge():
            print("TrainingDB built. path : Learner/TrainingDB/trainingDB.csv")
        else:
            raise Error("error occur while merging all db")

    elif args.action == 'buildDB':
        #####################################
        ##       build DB from files       ##
        #####################################
        if args.where == 'all':
            pcapFiles = glob.glob("Captures/*.pcap*")
        elif args.where == 'directory':
            pcapFiles = glob.glob(f"{args.path}*.pcap*")
            if not pcapFiles:
                raise FileNotFoundError(
                    f"directory '{args.path}' not found or no pcap_file in it. Try with other directory_name. Try relative path.")
        elif args.where == 'files':
            pcapFiles = []
            for name in args.path:
                if not glob.glob(f"{name}.pcap*"):
                    raise FileNotFoundError(
                        f"file '{name}' not found. Write relative path. Don't write file extension.")
                else:
                    pcapFiles += glob.glob(f"{name}*.pcap*")

        for pcapFile in pcapFiles:

            print(f"try to build database from {pcapFile}...")
            if build(pcapFile, args.dest[0]):
                print(f"{pcapFile} : Done!\n")
            else:
                raise Error(
                    f"error occured while building following file : {pcapFile}")

        print("all pcap files done!")
