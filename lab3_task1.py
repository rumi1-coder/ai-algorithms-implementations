def vacum_cleaner():
    cost=0
    goal_state={'A':0,'B':0,'C':0}
    current_state={'A':0,'B':0,'C':0}
    location_input = input("Enter Location of Vacuum")
    #location_input=location_input.upper()
    current_state[location_input] = input("Enter status of " + location_input)

    if location_input=='A':
        current_state['B']=input('Enter status of B : ')
        current_state['C']=input('Enter status of C : ')
    elif location_input=='B':
        current_state['A'] = input('Enter status of A : ')
        current_state['C'] = input('Enter status of C : ')
    else:
        current_state['B'] = input('Enter status of B : ')
        current_state['A'] = input('Enter status of A : ')
    print(current_state)

    if location_input=='A':
        print('vacuum cleaner is in room A ')
        if current_state['A']==0:
           print('room A is clean')
           print('checking other room status...............')
           if current_state['B']==0:
               print('room B is clean')
               cost += 1
               print('cost : ' + str(cost))
               print('checking other room status...............')
               if current_state['C']==0:
                   print('room C is clean')
                   cost += 1
                   print('cost : ' + str(cost))
                   print('All roomed cleaned')
               else:
                   print('room C is dirty')
                   print('cleaned')
                   cost += 2
                   print('cost : ' + str(cost))



           else:
               print('room B is dirty')
               print('cleaned')
               cost+=2
               print('cost : '+str(cost))
               print('checking other room status...............')
               if current_state['C'] == 0:
                   print('room C is clean')
                   cost += 1
                   print('cost : ' + str(cost))
                   print('all roomed cleaned')

               else:
                    print('room C is dirty')
                    print('cleaned')
                    cost += 2
                    print('cost : ' + str(cost))

        else:
           print('room A is dirty')
           print('cleaned')
           cost+=1
           print('cost : '+str(cost))
           print('checking other room status...............')
           if current_state['B'] == 0:
               print('room B is clean')
               cost += 1
               print('cost : ' + str(cost))
               print('checking other room status...............')
               if current_state['C'] == 0:
                   print('room C is clean')
                   cost += 1
                   print('cost : ' + str(cost))
                   print('All roomed cleaned')
               else:
                   print('room C is dirty')
                   print('cleaned')
                   cost += 2
                   print('cost : ' + str(cost))
           else:
               print('room B is dirty')
               print('cleaned')
               cost += 2
               print('cost : ' + str(cost))
               print('checking other room status...............')
               if current_state['C'] == 0:
                   print('room C is clean')
                   cost += 1
                   print('cost : ' + str(cost))
                   print('all roomed cleaned')

               else:
                   print('room C is dirty')
                   print('cleaned')
                   cost += 2
                   print('cost : ' + str(cost))
    elif location_input == 'B':
        print('vacuum cleaner is in room B ')
        if current_state['B'] == 0:
            print('room B is clean')
            print('checking other room status...............')
            if current_state['C'] == 0:
                print('room C is clean')
                cost += 1
                print('cost : ' + str(cost))
                print('checking other room status...............')
                if current_state['A'] == 0:
                    print('room A is clean')
                    cost += 2
                    print('cost : ' + str(cost))
                    print('All roomed cleaned')
                else:
                    print('room A is dirty')
                    print('cleaned')
                    cost += 3
                    print('cost : ' + str(cost))
            else:
                print('room C is dirty')
                print('cleaned')
                cost += 2
                print('cost : ' + str(cost))
                print('checking other room status...............')
                if current_state['A'] == 0:
                    print('room A is clean')
                    cost += 2
                    print('cost : ' + str(cost))
                    print('all roomed cleaned')

                else:
                    print('room A is dirty')
                    print('cleaned')
                    cost += 3
                    print('cost : ' + str(cost))

        else:
            print('room B is dirty')
            print('cleaned')
            cost+=1
            print('cost : ' + str(cost))
            print('checking other room status...............')
            if current_state['A'] == 0:
                print('room A is clean')
                cost += 1
                print('cost : ' + str(cost))
                print('checking other room status...............')
                if current_state['C'] == 0:
                    print('room C is clean')
                    cost += 2
                    print('cost : ' + str(cost))
                    print('All roomed cleaned')
                else:
                    print('room C is dirty')
                    print('cleaned')
                    cost += 3
                    print('cost : ' + str(cost))
            else:
                print('room A is dirty')
                print('cleaned')
                cost += 2
                print('cost : ' + str(cost))
                print('checking other room status...............')
                if current_state['C'] == 0:
                    print('room C is clean')
                    cost += 2
                    print('cost : ' + str(cost))
                    print('all roomed cleaned')

                else:
                    print('room C is dirty')
                    print('cleaned')
                    cost += 3
                    print('cost : ' + str(cost))
    else:
        print('vacuum cleaner is in room C ')
        if current_state['C'] == 0:
            print('room C is clean')
            print('checking other room status...............')
            if current_state['A'] == 0:
                print('room A is clean')
                cost += 2
                print('cost : ' + str(cost))
                print('checking other room status...............')
                if current_state['B'] == 0:
                    print('room B is clean')
                    cost += 1
                    print('cost : ' + str(cost))
                    print('All roomed cleaned')
                else:
                    print('room B is dirty')
                    print('cleaned')
                    cost += 2
                    print('cost : ' + str(cost))
            else:
                print('room A is dirty')
                print('cleaned')
                cost += 3
                print('cost : ' + str(cost))
                print('checking other room status...............')
                if current_state['B'] == 0:
                    print('room B is clean')
                    cost += 1
                    print('cost : ' + str(cost))
                    print('all roomed cleaned')

                else:
                    print('room B is dirty')
                    print('cleaned')
                    cost += 2
                    print('cost : ' + str(cost))

        else:
            print('room C is dirty')
            print('cleaned')
            cost+=1
            print('cost : ' + str(cost))
            print('checking other room status...............')
            if current_state['A'] == 0:
                print('room A is clean')
                cost += 2
                print('cost : ' + str(cost))
                print('checking other room status...............')
                if current_state['B'] == 0:
                    print('room B is clean')
                    cost += 1
                    print('cost : ' + str(cost))
                    print('All roomed cleaned')
                else:
                    print('room B is dirty')
                    print('cleaned')
                    cost += 2
                    print('cost : ' + str(cost))
            else:
                print('room A is dirty')
                print('cleaned')
                cost += 3
                print('cost : ' + str(cost))
                print('checking other room status...............')
                if current_state['B'] == 0:
                    print('room B is clean')
                    cost += 1
                    print('cost : ' + str(cost))
                    print('all roomed cleaned')

                else:
                    print('room B is dirty')
                    print('cleaned')
                    cost += 2
                    print('cost : ' + str(cost))

    #print("Initial Location Condition" + str(goal_state))
vacum_cleaner()