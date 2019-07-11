import subprocess
with open("stdout.txt","wb") as out, open("stderr.txt","wb") as err:
    subprocess.Popen(["docker", "ps", "-a"],stdout=out,stderr=err)

f = open('stdout.txt')
line = f.readline()

while line:
    line = f.readline()
    subprocess.call(["docker", "rm", f'{line.split(" ")[0]}'])
f.close()

