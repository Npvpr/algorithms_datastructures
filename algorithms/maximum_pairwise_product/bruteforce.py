# Time: O(n)
# Space: O(1)
# Just multiply all combinations and find maxmimum product
def mpp_f(garr):
    return max([garr[i] * garr[j] for i in range(len(garr)) for j in range(i + 1, len(garr))])

def mpp_s(garr):
    flg = max(garr)
    garr.remove(flg)
    print(garr)
    slg = max(garr)
    return flg * slg

print(mpp_s([1, 2, 3, 4, 5, 3, 2, 1, 0]))