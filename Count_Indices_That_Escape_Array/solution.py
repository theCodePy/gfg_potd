from collections import defaultdict

class Solution:
    def goodIndices(self, arr):
        good_indx = defaultdict(int)
        bad_indx = defaultdict(int)
        l = len(arr)
        i  = 0
        while i <l:
            if good_indx[i] or bad_indx[i]:
                i+=1
                continue
            tmp_seen = defaultdict(int)
            j = i
            while True:
                if j< 0 or j >= l or good_indx[j]:
                    for k in tmp_seen:
                        if tmp_seen[k]:
                            good_indx[k] = 1
                            print(f"good index {k}")
                    break
                elif tmp_seen[j] or bad_indx[j]:
                    for k in tmp_seen:
                        if tmp_seen[k]:
                            bad_indx[k] = 1
                            print(f"bad index {k}")
                    break
                elif not tmp_seen[j]:
                    tmp_seen[j] = 1
                
                j =  j + arr[j]
            i+=1
        good_count = 0
        for k in good_indx:
            if good_indx[k]:
                good_count += 1

        return good_count


if __name__ == "__main__":
    arr = [2, 3, -1, 2, -2, 4, 1]
    arr = [5, 4, -6, 7]
    print("Answer: ",Solution().goodIndices(arr))
