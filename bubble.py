
def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(len(arr)):
        swapped = False

        # Last i elements are already in place
        for j in range(i+1,len(arr)-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if (swapped == False):
            break


# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")    