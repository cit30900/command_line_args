import argparse

def parse_arguments():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Accept and display first name and last name')

    # Define command line arguments for first and last name
    parser.add_argument('--first-name', '-f', required=True, help='First name')
    parser.add_argument('--last-name', '-l', required=True, help='Last name')

    # Parse the command line arguments
    args = parser.parse_args()

    # Return the arguments
    return args

def main():
    # Get the values from the command line arguments
    args = parse_arguments()

    print(f'First Name: {args.first_name}')
    print(f'Last Name: {args.last_name}')


if __name__ == "__main__":
    main()