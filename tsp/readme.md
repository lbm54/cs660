Tsp is our traveling salesman problem implementation using simulated annealing as discussed in class.  
Temperature is just an integer, and we are decrementing by one each time we find a worse solution 
and fail the coin flip.  The main algorithm is similar to the one in the book using probability e^de/temp 
when we do find that worse solution.  Routes are using fully connected graphs but with varying edge weights 
(per our discussion that seemed to be ok?) and change in energy (dE) is calculated by summing up the total 
distances between the cities in two candidate routes.  New routes are then generated merely by swapping 
two cities along the route.  Please see setup.py for how the graph, nodes and edges are set up.  

Thanks!  Let us know if there are any questions in class or on Slack.

To run, please clone and execute python3 tsp_sa.py. The graph and initial route is randomly created each time.
