

states = ['NC', 'VT', 'CA', 'WI', 'FL', 'TX']

state_set = set(states)

remove = {'VT', 'CA'}

clean = [s for s in states if s not in remove]

print("Clean:", clean)

set_clean = state_set - remove

print("Set clean:", set_clean)

