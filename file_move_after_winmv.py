import os 
import shutil 
import sys
from multiprocessing import Pool

# 这份代码是由于preprocess_win_mv.py里使用shutil.move时用错了
# 多加了一个cut-0一类的，只好用这个修正文件搬运
# 使用的是已修正的preprocess_win_mv.py则不需要使用这份代码
# Using Example :
# python file_move_after_window.py dl
root = 'Dataset'
root = os.path.join(root,sys.argv[1],'preprocessed')
fs = os.listdir(root)
#for dir_ in fs:
def movefile(dir_):
    dir_ = os.path.join(root,dir_)
    dirs_cut = os.listdir(dir_)
    for dir_unit  in dirs_cut :
            if os.path.exists(os.path.join(dir_,dir_unit,dir_unit)):
                    dir_old = os.path.join(dir_,dir_unit,dir_unit)
                    dir_des = os.path.join(dir_,dir_unit)
                    for file in os.listdir(dir_old):
                        shutil.copy(os.path.join(dir_old,file),os.path.join(dir_des,file))
                        os.remove(os.path.join(dir_old,file))
                        print(os.path.join(dir_old,file),'is removed')
                    #if os.listdir(os.path.join(dir_,dir_unit,dir_unit)):
                    #        fss = os.listdir(os.path.join(dir_,dir_unit,dir_unit))
                    #        [os.remove(os.path.join(os.path.join(dir_,dir_unit,dir_unit),i)) for i in fss]
                    #else:
                    #        os.rmdir(os.path.join(dir_,dir_unit,dir_unit))
                    os.rmdir(dir_old)
                    print(dir_old,'is removed')

if __name__=='__main__':
    pool = Pool(8)
    for dir_ in fs:
        pool.apply_async(movefile,args = (dir_,))
    pool.close()
    pool.join()  