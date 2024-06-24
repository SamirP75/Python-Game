# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!IMPORTANT!!!!!!!!!!! !!!!!!!!!!MUST READ BEFORE PLAYING THE GAME!!!!!!!!!!!!!!!!!!!!
# This is under development so don't expect much 
# At night, monsters might come out (you don't want to be out in the dark)
# Use your coins wisely.
# If you dodge an attack, you take zero damage, but you get stunned. If you get stunned, you cannot attack the monster the next round.

'''
import os
coin_count = 50
hp = 100
character = input("Select your character: Jack, Emily, Michael, Sarah ")
if character == 'Jack':
	print("Stats:\nStrength:25\nDefense:25\nMelee:50\nFlexibility:20\nIntelligence:80")
	question = input('Are you sure you want to select Jack? ')
	if question == 'Yes':
		import Jack
	elif question == 'No':
		character1 = input("Select your character: Jack, Emily, Michael, Sarah ")
		if character1 == 'Jack':
			print("Stats:\nStrength:25\nDefense:25\nMelee:50\nFlexibility:20\nIntelligence:80")
		question_1 = input('Are you sure you want to select Jack? ')
		# noinspection PyUnboundLocalVariable
		if question_1 == 'Yes':
			import Jack
		if question_1 == 'No':
			print('Restart console to play again.')
		elif character1 == 'Emily':
			print("Stats:\nStrength:15\nDefense:40\nMelee:30\nFlexibility:60\nIntelligence:80")
			question_2 = input('Are you sure you want to select Emily? ')
		# noinspection PyUnboundLocalVariable
			if question_2 == 'Yes':
				print("ok")
			elif question_2 == 'No':
				print('Restart console to play again.')
		elif character1 == 'Michael':
			print("Stats:\nStrength:70\nDefense:40\nMelee:85\nFlexibility:0\nIntelligence:30")
			question_3 = input('Are you sure you want to select Michael? ')
		# noinspection PyUnboundLocalVariable
			if question_3 == 'Yes':
				pass
			elif question_3 == 'No':
				print('Restart console to play again.')
		elif character1 == 'Sarah':
			print("Stats:\nStrength:40\nDefense:70\nMelee:21\nFlexibility:85\nIntelligence:40")
			question_4 = input('Are you sure you want to select Sarah')
		# noinspection PyUnboundLocalVariable
		if question_4 == 'Yes':
			pass
		elif question_4 == 'No':
			print('Restart console to play again.')

if character == 'Emily':
	print("Stats:\nStrength:15\nDefense:40\nMelee:30\nFlexibility:60\nIntelligence:80")
	question_5 = input('Are you sure you want to select Emily ')
	if question_5 == 'Yes':
		pass
	if question_5 == 'No':
		question_6 = input('Select your character: Jack, Emily, Michael, Sarah ')
		if question_6 == 'Jack':
			question_7 = input('Are you sure you want to select Jack? ')
			if question_7 == 'Yes':
				import Jack
			if question_7 == 'No':
				print('Restart console to play again.')
		if question_6 == 'Emily':
			question_8 = input('Are you sure you want to be Emily? ')
			if question_8 == 'Yes':
				pass
			elif question_8 == 'No':
				print('Restart console to play again.')
		elif question_6 == 'Michael':
			question_9 = input('Are you sure you want to me Michael? ')
			if question_9 == 'Yes':
				pass
			elif question_9 == 'No':
				print('Restart console to play again.')
		elif question_6 == 'Sarah':
			question_10 = input('Are you sure you want to be Sarah')
			if question_10 == 'Yes':
				pass
			elif question_10 == 'No':
				print('Restart console to play again.')

if character == 'Michael':
	print("Stats:\nStrength:70\nDefense:40\nMelee:85\nFlexibility:0\nIntelligence:30")
	question_11 = input('Are you sure you want to select Michael?')
	if question_11 == 'Yes':
		pass
	elif question_11 == 'No':
		question_12 = input('Select your character: Jack, Emily, Michael, Sarah ')
		if question_12 == 'Jack':
			question_13 = input('Are you sure you want to select Jack? ')
			if question_13 == 'Yes':
				import Jack
			elif question_13 == 'No':
				print('Restart console to play again.')
		if question_12 == 'Emily':
			question_14 = input('Are you sure you want to be Emily? ')
			if question_14 == 'Yes':
				pass
			elif question_14 == 'No':
				print('Restart console to play again.')
		if question_12 == 'Michael':
			question_15 = input('Are you sure you want to be Michael?')
	# noinspection PyUnboundLocalVariable
	if question_15 == 'Yes':
		pass
	elif question_15 == 'No':
		print('Restart console to play again.')
	# noinspection PyUnboundLocalVariable
	if question_12 == 'Sarah':
		question_16: str = input('Are you sure you want to be Sarah')
	# noinspection PyUnboundLocalVariable
	if question_16 == 'Yes':
		pass
	elif question_16 == 'No':
		print('Restart console to play again.')

if character == 'Sarah':
	print("Stats:\nStrength:40\nDefense:70\nMelee:21\nFlexibility:85\nIntelligence:40")
'''