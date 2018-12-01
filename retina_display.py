import networkx as nx
import plotly.plotly as py
import plotly.graph_objs as go

graph = nx.read_graphml('mouse_retina_1.graphml')
x_d = nx.get_node_attributes(graph,'x')
y_d = nx.get_node_attributes(graph,'y')
z_d = nx.get_node_attributes(graph,'z')

x_n = []
y_n = []
z_n = []

for i in x_d.keys():
    x_n.append(x_d[i])
    y_n.append(y_d[i])
    z_n.append(z_d[i])

x_e = []
y_e = []
z_e = []

for e in list(graph.edges()):
    try:
        x_e += [x_d[e[0]],x_d[e[1]],None]
        y_e += [y_d[e[0]],y_d[e[1]],None]
        z_e += [z_d[e[0]],z_d[e[1]],None]
    except:
        k = 1

trace1=go.Scatter3d(x=x_e,y=y_e,z=z_e,mode='lines',line=dict(color='rgb(125,125,125)', width=1),hoverinfo='none')

trace2=go.Scatter3d(x=x_n,y=y_n,z=z_n,mode='markers',name='nodes',marker=dict(symbol='circle',size=6,color=z_n,
                    colorscale='Viridis',line=dict(color='rgb(50,50,50)', width=0.5)),
                    text=nx.get_node_attributes(graph,'x').keys(),hoverinfo='text')

#axis=dict(showbackground=False,showline=False,zeroline=False,showgrid=True,showticklabels=False,title='')
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)

data=[trace1, trace2]
fig=go.Figure(data=data, layout=layout)

py.offline.iplot(fig, filename='Mouse_retina_1')
