#!/usr/bin/python3
# define network both here and on top level file
nodes = {
    1: {
        "h1": "192.168.1.1",
        "h2": "192.168.2.1",
        "h3": "192.168.3.1",
        "r1": "10.0.1.1",
        "r2": "10.0.1.2",
        "r3": "10.0.2.2",
        "r4": "10.0.4.1",
        "r5": "10.0.4.2",
        "r6": "10.0.3.2",
        "r7": "10.0.7.1",
        "r8": "10.0.7.2",
        "r9": "10.0.6.2"
    },
    2:{
        "h1": "192.168.1.1",
        "h2": "192.168.2.1",
        "h3": "192.168.3.1",
        "h4": "192.168.4.1",
        "r1": "10.0.1.1",
        "r2": "10.0.1.2",
        "r3": "10.0.1.3",
        "r4": "10.0.1.4",
        "r5": "10.0.2.2",
        "r6": "10.0.3.2",
        "r7": "10.0.4.2"
    },
    3:{
        "h1": "192.168.1.1",
        "h2": "192.168.2.1",
        "h3": "192.168.3.1",
        "h4": "192.168.4.1",
        "r1": "10.0.1.1",
        "r2": "10.0.1.3",
        "r3": "10.0.1.4",
        "r4": "10.0.4.1",
        "r5": "10.0.3.2",
        "r6": "10.0.5.2"
    }
    
}



routes = {
    4: {"h1": {
            "h2": "r1",
            "h3": "r1",
            "h4": "r1",
            "r1": "r1",
            "r2": "r1",
            "r3": "r1",
            "r4": "r1",
            "r5": "r1",
            "r6": "r1",
            "r7": "r1"
        },
        "h2": {
            "h1": "r7",
            "h3": "r7",
            "h4": "r7",
            "r1": "r7",
            "r2": "r7",
            "r3": "r7",
            "r4": "r7",
            "r5": "r7",
            "r6": "r7",
            "r7": "r7"
        },
        "h3": {
            "h1": "r4",
            "h2": "r4",
            "h4": "r4",
            "r1": "r4",
            "r2": "r4",
            "r3": "r4",
            "r4": "r4",
            "r5": "r4",
            "r6": "r4",
            "r7": "r4"
        },
        "h4": {
            "h1": "r5",
            "h2": "r5",
            "h3": "r5",
            "r1": "r5",
            "r2": "r5",
            "r3": "r5",
            "r4": "r5",
            "r5": "r5",
            "r6": "r5",
            "r7": "r5"
        },
        "r1": {
            "h1": "h1",
            "h2": "r2",
            "h3": "r3",
            "h4": "r3",
            "r2": "r2",
            "r3": "r3",
            "r4": "r3",
            "r5": "r3",
            "r6": "r2",
            "r7": "r2"
        },
        "r2": {
            "h1": "r1",
            "h2": "r6",
            "h3": "r3",
            "h4": "r3",
            "r1": "r1",
            "r3": "r3",
            "r4": "r3",
            "r5": "r3",
            "r6": "r6",
            "r7": "r6"
        },
        "r3": {
            "h1": "r1",
            "h2": "r2",
            "h3": "r4",
            "h4": "r5",
            "r1": "r1",
            "r2": "r2",
            "r4": "r4",
            "r5": "r5",
            "r6": "r2",
            "r7": "r2"
        },
        "r4": {
            "h1": "r3",
            "h2": "r3",
            "h3": "h3",
            "h4": "r3",
            "r1": "r3",
            "r2": "r3",
            "r3": "r3",
            "r5": "r3",
            "r6": "r3",
            "r7": "r3"
        },
        "r5": {
            "h1": "r3",
            "h2": "r3",
            "h3": "r3",
            "h4": "h4",
            "r1": "r3",
            "r2": "r3",
            "r3": "r3",
            "r4": "r3",
            "r6": "r3",
            "r7": "r3"
        },
        "r6": {
            "h1": "r2",
            "h2": "r7",
            "h3": "r2",
            "h4": "r2",
            "r1": "r2",
            "r2": "r2",
            "r3": "r2",
            "r4": "r2",
            "r5": "r2",
            "r7": "r7"
        },
        "r7": {
            "h1": "r6",
            "h2": "h2",
            "h3": "r6",
            "h4": "r6",
            "r1": "r6",
            "r2": "r6",
            "r3": "r6",
            "r4": "r6",
            "r5": "r6",
            "r6": "r6"
        }}
}
links ={
    1:[
        ("r1","r2"),
        ("r2","r3"),
        ("r3","h1"),
        ("r3","r6"),
        ("r4","r5"),
        ("r5","r6"),
        ("r6","h2"),
        ("r6","r9"),
        ("r7","r8"),
        ("r8","r9"),
        ("r9","h3")
    ],
    2:[
        ("r1","r2"),
        ("r1","r3"),
        ("r1","r4"),
        ("r2","r5"),
        ("r3","r6"),
        ("r4","r7"),
        ("r5","h6"),
        ("r6","r7"),
        ("r1","h1"),
        ("r5","h2"),
        ("r6","h3"),
        ("r7","h4")
    ],
    3:[
        ("r1","r2"),
        ("r1","r3"),
        ("r2","r4"),
        ("r3","r4"),
        ("r3","r5"),
        ("r5","r6"),
        ("r1","h1"),
        ("r4","h2"),
        ("r6","h3"),
        ("r6","h4")
        
    ],
    4:[
        ("r1","r2"),
        ("r1","r3"),
        ("r2","r3"),
        ("r2","r6"),
        ("r3","r4"),
        ("r3","r5"),
        ("r6","r7"),
        ("r1","h1"),
        ("r7","h2"),
        ("r4","h3"),
        ("r5","h4")
    ]
}
staticRP ={
    1: "r5",
    2: "r3",
    3: "r5"
}


multicast_destinations_ex1 = [
    "h1",
    "h2",
    "h3"
]
