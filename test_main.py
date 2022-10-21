from main import biggestPath

def test_biggest_path1():
    d1 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}
    path = biggestPath(d1)
    assert path == "/dir3/dir5/dir6/dir7"

def test_biggest_path2():
    d2 = {'dir1': ['file1', 'file1']}
    path = biggestPath(d2)
    assert path == "/dir1"  # "/" - данное ожидание считаю ошибочным

def test_biggest_path3():
    d3 = {'dir1': ['file1', 'file2', 'file2']}
    path = biggestPath(d3)
    assert path == "/dir1/file1"
