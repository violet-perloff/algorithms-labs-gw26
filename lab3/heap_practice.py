"""Part 1: implement Max-Heap sift-down and complete the ascending Heapsort loop."""


def max_heapify_down(arr, i, heap_size):
    """Repair the max-heap property at index i in place."""
    while True:
        left = 2*i + 1
        right = 2*i + 2
        largest = i

        # Check left child
        if left < heap_size and arr[left] > arr[largest]:
            largest = left

        # Check right child
        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        # If i is already the largest, heap property holds
        if largest == i:
            return

        # Otherwise swap and continue sifting down
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def build_max_heap(arr):
  """Provided: build a max-heap from the bottom up, in place."""
  for i in range(len(arr) // 2 - 1, -1, -1):
    max_heapify_down(arr, i, len(arr))


def heap_sort(arr):
    build_max_heap(arr)
    for end in range(len(arr) - 1, 0, -1):
        # Move max to the end
        arr[0], arr[end] = arr[end], arr[0]
        # Repair heap of size `end`
        max_heapify_down(arr, 0, end)
    return arr


if __name__ == "__main__":
  from lab_checks import check_heap
  raise SystemExit(check_heap(max_heapify_down, build_max_heap, heap_sort))
