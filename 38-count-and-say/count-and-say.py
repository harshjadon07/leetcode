class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"

        for _ in range(n - 1):
            cur = []
            count = 1

            for i in range(1, len(res)):
                if res[i] == res[i - 1]:
                    count += 1
                else:
                    cur.append(str(count))
                    cur.append(res[i - 1])
                    count = 1

            cur.append(str(count))
            cur.append(res[-1])
            res = "".join(cur)

        return res