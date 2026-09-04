import hashlib
import os

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0): 
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName="Data"):

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("Provided path is not a directory")
        return

    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName, fname)

            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate

def DisplayResult(MyDict):

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    Count = 0

    for value in Result:

        for subvalue in value:
            Count = Count + 1
            print(subvalue)

        print("Duplicate Files Count:", Count)
        Count = 0

def DeleteDuplicate(Path="Data"):

    MyDict = FindDuplicate(Path)

    if MyDict is None:
        return

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    DeletedCount = 0

    for value in Result:

        for subvalue in value:

            if " - Copy" in os.path.basename(subvalue):
                print("Deleted File :", subvalue)
                os.remove(subvalue)
                DeletedCount += 1

    print("Total Deleted Files :", DeletedCount)
def main():

    Ret = FindDuplicate()

    if Ret is not None:
        DisplayResult(Ret)
        DeleteDuplicate()

if __name__ == "__main__":
    main()
