#!/usr/bin/python3
# define network both here and on top level file
nodes = {
    1: {
        "h1": 1,
        "h2": 2,
        "h3": 3,
        "r1": 4,
        "r2": 5,
        "r3": 6,
        "r4": 7,
        "r5": 8,
        "r6": 9,
        "r7": 10,
        "r8": 11,
        "r9": 12
    },
    2: {
        "h1": 1,
        "h2": 2,
        "h3": 3,
        "h4": 4,
        "r1": 5,
        "r2": 6,
        "r3": 7,
        "r4": 8,
        "r5": 9,
        "r6": 10,
        "r7": 11
    },
    3: {
        "h1": 1,
        "h2": 2,
        "h3": 3,
        "h4": 4,
        "r1": 5,
        "r2": 6,
        "r3": 7,
        "r4": 8,
        "r5": 9,
        "r6": 10
    },
    4: {
        "h1": 1,
        "h2": 2,
        "h3": 3,
        "h4": 4,
        "r1": 5,
        "r2": 6,
        "r3": 7,
        "r4": 8,
        "r5": 9,
        "r6": 10,
        "r7": 11
    }
}

nodes_inv = {
    1: {
        1: "h1",
        2: "h2",
        3: "h3",
        4: "r1",
        5: "r2",
        6: "r3",
        7: "r4",
        8: "r5",
        9: "r6",
        10: "r7",
        11: "r8",
        12: "r9"
    },
    2: {
        1: "h1",
        2: "h2",
        3: "h3",
        4: "h4",
        5: "r1",
        6: "r2",
        7: "r3",
        8: "r4",
        9: "r5",
        10: "r6",
        11: "r7"
    },
    3: {
        1: "h1",
        2: "h2",
        3: "h3",
        4: "h4",
        5: "r1",
        6: "r2",
        7: "r3",
        8: "r4",
        9: "r5",
        10: "r6"
    },
    4: {
        1: "h1",
        2: "h2",
        3: "h3",
        4: "h4",
        5: "r1",
        6: "r2",
        7: "r3",
        8: "r4",
        9: "r5",
        10: "r6",
        11: "r7",
    }
}

routes = {
    4: {
        "h1": {
            "h2": ("192.168.1.1", "192.168.1.2"),  # r1
            "h3": ("192.168.1.1", "192.168.1.2"),
            "h4": ("192.168.1.1", "192.168.1.2"),
            "r1": ("192.168.1.1", "192.168.1.2"),
            "r2": ("192.168.1.1", "192.168.1.2"),
            "r3": ("192.168.1.1", "192.168.1.2"),
            "r4": ("192.168.1.1", "192.168.1.2"),
            "r5": ("192.168.1.1", "192.168.1.2"),
            "r6": ("192.168.1.1", "192.168.1.2"),
            "r7": ("192.168.1.1", "192.168.1.2")
        },
        "h2": {
            "h1": ("192.168.2.1", "192.168.2.2"),  # r7
            "h3": ("192.168.2.1", "192.168.2.2"),
            "h4": ("192.168.2.1", "192.168.2.2"),
            "r1": ("192.168.2.1", "192.168.2.2"),
            "r2": ("192.168.2.1", "192.168.2.2"),
            "r3": ("192.168.2.1", "192.168.2.2"),
            "r4": ("192.168.2.1", "192.168.2.2"),
            "r5": ("192.168.2.1", "192.168.2.2"),
            "r6": ("192.168.2.1", "192.168.2.2"),
            "r7": ("192.168.2.1", "192.168.2.2")
        },
        "h3": {
            "h1": ("192.168.3.1", "192.168.3.2"),  # r4
            "h2": ("192.168.3.1", "192.168.3.2"),
            "h4": ("192.168.3.1", "192.168.3.2"),
            "r1": ("192.168.3.1", "192.168.3.2"),
            "r2": ("192.168.3.1", "192.168.3.2"),
            "r3": ("192.168.3.1", "192.168.3.2"),
            "r4": ("192.168.3.1", "192.168.3.2"),
            "r5": ("192.168.3.1", "192.168.3.2"),
            "r6": ("192.168.3.1", "192.168.3.2"),
            "r7": ("192.168.3.1", "192.168.3.2")
        },
        "h4": {
            "h1": ("192.168.4.1", "192.168.4.2"),  # r5
            "h2": ("192.168.4.1", "192.168.4.2"),
            "h3": ("192.168.4.1", "192.168.4.2"),
            "r1": ("192.168.4.1", "192.168.4.2"),
            "r2": ("192.168.4.1", "192.168.4.2"),
            "r3": ("192.168.4.1", "192.168.4.2"),
            "r4": ("192.168.4.1", "192.168.4.2"),
            "r5": ("192.168.4.1", "192.168.4.2"),
            "r6": ("192.168.4.1", "192.168.4.2"),
            "r7": ("192.168.4.1", "192.168.4.2")
        },
        "r1": {
            "h1": ("192.168.1.2", "192.168.1.1"),  # h1
            "h2": ("10.0.2.2", "10.0.2.1"),  # r2
            "h3": ("10.0.3.2", "10.0.3.1"),  # r3
            "h4": ("10.0.3.2", "10.0.3.1"),
            "r2": ("10.0.3.2", "10.0.2.1"),
            "r3": ("10.0.3.2", "10.0.3.1"),
            "r4": ("10.0.3.2", "10.0.3.1"),
            "r5": ("10.0.3.2", "10.0.3.1"),
            "r6": ("10.0.3.2", "10.0.2.1"),
            "r7": ("10.0.3.2", "10.0.2.1")
        },
        "r2": {
            "h1": ("10.0.2.1", "10.0.2.2"),  # r1
            "h2": ("10.0.6.2", "10.0.6.1"),  # r6
            "h3": ("10.1.2.1", "10.1.2.2"),  # r3
            "h4": ("10.1.2.1", "10.1.2.2"),
            "r1": ("10.1.2.1", "10.0.2.2"),
            "r3": ("10.1.2.1", "10.1.2.2"),
            "r4": ("10.1.2.1", "10.1.2.2"),
            "r5": ("10.1.2.1", "10.1.2.2"),
            "r6": ("10.0.6.2", "10.0.6.1"),
            "r7": ("10.0.6.2", "10.0.6.1")
        },
        "r3": {
            "h1": ("10.0.3.1", "10.0.3.2"),  # r1
            "h2": ("10.1.2.2", "10.1.2.1"),  # r2
            "h3": ("10.0.4.2", "10.0.4.1"),  # r4
            "h4": ("10.0.5.2", "10.0.5.1"),  # r5
            "r1": ("10.0.3.1", "10.0.3.2"),
            "r2": ("10.1.2.2", "10.1.2.1"),
            "r4": ("10.0.4.2", "10.0.4.1"),
            "r5": ("10.0.5.2", "10.0.5.1"),
            "r6": ("10.1.2.2", "10.1.2.1"),
            "r7": ("10.1.2.2", "10.1.2.1")
        },
        "r4": {
            "h1": ("10.0.4.1", "10.0.4.2"),  # r3
            "h2": ("10.0.4.1", "10.0.4.2"),
            "h3": ("192.168.3.2", "192.168.3.1"),  # h3
            "h4": ("10.0.4.1", "10.0.4.2"),
            "r1": ("10.0.4.1", "10.0.4.2"),
            "r2": ("10.0.4.1", "10.0.4.2"),
            "r3": ("10.0.4.1", "10.0.4.2"),
            "r5": ("10.0.4.1", "10.0.4.2"),
            "r6": ("10.0.4.1", "10.0.4.2"),
            "r7": ("10.0.4.1", "10.0.4.2")
        },
        "r5": {
            "h1": ("10.0.5.1", "10.0.5.2"),  # r3
            "h2": ("10.0.5.1", "10.0.5.2"),
            "h3": ("10.0.5.1", "10.0.5.2"),
            "h4": ("192.168.4.2", "192.168.4.1"),  # h4
            "r1": ("10.0.5.1", "10.0.5.2"),
            "r2": ("10.0.5.1", "10.0.5.2"),
            "r3": ("10.0.5.1", "10.0.5.2"),
            "r4": ("10.0.5.1", "10.0.5.2"),
            "r6": ("10.0.5.1", "10.0.5.2"),
            "r7": ("10.0.5.1", "10.0.5.2")
        },
        "r6": {
            "h1": ("10.0.6.1", "10.0.6.2"),  # r2
            "h2": ("10.0.7.2", "10.0.7.1"),  # r7
            "h3": ("10.0.6.1", "10.0.6.2"),
            "h4": ("10.0.6.1", "10.0.6.2"),
            "r1": ("10.0.6.1", "10.0.6.2"),
            "r2": ("10.0.6.1", "10.0.6.2"),
            "r3": ("10.0.6.1", "10.0.6.2"),
            "r4": ("10.0.6.1", "10.0.6.2"),
            "r5": ("10.0.6.1", "10.0.6.2"),
            "r7": ("10.0.7.2", "10.0.7.1")
        },
        "r7": {
            "h1": ("10.0.7.1", "10.0.7.2"),  # r6
            "h2": ("192.168.2.2", "192.168.2.1"),  # h2
            "h3": ("10.0.7.1", "10.0.7.2"),
            "h4": ("10.0.7.1", "10.0.7.2"),
            "r1": ("10.0.7.1", "10.0.7.2"),
            "r2": ("10.0.7.1", "10.0.7.2"),
            "r3": ("10.0.7.1", "10.0.7.2"),
            "r4": ("10.0.7.1", "10.0.7.2"),
            "r5": ("10.0.7.1", "10.0.7.2"),
            "r6": ("10.0.7.1", "10.0.7.2")
        }}
}
links = {
    1: [
        ("r1", "r2"),
        ("r2", "r3"),
        ("r3", "h1"),
        ("r3", "r6"),
        ("r4", "r5"),
        ("r5", "r6"),
        ("r6", "h2"),
        ("r6", "r9"),
        ("r7", "r8"),
        ("r8", "r9"),
        ("r9", "h3")
    ],
    2: [
        ("r1", "r2"),
        ("r1", "r3"),
        ("r1", "r4"),
        ("r2", "r5"),
        ("r3", "r6"),
        ("r4", "r7"),
        ("r5", "h6"),
        ("r6", "r7"),
        ("r1", "h1"),
        ("r5", "h2"),
        ("r6", "h3"),
        ("r7", "h4")
    ],
    3: [
        ("r1", "r2"),
        ("r1", "r3"),
        ("r2", "r4"),
        ("r3", "r4"),
        ("r3", "r5"),
        ("r5", "r6"),
        ("r1", "h1"),
        ("r4", "h2"),
        ("r6", "h3"),
        ("r6", "h4")

    ],
    4: [
        ("r1", "r2"),
        ("r1", "r3"),
        ("r2", "r3"),
        ("r2", "r6"),
        ("r3", "r4"),
        ("r3", "r5"),
        ("r6", "r7"),
        ("r1", "h1"),
        ("r7", "h2"),
        ("r4", "h3"),
        ("r5", "h4")
    ]
}
staticRP = {
    1: "r5",
    2: "r3",
    3: "r5",
    4: "r1"
}

interfaces = {
    4: {
        "h1": ["192.168.1.1"],
        "h2": ["192.168.2.1"],
        "h3": ["192.168.3.1"],
        "h4": ["192.168.4.1"],
        "r1": ["192.168.1.2", "10.0.2.2", "10.0.3.2"],
        "r2": ["10.0.2.1", "10.1.2.1", "10.0.6.2"],
        "r3": ["10.0.3.1", "10.1.2.2", "10.0.4.2", "10.0.5.2"],
        "r4": ["192.168.3.2", "10.0.4.1"],
        "r5": ["192.168.4.2", "10.0.5.1"],
        "r6": ["10.0.6.1", "10.0.7.2"],
        "r7": ["192.168.2.2", "10.0.7.1"]
    }
}

multicast_destinations = {
    1: ["h2",
        "h3",
        "h4"],
    2: ["h2",
        "h3",
        "h4"],
    3: ["h2",
        "h3",
        "h4"],
    4: ["h2",
        "h3",
        "h4"],
}
