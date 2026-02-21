

if __name__ == '__main__':
    import sys
    if '--debug' in sys.argv:
        print("Debug mode is enabled")
        sys.argv.remove('--debug')
