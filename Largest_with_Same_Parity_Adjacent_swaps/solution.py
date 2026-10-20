class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        n = len(arr)
        i = 0
        while i < n:
            idx = i
            rem = arr[i] % 2
            sort_req = False
            while i+1 < n and rem == arr[i+1] % 2:
                if arr[i+1] > arr[i] and not sort_req:
                    sort_req = True
                i +=1
            # eve_odd = "EVEN" if rem%2==0 else "ODD"
            # print(f"{eve_odd} detected: from {idx} to {i} = {arr[idx: i+1]}")
            if sort_req:
                arr[idx:i+1] = sorted(arr[idx:i+1], reverse=True) 
            i+=1
        return arr


if __name__ == "__main__":
    arr = [1, 3, 2, 4, 6, 1, 3, 5, 7, 5, 7, 4, 6, 8]
    print(Solution().lexicographicallyLargest(arr))

