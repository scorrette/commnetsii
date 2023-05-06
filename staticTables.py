#!/usr/bin/python3
# define network both here and on top level file


nodes_ex1 = {
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
}

nodes_ex2 = {
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

}
nodes_ex3 = {
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

routes = {
    "h1": ["r1"],
    "h2": ["r2"],
    "r1": ["h1", "r2"],
    "r2": ["h2", "r1"]
}
links_ex1 = [
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
]
links_ex2 = [
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
]

links_ex3 = [
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
    
]

staticRP_ex1 = "r5"
staticRP_ex2 = "r3"
staticRP_ex3 = "r5"

multicast_destinations_ex1 = [
    "h1",
    "h2",
    "h3"
]