import copy
import sys
import time

sys.setrecursionlimit(10 ** 6)

"""
**************************** Τελεστές Μετάβασης
"""
def goto_1(state):
    if state[5]<10 and state[1]>0: # Έλεγχος αν δεν είναι γεμάτο το ασανσέρ κι αν ο όροφος έχει κατοίκους
        if state[1]>10-state[5]: # Έλεγχος αν δεν χωρούν όλοι οι κάτοικοι στο ασανσέρ
            new_state = [1] + [state[1]-(10-state[5])] + [state[2]] + [state[3]] + [state[4]] + [10]
        else:
            new_state = [1] + [0] + [state[2]] + [state[3]] + [state[4]] + [state[5]+state[1]]
        return new_state
    
    
def goto_2(state):
    if state[5]<10 and state[2]>0:
        if state[2]>10-state[5]:
            new_state = [2] + [state[1]] + [state[2]-(10-state[5])] + [state[3]] + [state[4]] + [10]
        else:
            new_state = [2] + [state[1]] + [0] + [state[3]] + [state[4]] + [state[5]+state[2]]
        return new_state
    
    
def goto_3(state):
    if state[5]<10 and state[3]>0:
        if state[3]>10-state[5]:
            new_state = [3] + [state[1]] + [state[2]] + [state[3]-(10-state[5])] + [state[4]] + [10]
        else:
            new_state = [3] + [state[1]] + [state[2]] + [0] + [state[4]] + [state[5]+state[3]]
        return new_state


def goto_4(state):
    if state[5]<10 and state[4]>0:
        if state[4]>10-state[5]:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [state[4]-(10-state[5])] + [10]
        else:
            new_state = [4] + [state[1]] + [state[2]] + [state[3]] + [0] + [state[5]+state[4]]
        return new_state
    
def goto_0(state):
    new_state = [0] +[state[1]] + [state[2]] + [state[3]] +[state[4]] + [0]
    return new_state

"""
**************************** 
"""

def find_children(state):
    children = []

    # Αντιγράφουμε μια προσωρινή λίστα για να δούμε τι θα γίνει αν
    # πάμε στον όροφο που αναγράφεται, βρίσκουμε διαδόχους
    floor0_state = copy.deepcopy(state) 
    floor0_child = goto_0(floor0_state) 

    floor1_state = copy.deepcopy(state)
    floor1_child = goto_1(floor1_state)
    
    floor2_state = copy.deepcopy(state)
    floor2_child = goto_2(floor2_state)
    
    floor3_state = copy.deepcopy(state)
    floor3_child = goto_3(floor3_state)
    
    floor4_state = copy.deepcopy(state)
    floor4_child = goto_4(floor4_state)

    # Αν υπάρχει επιστροφή στην τιμή βάλτο στην λίστα των διαδόχων
    if floor0_child != None:            
        children.append(floor0_child)
    
    if floor1_child != None:
        children.append(floor1_child)
        
    if floor2_child != None:
        children.append(floor2_child)
    
    if floor3_child != None:
        children.append(floor3_child)
        
    if floor4_child != None:
        children.append(floor4_child)
    return children

def make_front(state): # Το γυρνάει σαν ένα στοιχείο πίνακα
    return [state]

    
def goal_found(front,tail,method):
    print("Goal Found! Front = ",front,"\n\nWith -",method,"-")
    print("\n\nTail:")
    path = tail[0]
    pos = 0
    print(path)
    print("\nSteps:")
    for step in path:
        print(step[pos],"->",end = " ")
    print("End")
    sys.exit(0)

def by_residents(x):
        return x[-1]

def expand_front(front,method):
    #print("--------------------")
    # Κόμβος (node) = Ο τέρμα αριστερός κόμβος τον οποίο θα επεκτείνουμε
    node = front.pop(0)
    # Προηγούμενο μήκος ουράς
    prev_len = len(front)
    last_index = len(front)
    for child in find_children(node):
        if method == 'BFS':
            # Το κάθε παιδί που βρίσκει καταλήγει αντίστροφα απο την φορά που βρέθηκε
            # στον πίνακα, έτσι ώστε να ξεκινάει πρώτα απο τον 4ο όροφο
            front.insert(last_index,child)
        else:    
            # Για κάθε παιδί βάλτο στην αρχή του front
            front.insert(0,child)
    
    if method == 'BestFS':
        #Τωρινό μήκος ουράς
        cur_len = len(front)
        # Πόσα παιδιά προστέθηκαν
        new_children = cur_len - prev_len
        # Τα στοιχεία αποθηκεύονται στο front_for_sort δηλαδή ποιό τμήμα θα κάνει sort
        front_for_sort = front[0:new_children]
        # Θέλω να κάνει sort μόνο τα παιδιά που βρήκε τώρα οπότε απο prev_len μέχρι cur_len
        front_for_sort.sort(key = by_residents)
        for x in range(len(front_for_sort)):
            # Διαγραφή των previously unsorted στοιχείων
            front.pop(0)
            
        for x in front_for_sort:
            # Προσθήκη των sorted καταστάσεων
            front.insert(0,x)
    #print("Front:\n",front)
    return front


def expand_tail(tail,method):
    #print("--------------------")
    # Δημιουργούμε new_Tail για να αφήνουμε την καθ' αυτή tail άθικτη
    new_Tail = copy.deepcopy(tail) 
    
    # Σε κάθε επέκταση θα προσθέτουμε το current_node μαζί με το παιδί που βρίσκουμε
    current_node = new_Tail[0].copy()
    node = new_Tail[0].pop(-1)
    
    # Η πρώτη θέση θα διεγραφτεί γιατι θα επεκταθεί
    new_Tail.pop(0)

    # Το tailLen χρειάζεται στο BFS για insert στο μήκος του και όχι append
    tailLen = len(new_Tail)
    
    BestFS_tmp_arr = []
    
    for child in find_children(node):
        if(method=="DFS"):
            # Για κάθε παιδί βάζουμε στην αρχή του πίνακα την αρχική κατάσταση
            # στην οποία βρισκόνταν
            new_Tail.insert(0,current_node.copy())
        
            # Και στο τέλος προσθέτουμε το παιδί
            new_Tail[0].append(child)
        
        elif(method=="BFS"):
            # Σαν DFS μονο που ότι βρίσκουμε το βάζουμε στην tailLen θέση
            new_Tail.insert(tailLen,current_node.copy())
            
            # Αν το κάναμε απλά append θα επισκεπτόμασταν τους πρώτους ορόφους
            new_Tail[tailLen].append(child)
        else:
            BestFS_tmp_arr.insert(0,child)
    
    if(method == "BestFS"):
        BestFS_tmp_arr.sort(key = by_residents)
        for x in BestFS_tmp_arr:
            new_Tail.insert(0,current_node.copy())
            new_Tail[0].append(x)
    #for x in new_Tail:
        #print(x)
    #print("Tail\n",new_Tail)
    return new_Tail


def find_solution(front,closed,goal,method,tail):
    #time.sleep(0.2)
    if not front:
        # Αν το μέτωπο είναι άδειο δηλαδή δεν υπάρχει τίποτα να ελεγθεί
        print("No Solution Found :(")
    
    elif front[0] == goal:
        goal_found(front[0],tail,method)
        
    
    elif front[0] in closed: 
        # Αν το πρώτο στοιχείο στην λίστα είναι κύκλος δηλαδή έχει επαναληφθεί
        new_front = copy.deepcopy(front)
        # Βγάλτο
        new_front.pop(0)
        new_tail = copy.deepcopy(tail)
        # Βγάλτο κι απο την ουρά
        new_tail.pop(0)
        # Και ξανατρέξε τον αλγόριθμο για το επόμενο node
        find_solution(new_front,closed,goal,method,new_tail)
    
    else:
        closed.append(front[0])
        # Βάζουμε την κατάσταση που βρισκόμαστε στο κενό σύνολο για να μην
        # ξαναβρεθούμε στην ίδια περίπτωση
        front_copy = copy.deepcopy(front)
        front_children = expand_front(front_copy.copy(),method)
        new_tail = expand_tail(tail,method)
        find_solution(front_children,closed,goal,method,new_tail)
    

def main():
    state = [0,12,3,7,8,0] #Όροφος, Κ_1, Κ_2, Κ_3, Κ_4, Χωρητικότητα Ασανσέρ
    goal = [0,0,0,0,0,0]
    method = input("Type \"DFS\", \"BFS\" or \"BestFS\" for solving algorithm: ")
    if method != "DFS" and method != "BFS" and method != "BestFS":
        print("Wrong Input...Exiting Program")
        sys.exit(0)

    tail = [[state]]
    print("Starting search...")
    find_solution(make_front(state),[],goal,method,tail)
           

if __name__ == "__main__":
    main()
