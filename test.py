import jnius
import faiss
import os
# os.environ["JAVA_HOME"] = "/Library/Java/JavaVirtualMachines/jdk-11.0.11.jdk/Contents/Home"
java_version = jnius.autoclass("java.lang.System").getProperty("java.version")
num_gpus = faiss.get_num_gpus()
print("number of gpus : " + str(num_gpus))
print("java version : " + java_version)
if java_version.startswith("1.") or java_version.startswith("9."):
    raise RuntimeError("It requires Java 11 or newer, we only found Java %s;", java_version)
