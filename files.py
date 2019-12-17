import psutil

def get_files(keywords=['Windows', 'Program Files']):
    files = []
    for proc in psutil.process_iter():
        try:
            ls = proc.open_files()
        except:
            continue
        if ls == []:
            continue
        for l in ls:
            for keyw in keywords:
                if keyw in (l.path):
                    files.append(l.path)
    return files
