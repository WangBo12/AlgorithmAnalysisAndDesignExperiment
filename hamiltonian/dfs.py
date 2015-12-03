#coding=utf8

import copy
from state import StateMemoryLess as State

def find_hamiltonian_in_dfs(vertex , adj_matrix) :
    adj_matrix = copy.copy(adj_matrix) # copy , to avoid change the origin data
    stack = []
    vertex_num = len(vertex)
    # Build Root State
    # just using convex idx 0 for the root 
    root_vertex_id = 0
    previous_vertex_id = -1 
    visited_state = [False] * vertex_num
    root = State(root_vertex_id , previous_vertex_id , visited_state)
    root.init_path_recorder_from_parent(None)
    stack.append(root)
    
    op_nums = 0 

    while len(stack) > 0 :
        # visit stack top
        cur_node = stack.pop()
        cur_node.set_visited()
        cur_node.add_path(cur_node.get_vertex_id())

        op_nums += 1

        ## ready to extend the childs !
        extendable_convex_id_list = cur_node.get_extendable_vertex_id(adj_matrix)
        # check whether extendable
        if len(extendable_convex_id_list) == 0 :
            if cur_node.has_hamiltonian(root_vertex_id,adj_matrix) :
                # print the path
                print cur_node.get_path()
                print op_nums
                return True 
            else :
                continue # no node to be extended ! 
        # extend child
        cur_visited_state = cur_node.get_visited_state()
        previous_vertex_id = cur_node.get_vertex_id()
        for extend_convex_id in extendable_convex_id_list :
            extend_state = State(extend_convex_id ,previous_vertex_id , 
                                 copy.copy(cur_visited_state)) # make a copy .
                           # the copy is necessary . if No Copy , all node share one list
            extend_state.init_path_recorder_from_parent(cur_node)

            stack.append(extend_state)
    return False

        

