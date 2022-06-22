from download import download
from createData import generateYear, generateMonth, generateLast

# Download and update the dataset
print("downloading data...")
download()

print("Generating dataset...")
print("...year...", end="")
generateYear()
print("Done!")
print("...month...", end="")
generateMonth()
print("Done!")
print("...last...", end="")
generateLast()
print("Done!")
