#encoding = utf-8

def cmd(cmd):
    try:
        import  subprocess
        return subprocess.getoutput(cmd)
    except:
        import subprocess
        return subprocess.check_output(cmd, shell = True)
#         return os.system(cmd)
