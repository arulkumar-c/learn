def solution(laps):
	print(f'laps = {laps}')
	best_time = {e.split(' ')[0]:int(e.split(' ')[1]) for e in laps[0]}
	#print(f'best_time = {best_time}')

	elemination_list = []

	for lap in laps:
		print('')
		if not best_time:
			# all players got emeninated
			break
		active_scores = {}
		print(f'lap = {lap}')
		for driver_entry in lap:
			driver, cs = driver_entry.split(' ')
			curr_score = int(cs)
			#print(f'lap = {lap}, driver = {driver}, curr_score = {curr_score}')
			if (driver in best_time):
				if (curr_score < best_time[driver]):
					best_time[driver] = curr_score
				if best_time[driver] in active_scores:
					active_scores[best_time[driver]] += [driver]
				else:
					active_scores[best_time[driver]] = [driver]
		print(f'active_scores before trimming = {active_scores}')
		slow_drivers = active_scores.pop(max(active_scores.keys()))
		slow_drivers.sort()
		print(f'active_scores after trimming = {active_scores}')
		print(f'slow_drivers after trimming = {slow_drivers}')
		elemination_list += slow_drivers
		print(f'elemination_list after updating = {elemination_list}')
		print(f'best_time before trimming = {best_time}')
		for driver in slow_drivers:
			best_time.pop(driver)
		print(f'best_time after trimming = {best_time}')

	print('')
	print(f'best_time after all computation = {best_time}')
	#elemination_list += active_scores.keys().sort()
	print(f'elemination_list after all computation = {elemination_list}')

	return(elemination_list)


if __name__ == "__main__":
	print('')
	laps = [
		['Arul 200', 'Bala 403', 'Casy 343', 'Dude 212'],
		['Arul 123', 'Casy 433', 'Bala 343', 'Dude 343'],
		['Dude 123', 'Bala 233', 'Casy 303', 'Arul 212'],
		['Bala 300', 'Arul 433', 'Casy 233', 'Dude 180']
	]
	print(f"solution(laps) = {solution(laps)}\n")


	print('')
	laps = [
		['Harold 154', 'Gina 155', 'Juan 160'],
		['Juan 152', 'Gina 153', 'Harold 160'],
		['Harold 148', 'Gina 150', 'Juan 151']
	]
	print(f"solution(laps) = {solution(laps)}\n")


	print('')
	laps = [
		['Gina 155', 'Eddie 160', 'Joy 161', 'Harold 163'],
		['Gina 153', 'Eddie 161', 'Joy 160', 'Harold 151'],
		['Gina 152', 'Eddie 154', 'Joy 150', 'Harold 149'],
		['Gina 150', 'Eddie 151', 'Joy 155', 'Harold 148']
	]
	print(f"solution(laps) = {solution(laps)}\n")


	laps = [
		['Gina 155', 'Eddie 155', 'Joy 155', 'Harold 155'],
		['Gina 153', 'Eddie 161', 'Joy 160', 'Harold 151'],
		['Gina 152', 'Eddie 154', 'Joy 150', 'Harold 149'],
		['Gina 150', 'Eddie 151', 'Joy 155', 'Harold 148']
	]
	print(f"solution(laps) = {solution(laps)}\n")
