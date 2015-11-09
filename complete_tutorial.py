import subprocess

def main():
    print('activate_resize')
    errorlevel = subprocess.call('osascript activate_resize.scpt', shell=True)
    assert errorlevel == 0
    print('end activate_resize')

if __name__ == '__main__':
    main()
