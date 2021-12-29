
import time,sys

correctAns=0
for i in range(0,10):
    tries = 3
    start = time.time()
    prompt = str(i) + ' x ' + str(i) + ' = '
    num = input(prompt)
    end = time.time()
    
    if (end-start)>8:
        print('Time limit exceeded')
        time.sleep(1)
        sys.exit()

    if num == str(i*i):
        print('Correct!')
        time.sleep(1)
        correctAns+=1
        continue

    elif num != str(i*i):
        tries-=1
        while tries>0:
            print('Incorrect!!')
            tries-=1
            start = time.time()
            prompt = str(i) + ' x ' + str(i) + ' = '
            num = input(prompt)
            end = time.time()
            if (end-start)>8:
                print('Time limit exceeded')
                time.sleep(1)
                sys.exit()

            if num == str(i*i):
                print('Correct!')
                time.sleep(1)
                correctAns+=1
                break

            elif num != str(i*i):
                continue

        if tries == 0:
            print('Retry limit over')
            
print('Correct answers : '+str(correctAns))
