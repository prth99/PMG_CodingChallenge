import sys

# Get the files passed in args
filenames = sys.argv[1:]

# Setup output
mergedCsv = ""

# Store headers
mergedHeaders = ""

for filename in filenames:
    try:
        with open(filename, "r") as csv:
            headers = True
            for line in csv:
                if headers:
                    # mergedHeaders is just the headers from the last file
                    headers = False
                    mergedHeaders = line
                else:
                    # for each line in the csv file remove the new line character at the end of each line and append the filename 
                    mergedCsv += f"{line.strip()},\"{filename}\"\n"     # line.strip() removes the new line character
    except:
        print("Couldn't open file! Exiting.")
        quit()

# adding headers
mergedHeaders = f"{mergedHeaders[:-1]},\"filename\"\n"  

mergedCsv = mergedHeaders + mergedCsv

print(mergedCsv)

# Run Command: python3 CSV-Combiner.py accessories.csv cleaners.csv clothing.csv > output.csv
