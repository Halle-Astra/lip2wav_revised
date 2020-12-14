#preprocessing on windows by copiny
#由于作者的代码中路径切割与替换是针对linux的，而在我发现之前已经用了10.5小时运行preprocess，而其路径在win下失误，故而写此代码进行手动移动文件。
'''
The pathes replacements in preprocess.py have problem on Windows. 
But the cost of that code is so long that I write this code to move files .(10.5 hours of dl speaker's)

You need run as : 
python preprocess_win_cp.py <name>

Using Example :
python preprocess_win_cp.py dl

If you want to remove directory of speaker after files movement, you can add the argument as '--remove_dir':
python preprocess_win_cp.py dl --remove_dir
'''
import os 
import shutil 
import sys 
from tqdm import tqdm 
from multiprocessing import Pool 

def move_file(cut_path,des_path,file,remove):
	old_file = os.path.join(cut_path,file)
	des_fn = os.path.join(des_path,file)#destination filename 
	shutil.copy(old_file,des_fn)
	if remove:
		os.remove(old_file)

if __name__ == '__main__':
	root = 'Dataset'
	remove = False
	speaker = sys.argv[1]
	if len(sys.argv) == 3  and sys.argv[2] == '--remove_dir':
		remove = True
	root = os.path.join(root,speaker)
	intervals_root = os.path.join(root,'intervals')
	res_root = os.path.join(root,'preprocessed')
	dirs_ = os.listdir(intervals_root)
	dirs_ = [os.path.join(intervals_root,i) for i in dirs_]
	pbar = tqdm(total=len(dirs_)) # each cut directory copying
	for dir_ in dirs_:
		dir_temp = os.listdir(dir_)
		dir_temp = [i for i in dir_temp if '.mp4' not in i]
		for cut_dir in dir_temp:
			dir_fe = os.path.split(dir_)[-1] # dir final element
			cut_path = os.path.join(dir_,cut_dir)
			des_path = os.path.join(res_root,dir_fe,cut_dir)
			if not os.path.exists(des_path):
				os.makedirs(des_path)
			pool = Pool(8)
			for file in os.listdir(cut_path):
				pool.apply_async(move_file,args = (cut_path,des_path,file,remove))
			pool.close()
			pool.join()
			if remove:
				os.rmdir(cut_path)
			#print('\r',cut_path,' is moved.',end = '')
		pbar.update(1)
	
