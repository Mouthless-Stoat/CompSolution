from math import floor


class Clock:
    hour = 12
    min = 0

    def inc(self):
        self.min += 1
        if self.min >= 60:
            self.min = 0
            self.hour += 1
        if self.hour == 13:
            self.hour = 1

    def is_arith(self):
        seq = list(
            map(
                int,
                list(str(self.hour)),
            ),
        )
        seq += list(
            map(int, list(("0" if self.min < 10 else "") + str(self.min))),
        )

        diff = seq[1] - seq[0]

        for d in range(len(seq) - 1):
            if diff == seq[d + 1] - seq[d]:
                continue
            else:
                return False
        return True


clock = Clock()
table = []

for i in range(720):
    table.append(clock.is_arith())
    clock.inc()

s = sum(table)

time = eval(input()) + 1

print(floor(time / 720) * s + sum(table[0 : (time % 720)]))
