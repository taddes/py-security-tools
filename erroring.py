


def main():
    try:
        f = open('./some_text.txt')
        lines = file.readlines()
        print(lines)
    except FileNotFoundError as e:
        print(f'File was not found {e}')
        import sys
        sys.exit()
    except NameError as e:
        print(f'You misspelled something {e}')
    except Exception as e:
        print(type(e))
        print(f'Error encountered {e}')
    finally:
        print('Fin')
        # f.close()

if __name__ == "__main__":
    main()