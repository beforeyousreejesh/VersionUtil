def compare(version1:str,version2:str):
    version1_tuple=__version(version1)
    version2_tuple=__version(version2)

    if version1_tuple>version2_tuple:
        return 1

    if version1_tuple<version2_tuple:
        return -1
    else:
        return 0
    
def __version(version:str) ->tuple:
    return tuple(map(int,version.split('.')))
