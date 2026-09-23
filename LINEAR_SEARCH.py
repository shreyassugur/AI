arr = [10, 25, 30, 45, 50]
key = int(input("Enter the element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")
