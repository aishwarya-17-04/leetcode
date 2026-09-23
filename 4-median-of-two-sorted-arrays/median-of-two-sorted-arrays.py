class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2


        if len(B) < len(A):
            A, B = B, A


        l, r = 0, len(A)

        while True:
            i = l + (r-l) // 2
            j = half - i

            Aleft = A[i-1] if i>=1 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")
            Bleft = B[j-1] if j>=1 else float("-infinity")
            Bright = B[j] if j< len(B) else float("infinity")

            if Aleft <= Bright and Bleft<= Aright:
                if total % 2!=0:
                    return float(min(Aright, Bright))
                return(max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            elif Aleft > Bright:
                r = i-1

            else:
                l =i+1
