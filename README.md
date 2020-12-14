# lip2wav revised 
This project is in order to reproduct the paper of lip2wav.

Now I place some codes that I wrote to help me do this work on my Win10 PC. 

## preprocess.py 
This code is copied and adapted for my Windows enviroment. 

`vfile.replace` has been revised so that can generate images, wav, npz files correctly on my computer.

The usage of this code is the same as https://github.com/Rudrabha/Lip2Wav .

## preprocess\_win\_mv.py
The pathes replacements in preprocess.py have problem on Windows. 
But the cost of that code is so long that I write this code to move files .(10.5 hours of dl speaker's)

You need run as : 
`python preprocess_win_mv.py <name>`

Using Example :
`python preprocess_win_mv.py dl`

<font color = 'red'>This code is quicker a lot than `preprocess_win_cp.py`.</font> 

## preprocess\_win\_cp.py
The pathes replacements in `preprocess.py` have problem on Windows and I repaired this bug.
But the cost of that code is so long that I write this code to move files .(about 10.5 hours of dl speaker's)

You need run as : 
`python preprocess_win_cp.py <name>`

Using Example :
`python preprocess_win_cp.py dl`

If you want to remove directory of speaker after files movement, you can add the argument as `--remove_dir`:
`python preprocess_win_cp.py dl --remove_dir`

## file\_move\_after\_winmv.py
这份代码是由于`preprocess_win_mv.py`里使用`shutil.move`时用错了
多加了一个cut-0一类的，只好用这个修正文件搬运
使用的是已修正的`preprocess_win_mv.py`则不需要使用这份代码

Using Example :
`python file_move_after_window.py dl`
