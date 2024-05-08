def printLog(log, type="INFO"):
    if type == "INFO":
        print("\033[0;37m" + "[" + type + "] " + log + "\033[0m")
    elif type == "ERROR":
        print("\033[1;31m" + "[" + type + "] " + log + "\033[0m")
    elif type == "WARNING":
        print("\033[1;33m" + "[" + type + "] " + log + "\033[0m")
    elif type == "SUCCESS":
        print("\033[1;32m" + "[" + type + "] " + log + "\033[0m")
    elif type == "DEBUG":
        print("\033[1;34m" + "[" + type + "] " + log + "\033[0m")
    else:
        print("\033[0;37m" + "[" + type + "] " + log + "\033[0m")
