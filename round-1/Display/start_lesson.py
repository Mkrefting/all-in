from datetime import datetime
import random
import time


#get loads of CC/text lines
def get_all():
    with open('random_transcript_lines.txt','r') as f:
        data = f.readlines()
    lines = []
    for line in data:
        lines.append(line.rstrip())
    return lines

#clear lesson_transcript at beginning of new lesson
def clear_file():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('lesson_transcript.txt','w') as f:
        f.write(current_time+'\n')
      

#write a new text line to 'lesson_transcript.txt'
def write_line(line):
    with open('lesson_transcript.txt','a+') as f:
        f.write(line+'\n')
        
    

def start_lesson():
    clear_file()
    all_lines = get_all()
    while True:
        line = random.choice(all_lines)
        write_line(line)
        print(line)
        time.sleep(2.1)


start_lesson()

