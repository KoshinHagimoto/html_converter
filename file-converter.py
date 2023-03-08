import sys
import markdown

def validate_inputpath(inputpath):
    try:
        f = open(inputpath)
    except FileNotFoundError:
        print('!!! FileNotFoundError !!!')
        print('the file [' + inputpath + '] is not found.')
        sys.exit('Error')
    f.close()

def converter(inputpath, outputpath):
    with open(inputpath) as f:
        text = f.read()
    with open(outputpath, 'w') as f:
        f.write(markdown.markdown(text))

def main():
    command = sys.argv[1]
    inputpath = sys.argv[2]
    validate_inputpath(inputpath)
    outputpath = sys.argv[3]
    if command == 'markdown':
        converter(inputpath, outputpath)
    else:
        print('!!! this command is unavailable!!!')
        sys.exit()

if __name__ == '__main__':
    main()