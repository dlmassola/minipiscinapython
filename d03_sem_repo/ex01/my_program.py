from path import Path

def main():

    folder = "folder"
    file = "file.txt"

    path = Path(folder)
    path.mkdir()

    content = "EX01 - DAY03"

    file = path / file
    file.write_text(content)

    # Read the content from the file using Path object
    content = file.read_text()

    # Display the content
    print("Lendo conteúdo: ", file)
    print(content)

if __name__ == '__main__':
    main()