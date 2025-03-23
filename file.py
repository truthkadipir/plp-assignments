def read_and_modify_file():
    filename=input("input file name: ")
    with open(filename, "r") as file:
        content=file.readlines()
    #modify file
    modified_content=[line.upper() for line in content]

    new_filename="modified_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.writelines(modified_content)
    print(f'Modified file saved as {new_filename}')
    except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again")
    except IOError:
    print("Error: Unable to read the file or wite to the file")
    except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
    read_and_modify_file()
