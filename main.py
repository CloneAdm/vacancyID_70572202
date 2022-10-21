def addResult(dPaths: dict, path: str):
    # ДОПИСАТЬ проверку качества пути

    if len(path) > 255:
        print("Слишком длинный путь")
    else:
        if dPaths.get(path, None) is not None:
            dPaths.pop(path)
        else:
            dPaths[path] = len(path)


def getAllPaths(dFS: dict, dPaths: dict, parent:str = ""):

    for nameFolder, content in dFS.items():
        thisPath = parent + nameFolder
        addResult(dPaths, thisPath)

        if isinstance(content, list):
            for nameFile in content:
                fullPathFile = f"{thisPath}/{nameFile}"
                addResult(dPaths, fullPathFile)

        elif isinstance(content, dict):
            getAllPaths(content, dPaths, thisPath + "/")

        else:
            pass


def biggestPath(dFS: dict) -> str:
    dPaths = {"/":1}
    getAllPaths(dFS, dPaths, "/")

    sortedPaths = sorted(dPaths, key=dPaths.get)
    return sortedPaths[-1]


