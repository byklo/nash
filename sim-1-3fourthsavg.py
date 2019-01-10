import collections
import random

# numgens generate the possible "actions" from each player (numbers they pick).
# sim() takes a generator and runs through the possible plays, counting wins and
# games each number participated in. 

def sim1_numgen():
    n = 100
    maxx = 100
    vector = [ 1 for x in xrange(1, n + 1) ]
    yield vector
    while sum(vector) < n * maxx:
        # index
        i = n - 1
        while vector[i] == maxx:
            vector[i] = 1
            i -= 1
        vector[i] += 1
        yield vector

def sim1_samplegen():
    n = 100000
    i = 0
    minn = 1
    maxx = 100
    while i < n:
        yield [ random.randint(minn, maxx) for x in xrange(1, 101) ]
        i += 1


def sim2_numgen():
    for x1 in xrange(1, 101):
        for x2 in xrange(1, 101):
            for x3 in xrange(1, 101):
                yield [x1, x2, x3]

def sim3_numgen():
    for x1 in xrange(1, 101):
        for x2 in xrange(1, 101):
            yield [x1, x2]

def test_numgen(gen, cout=False):
    i = 0
    for nums in gen():
        if cout:
            print nums
        i += 1
    print "printed %i nums" % i



def calc(nums):
    return 1.0 * 3 / 4 / len(nums) * sum(nums)

def who_won(raw_ans, nums):
    diffs = {}
    for x in nums:
        diffs[abs(x - raw_ans)] = x
    return diffs[min(diffs.keys())]

def sim(gen):
    # ans_table = collections.defaultdict(int)
    win_table = collections.defaultdict(int)
    games_table = collections.defaultdict(int)
    for nums in gen():
        raw_ans = calc(nums)
        rounded = int(round(raw_ans))
        winner = who_won(raw_ans, nums)
        # ans_table[rounded] += 1
        seen = {}
        for x in nums:
            if x not in seen:
                games_table[x] += 1
                seen[x] = 1
        win_table[winner] += 1
        # print "game %s, winner %s" % (nums, winner)
    winners = sorted(win_table.items(), key=lambda x: x[1] * 100.0 / games_table[x[0]], reverse=True)
    for winner in winners[:20]:
        n = games_table[winner[0]]
        print "%i won %i/%i games (%0.2f%%)" % (winner[0], winner[1], n, winner[1] * 100.0 / n)

def sim1():
    sim(sim1_numgen)

def randsim1():
    sim(sim1_samplegen)

def sim2():
    sim(sim2_numgen)

def sim3():
    sim(sim3_numgen)

randsim1()
sim1()
sim2()
sim3()
