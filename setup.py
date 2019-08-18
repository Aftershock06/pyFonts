import subprocess


cmd = "sudo mv -v fonts/* ~/usr/local/share/fonts/truetype/"
subprocess.call(cmd)
