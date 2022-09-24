import os
import os.path


userIds = [313,314,315,316]

baseDir = "\\192.168.17.100\scora"


version = "v0.99.0"

apkPath = os.path.join(baseDir, "App", "ScoraViewer-"+ version + ".apk")

for id in userIds:
    userDir = os.path.join(baseDir, "user", str(id), "App")
    os.link(apkPath,userDir )