# commnetsii
run main.py to start up Mininet, with the -E tag to allow for xterms.
after Mininet has started up, xterm h1 h2 h3 h4 r1 r2 r3 r5 r6 r7   **This creates a terminal for each node in the demotopology**
After having generated all the terminals for each node, for each corresponding terminal run node.py with the node name as a parameter.
Example terminal input given terminal for h1:<   python node.py h1    >
After running node.py on each terminal, on h1 which is our Source node, type multicast followed by k paramater for k out of n.
Example terminal input given k=2:<  multicast 2    >
After this, the user should see the packet being forwarded throughout the network with the appropiate acks back to Source node.  
