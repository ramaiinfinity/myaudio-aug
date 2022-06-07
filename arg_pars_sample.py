import sys
import os
import argparse

parser = argparse.ArgumentParser()

#add parameters
parser.add_argument("--original_dir",type= str, help="Original directory path", default="")
parser.add_argument("--target_dir",type= str, help="Target directory path", default="")
parser.add_argument("--output_file",type= str, help="Output text/csv path with filename", default="")


args = parser.parse_args()

# print(len(sys.argv))
# exit()



# if len(sys.argv) == 4:    
#     if ("" in sys.argv[1]) and  ("" in sys.argv[2]):
#         pass
#     else:
#         print("input_file extension does not match '.txt'")
#         sys.exit()
# #コマンドの引数が合わない場合は中断
# else:
#     print("usage: python batch_cer.py [original_folder_name]  [target_folder_name] [result.txt]")
#     sys.exit()


# path_before= sys.argv[2]
# path_after= sys.argv[1]

# path_before= "scripts3_1"
# path_after= "scripts3_1"

path_before= args.target_dir
path_after= args.original_dir

before_list=os.listdir(path_before)
after_list=os.listdir(path_after)

for file_a, file_b in zip(after_list,before_list):
    # print(" here",os.path.join(path_after,file_a), os.path.join(path_after,file_a))
    if file_a == file_b:
        a=os.path.join(path_after,file_a)
        b=os.path.join(path_before,file_b)
        os.system("python cer.py "+a+" "+b+" "+args.output_file )
    else:
        print(f"File name miss match between {file_a} and {file_b} ")
        sys.exit()