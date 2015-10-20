__author__ = 'mhan'


import graphlab as gl
gl.canvas.set_target('ipynb')

vertices = gl.SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/bond/bond_vertices.csv')
edges = gl.SFrame.read_csv('http://s3.amazonaws.com/dato-datasets/bond/bond_edges.csv')

vertices.show()
edges.show()

g = gl.SGraph()

# add some vertices in a dataflow-ish way
g = g.add_vertices(vertices=vertices, vid_field='name')

# more dataflow
g = g.add_edges(edges=edges, src_field='src', dst_field='dst')

g.get_vertices()
g.get_edges()

# Get all the "friend" edges
g.get_edges(fields={'relation': 'friend'})

pr = gl.pagerank.create(g)
pr.get('pagerank').topk(column_name='pagerank')