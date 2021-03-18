# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

import re
def solution(new_id):
	new_id = new_id.lower()
	new_id = re.sub('[^a-z0-9-_.]', '', new_id)
	
	while '..' in new_id:
        new_id = new_id.replace('..','.')
	
	while True:
        try:
            if new_id[0] == '.':
                new_id = new_id[1:]
            if new_id[-1] == '.':
                new_id = new_id[:-1]
	    except:
	        new_id = new_id
	    if len(new_id)==0:
	        new_id = 'a'
	    if len(new_id) > 15:
	        new_id = new_id[:15]
	    if new_id[0]!='.' and new_id[-1]!='.' and len(new_id)<16:
            break
	
	
	while len(new_id)<3:
        new_id+=new_id[-1]
	
	return new_id


if __name__ == "__main__":
    ni = 	"...!@BaT#*..y.abcdefghijklm"
    solution(ni)
    # "bat.y.abcdefghi"