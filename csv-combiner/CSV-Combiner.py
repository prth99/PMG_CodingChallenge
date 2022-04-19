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
                    mergedCsv += f"{line.strip()},\"{filename}\"\n"
    except:
        print("Couldn't open file! Exiting.")
        quit()

mergedHeaders = f"{mergedHeaders[:-1]},\"filename\"\n"

mergedCsv = mergedHeaders + mergedCsv

print(mergedCsv)
