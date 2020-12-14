#preprocessing on windows by copiny
#由于作者的代码中路径切割与替换是针对linux的，而在我发现之前已经用了10.5小时运行preprocess，而其路径在win下失误，故而写此代码进行手动移动文件。
'''
The pathes replacements in preprocess.py have problem on Windows. 
But the cost of that code is so long that I write this code to move files .(10.5 hours of dl speaker's)

You need run as : 
python preprocess_win_mv.py <name>

Using Example :
python preprocess_win_mv.py dl
'''
import os 
import shutil 
import sys 
from tqdm import tqdm 
from multiprocessing import Pool 

def move_dir(dir_,cut_dir,res_root):
	dir_fe = os.path.split(dir_)[-1] # dir final element
	cut_path = os.path.join(dir_,cut_dir)
	des_path = os.path.join(res_root,dir_fe) # 不能加多一层cut_dir，它自己会加一个
	if not os.path.exists(des_path):
		os.makedirs(des_path)
	shutil.move(cut_path,des_path)

if __name__ == '__main__':
	root = 'Dataset'
	speaker = sys.argv[1]
	root = os.path.join(root,speaker)
	intervals_root = os.path.join(root,'intervals')
	res_root = os.path.join(root,'preprocessed')
	dirs_ = os.listdir(intervals_root)
	dirs_ = [os.path.join(intervals_root,i) for i in dirs_]
	pbar = tqdm(total=len(dirs_)) # each cut directory copying
	for dir_ in dirs_:
		dir_temp = os.listdir(dir_)
		dir_temp = [i for i in dir_temp if '.mp4' not in i]
		pool = Pool(8)
		for cut_dir in dir_temp:
			print(dir_,'\n',cut_dir,'\n',res_root)
			pool.apply_async(move_dir,args = (dir_,cut_dir,res_root))
		pool.close()
		pool.join()
		pbar.update(1)
