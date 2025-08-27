def modify_content(text):
    """
    Modify the content of the file by converting it to uppercase.
    
    Parameters:
    text (str): Original content of the file
    
    Returns:
    str: Modified content
    """
    return text.upper()


def read_and_modify_file():
    """
    Prompts the user for a file name, reads the file, modifies its content,
    and writes the modified content to a new file. Handles errors gracefully.
    """
    try:
        input_filename = input("Enter the name of the file to read: ").strip()

        # Open and read the original file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create a new output filename
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"\n✅ Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"\n❌ Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"\n❌ Error: Could not read or write the file '{input_filename}'.")


def create_sample_file():
    """
    Creates a sample file named 'python.txt' with example content.
    """
    sample_content = """Hello Python!
This is a sample file for demonstration.
It will be converted to uppercase."""
    
    with open("python.txt", "w") as file:
        file.write(sample_content)
    
    print("📄 Sample file 'python.txt' has been created.\n")


# ------------------ MAIN EXECUTION ------------------
if __name__ == "__main__":
    create_sample_file()      # Create sample file (optional)
    read_and_modify_file()    # Run main program


