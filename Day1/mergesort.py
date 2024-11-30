def prepare_gifts(gifts):
    """
    Orders an array of Integers and deletes duplicates during its process by using mergesort algorithm
    Args:
        gifts : List of integers.
    Returns:
        list:Ordered list without duplicates.
    """

    # If list is empty then return an empty list
    if not gifts:
        return []

    # Inner Function to perform mergesort
    def merge_sort(arr):
        # Handle list with 1 element
        if len(arr) <= 1:
            return arr
        # Split list by half
        mid = len(arr) // 2

        # Recursive call of the mergesort in each half
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        # Fuse both halves into a complete array while deleting duplicates
        return merge(left, right)

    # Inner function for merging two ordered lists
    def merge(left, right):
        # Result list
        sorted_list = []
        # Pointers to iterate left and right
        i = j = 0

        while i < len(left) and j < len(right):
            # If element on left is lesser than the one on right then add it to the result list and advance pointer
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            # If element on right is lesser than the one on right then add it to the result list and advance pointer
            elif left[i] > right[j]:
                sorted_list.append(right[j])
                j += 1
            # If both elements are the same append only once and advance both pointers
            else:
                sorted_list.append(left[i])
                i += 1
                j += 1

        # Add any remaining element of left list
        sorted_list.extend(left[i:])
        # Add any remaining element of right ist
        sorted_list.extend(right[j:])

        return sorted_list

    return merge_sort(gifts)
