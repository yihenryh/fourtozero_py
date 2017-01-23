from collections import deque

class State:
	Win, Loss, Tie, Draw, Undecided = ["Win", "Loss", "Tie", "Draw", "Undecided"]

def initial_position():
	return 4

def primitive(pos):
	if pos == 0:
		return State.Loss
	return State.Undecided

def gen_moves(pos):
	if pos >= 1:
		yield 1
	if pos >= 2:
		yield 2

def do_moves(pos, move):
	return pos - move;

#should work for drawless games
def solve():
	strat = dict()

	seen = set([initial_position()])
	q = deque([initial_position()]) #use as queue
	s = deque() #use as stack

	#traverse game tree to the primitives
	while len(q) != 0:
		pos = q.popleft()
		s.append(pos)

		if primitive(pos) is State.Loss:
			strat[pos] = State.Loss
			continue

		for move in gen_moves(pos):
			new_pos = do_moves(pos, move)

			if new_pos not in seen:
				q.append(new_pos)
				seen.add(new_pos)

	#build game tree back up to initial_position, using the stack
	while len(s) != 0:
		pos = s.pop()

		loss_child = False
		tie_child = False

		#win: there exists a child that is a loss
		#loss: all children are win
		#tie: no child is a loss, and there is a child that is a tie
		for move in gen_moves(pos):
			prim = strat[do_moves(pos, move)]

			if prim is State.Loss:
				loss_child = True
				break
			elif prim is State.Tie:
				tie_child = True

		if loss_child:
			strat[pos] = State.Win
		elif tie_child:
			strat[pos] = State.Tie
		else:
			strat[pos] = State.Loss

	print strat[initial_position()]


for i in range(100):
	initial_position = lambda: i
	print i,
	solve()


