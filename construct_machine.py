import json

def construct_machine(alphabet):
    tm = {
        "states": [],
        "input_symbols": [], 
        "tape_symbols": [], 
        "initial_state": "q0",
        "accept_state": "accept",
        "reject_state": "reject",
        "transitions": { }
        }
    tm["states"].extend(["q0","q1","accept","reject","found","return"])
    tm["tape_symbols"].append("_")
    
    tm["transitions"]["q0"] = {}
    # Letter iterator
    for let in alphabet: 
        # Adding letter to tape and input symbols
        tm["tape_symbols"].append(let)
        tm["input_symbols"].append(let)
        if(let!=" "):
            findLetter = "find"+str(let)
            #q0 transitions:
            tm["transitions"]["q0"][let+",#,#"] = [findLetter, "#","#","#","S","S","S"]
            
            # Letter finder state/transitions
            tm["states"].append(findLetter)
            tm["transitions"][findLetter]= {
                "#,#,#":[findLetter, "#","#","#", "S","R","R"],
                "#,"+let+",#": ["found","#",let,"#","S","S","S"]
            }
    
    # last transitions:
    tm["transitions"]["found"] = {
        "#,#,var":["return", "var", "#", "#", "S", "S", "S"],
    }
    tm["transitions"]["return"] = {
        "#,#,#":["return", "#", "#", "#", "S", "L", "L"],
        "#,_,_":["q1", "#", "#", "#", "R", "R", "R"]
    }
    tm["transitions"]["q1"] = {
        "_,#,#":["accept", "_", "#", "#", "S", "S", "S"],
        " ,#,#":["q1", " ", "#", "#", "R", "S", "S"],
        "#,#,#":["q0", "#", "#", "#", "S", "S", "S"],
    }
    
    
    with open('machine_config.json', 'w') as file:
        json.dump(tm, file, indent=4)
    