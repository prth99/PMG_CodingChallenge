import subprocess

TEST_COMMAND = ["python3", "CSV-Combiner.py"]

def runTestCase(testCase):
    command = TEST_COMMAND.copy()
    for item in testCase:
        command.append(item)
    return subprocess.run(command, stdout=subprocess.PIPE)

def testSingleFile():
    testCase = ["accessories.csv"]
    result = runTestCase(testCase)
    return True

def testAllFiles():
    testCase = ["accessories.csv", "cleaners.csv", "clothing.csv"]
    result = runTestCase(testCase)
    return True

def testInvalidFiles():
    testCase = ["foo.csv", "bar.csv", "baz.csv"]
    result = runTestCase(testCase)
    return result.stdout == b"Couldn't open file! Exiting.\n"

def main():
    print(testSingleFile() and testAllFiles() and testInvalidFiles())

if __name__ == '__main__':
    main()