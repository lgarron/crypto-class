import random
import Queue


"""
Based on https://github.com/lgarron/security-games
"""


def experiment(game, challenger, adversary):
  queue_c_to_a = Queue.Queue()
  queue_a_to_c = Queue.Queue()
  challenger(game, queue_a_to_c, queue_c_to_a)
  return adversary(game, queue_c_to_a, queue_a_to_c)


def advantage(challenger, adversary, num_trials):
  num_experiments = num_trials
  W_0 = sum([experiment(0, challenger, adversary) for i in range(num_experiments)]) / float(num_experiments)
  W_1 = sum([experiment(1, challenger, adversary) for i in range(num_experiments)]) / float(num_experiments)
  return abs(W_0 - W_1)



def challenger(game, input, output):
  if game == 0:
    output.put(random.choice(["HEADS", "TAILS"]))
  if game == 1:
    output.put("HEADS")


def A1(challenger, input, output):
    return 1


def A2(challenger, input, output):
    return random.choice([0, 1])


def A3(challenger, input, output):
  m = input.get()
  if m == "HEADS":
    return 1
  if m == "TAILS":
    return 0


# def A4(challenger, input, output):
#   m = input.get()
#   if m == "HEADS":
#     return 1
#   if m == "TAILS":
#     return 0


def A5(challenger, input, output):
  m = input.get()
  if m == "HEADS":
    return random.choice([0, 1])
  if m == "TAILS":
    return 0

print advantage(challenger, A1, 1000)
print advantage(challenger, A2, 1000)
print advantage(challenger, A3, 1000)
# print advantage(challenger, A4, 1000)
print advantage(challenger, A5, 1000)
