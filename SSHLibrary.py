import os
import time
	#just put file,can't put directery
def PutFile(IP,Username,Password,LocalPath,RemotePath):
	pc=os.popen("plink -l " + Username +" -pw " + Password + " " + IP + " mkdir -p " + RemotePath)
	buffer=pc.read()
	print buffer
	pc.close()	
	f=open("F:\\Robot\\PutRemoteFile.txt", 'w')
	f.write("cd \"/cygdrive" + RemotePath + "\"\r\n")
	f.write("put \"" + LocalPath + "\"")
	f.close()
	p=os.popen("psftp -l "+ Username +" -pw " + Password + " " + IP + " -b F:\\Robot\\PutRemoteFile.txt")
	buffer=p.read()
	print buffer
	p.close()


	# just get file,can't get directery
def GetFile(IP,Username,Password,LocalPath,RemotePath):
	f=open("F:\\Robot\\GetRemoteFile.txt",'w')
	f.write("lcd \"" + LocalPath + "\"\r\n")
	f.write("get \"/cygdrive" + RemotePath + "\"")
	f.close()
	p=os.popen("psftp -l "+ Username +" -pw " + Password + " " + IP + " -b F:\\Robot\\GetRemoteFile.txt")
	buffer=p.read()
	print buffer
	p.close()


def combine_put_get(ip, username, password, logman1_local_path, logman2_local_path,
					remote_path,local_path_receive,run_time=20,log_file = 'perf_log_test_000001.csv'):
	PutFile(ip, username, password, logman1_local_path, remote_path)
	pl = os.popen("plink -l " + username + " -pw " + password + " " +
				  ip + " chmod 777 /cygdrive" + remote_path + "/logman1.bat")
	buffer = pl.read()
	print buffer
	pl.close()
	p2 = os.popen("plink -l " + username + " -pw " + password + " " +
				  ip + " /cygdrive" + remote_path + "/logman1.bat")
	buffer = p2.read()
	print buffer
	p2.close()
	print("please waiting 50 seconds!")
	time.sleep(int(run_time))
	print '10 seconds'
	print("end waiting!")
	####################3bug#############################3
	PutFile(ip, username, password, logman2_local_path, remote_path)
	p3 = os.popen("plink -l " + username + " -pw " + password + " " +
				  ip + " chmod 777 /cygdrive" + remote_path + "/logman2.bat")
	buffer = p3.read()
	print buffer
	p3.close()
	p4 = os.popen("plink -l " + username + " -pw " + password + " " +
				  ip + " /cygdrive" + remote_path + "/logman2.bat")
	buffer = p4.read()
	print buffer
	p4.close()
	GetFile(ip, username, password, local_path_receive, "/C/PerfLogs/Admin/"+log_file)

